import tkinter as tk

class Application(tk.Frame):
    #declaring independent constructor
    def __init__(self, master=None):
        #getting inherited variables and properties
        super().__init__(master);
        self.master=master;






def main():
    root = tk.Tk()
    app = Application(root);
    root.title("Scissors, paper,stone");
    root.geometry("480x480");
    root.resizeable();
    app.mainloop();
    

if __name__ == "__main__":
    main()