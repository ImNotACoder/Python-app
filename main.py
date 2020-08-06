import tkinter as tk
from Buttons import StartButton, GameButtons

class Application(tk.Frame):
    
    def __init__(self, master=None):
        """Constructor for the main application folder"""

        #Inheriting variables from superclass
        super().__init__(master);

        #Store the master
        self.master=master;

        


            
        
def main():
    """Main function for the file"""

    #Create the main application window
    root = tk.Tk()

    #Calling the application class with root as master
    app = Application(root);

    #Set the title for the window
    root.title("Scissors, paper,stone");

    #Set the dimension of the window
    root.geometry("480x480");

    #Toggle if the window is resizable
    #root.resizeable();

    #Create the start button for the root
    StartButton.CreateStartButton(root);

    #Run the mainloop
    app.mainloop();
    
if __name__ == "__main__":
    main()
    