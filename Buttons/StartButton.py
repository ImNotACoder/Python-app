import tkinter as tk

try:
    from .ButtonCommands import OnClick
    from .GameButtons import *
except ImportError:
    
    from ButtonCommands import OnClick
    from GameButtons import *

def CreateStartButton(win):
    """Create the start button"""

    #Define the start button
    StartButton = tk.Button(win, text="Press to Start!", bg="red", font=("Arial", 40));

    def a():
        """
        Wrapper function for calling arguments
        lambda: argument_list: expression
        """
        CreateGameButtons(win);
        return OnClick.UnplaceStartButton(StartButton);

    #Place the button at position
    StartButton.place(x=50, y=150);

    #Configure the button with the command
    StartButton.configure(command = a);

def CreateGameButtons(win):
    #Create the ScissorsButtons
    CreateScissorsButton(win);

    #Create the PaperButtons
    CreatePaperButton(win);

    #Create the StoneButtons
    CreateStoneButton(win);


#If the file is run as the main file
if __name__ == "__main__":

    #Create a window
    win = tk.Tk();

    #Create the start button in the window
    CreateStartButton(win);

    #Run the window
    win.mainloop();
    