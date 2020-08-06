import tkinter as tk
import tkinter.messagebox

pressed = 0;

try:
    from .ButtonCommands import OnClick
except ImportError:
    from ButtonCommands import OnClick

def CreateScissorsButton(win):
    """Create the scissors button"""
    ScissorsButton=tk.Button(win, text="Scissors", width=10, height=5, command= lambda: OnClick.ComputerChoice(win, 1));
    ScissorsButton.place(x=50, y=50);
   
def CreatePaperButton(win):
    """Create the paper button"""
    PaperButton=tk.Button(win, text="Paper", width=10, height=5, command= lambda: OnClick.ComputerChoice(win, 2));
    PaperButton.place(x=200, y=50);

def CreateStoneButton(win):
    """Create the stone button"""
    StoneButton=tk.Button(win, text="Stone", width=10,height=5, command= lambda: OnClick.Choice(win, 3));
    StoneButton.place(x=350, y=50);



if __name__ == "__main__":

    #Create a window
    win = tk.Tk();

    #Create the scissors button in the window
    CreateScissorsButton(win);

    #Run the window
    win.mainloop();
    