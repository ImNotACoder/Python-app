import random
import tkinter as tk

def UnplaceStartButton(button):
    """Unplace the button"""
    #button.pack_forget() 
    button.place_forget()

def ComputerChoice(win, number):
    """
    scissors = 1
    paper = 2
    stone = 3

    number - x = 1 -> player lose
    number - x = -1 -> player win
    number - x = -2 ->player lose
    number - x = 2 -> player win #put in else
    
    check for stone + scissors
    """
    x=random.randint(1,3);
    main_label= tk.Label(win, width=200, height=200);
    main_label.place(x=200, y=200);
    if(x == number):
        main_label.configure(text="Its a draw");
    elif(number - x == 1):
        main_label.configure(text="You lose");
    elif(number - x == -1):
        main_label.configure(text="You win");
    elif((number == 3) and (x == 1)):
        main_label.configure(text="You win");
    elif((number == 1) and (x == 3)):
        main_label.configure(text="You lose");


    main_label.pack()
    

    