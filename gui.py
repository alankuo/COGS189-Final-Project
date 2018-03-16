from tkinter import Tk, Label, Button, messagebox
import tkinter as tk
import fileinput
import time
import numpy as np
import datetime
import random

# Global variables
running = True 
COLOR = 'black'
id = 0
length = 0

def prepareVal():
    date = str(datetime.datetime.now())
    hour = int(date[11:13])
    minute = int(date[14:16])
    # print("Time: " + str(datetime.datetime.now()))
    print("Hour: " + str(hour))
    print("Minute: " + str(minute))
    SEED = 1
    tiredness = 1
    # Student 1
    # Morning: most energetic
    # Afternoon: energetic
    # Night: less energetic
    # Midnight: tired
    if hour > 7 and hour <= 12:
        SEED = 10
        tiredness = 1
    if hour > 12 and hour <= 18:
        SEED = 15
        tiredness = 2
    if hour > 18 and hour <= 23:
        SEED = 20
        tiredness = 3
    if hour > 23 or hour <= 3:
        SEED = 25
        tiredness = 4
    if hour > 3 and hour <= 7:
        SEED = 25
        tiredness = 5
    return hour, SEED, tiredness

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Focus Up!")

        self.filler = Label(master, pady=40 ,text="")
        self.filler.pack()

        label = Label(master, text="Welcome to Focus-Up Application!!")
        self.label = label
        self.label.pack()

        self.signal = None

        # self.greet_button = Button(master, text="Greet", width=25, command=self.greet)
        # self.greet_button.pack()

        self.filler = Label(master, pady=25 ,text="")
        self.filler.pack()

        self.entry_button = Button(master, text="Start Program", width=25, highlightbackground=COLOR, pady=10, command=self.start)
        self.entry_button.pack()

        # self.pause_button = Button(self.master, text='Pause Program', width=25, highlightbackground=COLOR, pady=10, command=self.pause)
        # self.pause_button.pack()

        self.close_button = Button(master, text="Close Window", width=25, highlightbackground=COLOR, pady=10, command=master.quit)
        self.close_button.pack()

        # self.btn = Button(master,text='Rest', width=25, command=self.clicked)
        # self.btn.pack()

    def reading(self):
        if running:  # Only do this if the Stop button has not been clicked
            hour, SEED, tiredness = prepareVal()
            num = random.randrange(SEED)
            num2 = random.uniform(0.5, 4.0)
            num2 = float("{0:.2f}".format(num2))
            print("Random: " + str(num))
            print("Random2: " + str(num2))
            print("Tiredness: " + str(tiredness))
            if self.signal != None:
                self.signal.destroy()
            else:
                self.read = Label(self.master, text="Reading Your Current Brain Signal...")
                self.read.pack()
            self.signal = Label(self.master, text="Your Current Brain Signal: "+str(num)+"Hz")
            self.signal.pack()
        global id
        id = self.master.after(1000, self.reading)
        global length
        length+=1
        if length > 5:
            self.clicked()


    def start(self):
        """Enable scanning by setting the global flag to True."""
        global running
        running = True
        self.reading()
        #self.start_button.destroy()
        #self.start_button = Button(self.master, text='Pause Program', width=25, highlightbackground=COLOR, pady=10, command=self.pause)
        self.entry_button.configure(text='Pause Program', width=25, highlightbackground=COLOR, pady=10, command=self.pause)

    def pause(self):
        """Stop scanning by setting the global flag to False."""
        global running, id
        running = False
        self.master.after_cancel(id)
        self.entry_button.configure(text="Start Program", width=25, highlightbackground=COLOR, pady=10, command=self.start)
        # print('id in pause is: '+str(id))

    def clicked(self):
        messagebox.showinfo('Take a Rest!!', 'You are not concentrating well enough, \
            take a rest before working on anything else!!!!!')
        self.master.quit()

window = Tk()
my_gui = MyFirstGUI(window)
window.geometry('600x400')
print('HERE ARE THE LOGS:')
window.mainloop()









