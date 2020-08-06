import tkinter as tk
try:
      from .ButtonCommands import OnClick
except ImportError:
     from ButtonCommands import OnClick

def CreateStartButton(win):
    StartButton = tk.Button(win, text="Press to Start!", bg="red", font=("Arial", 40))
    StartButton.pack()
    StartButton.configure(command=lambda: OnClick.UnpackStartButton(StartButton))

if __name__ == "__main__":
    win = tk.Tk()
    Test(win)
    win.mainloop()