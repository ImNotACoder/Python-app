import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master = None):
        """Main class for the application
        A template for making a tkinter app

        What does this app do:
        1. Label to update based on textbox
        2. Label to show the counter
        """

        #Call the superclass
        super().__init__(master)

        #Store variables
        self.master = master

        #Create the widgets
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets"""
        #Create the label
        self.main_label = tk.Label(self.master, text = "Click the button")

        #Pack the main label
        self.main_label.pack()

        #Create the variable to show the current count
        self.counter = tk.IntVar()

        #Set the initial value
        self.counter.set(1)

        #Create the label to show the value
        self.counter_label = tk.Label(self.master, textvariable=self.counter)

        #Pack the counter label
        self.counter_label.pack()

        #Create a variable to store a string
        self.str_var = tk.StringVar()

        #Set the initial string
        self.str_var.set("Change text by typing into the entry below")

        #Create an entrybox to store the str_var
        self.entrybox = tk.Entry(self.master)

        #Create the entrybox
        self.entrybox.pack()

        #Create a label to show the string value
        self.str_label = tk.Label(self.master, textvariable = self.str_var)

        #Create the str label
        self.str_label.pack()

        #Create the button for the person to click to increase counter
        self.submit = tk.Button(self.master, text = "Click me to increase counter", command = self.inc)

        #Pack the submit button
        self.submit.pack()

        #Create a button for replacing the label
        self.str_btn = tk.Button(self.master, text = "Click me replace label", command = self.set_text)

        #Pack the str button
        self.str_btn.pack()

    def inc(self):
        """Increment the counter"""
        #Set the counter
        self.counter.set(
            #Get current counter + 1
            self.counter.get() + 1
            )

    def set_text(self):
        """Set the text for the str_var"""

        #Set the str_var value
        self.str_var.set(
            #Get the value from the entrybox
            self.entrybox.get()
            )


#If the file is run at the main file
if __name__ == '__main__':

    #Create the initial window
    root = tk.Tk()

    #Create the application
    app = Application(root)

    #Set the title
    root.title("Test application")

    #Set the geometry
    root.geometry("500x500")

    #Set resizable
    root.resizable()

    #Run the app
    app.mainloop()