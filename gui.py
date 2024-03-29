from tkinter import Tk, Label, Button, messagebox
import tkinter as tk
import fileinput
import time
import numpy as np
import datetime
import random
import pygame

# Morning: 7am - 12pm
# Afternoon: 12pm - 6pm
# Night: 6pm - 9pm
# Midnight 9pm - 1am
# Sleep 1am - 7am

# Global variables
running = True 
COLOR = 'green'
BGCOLOR = '#ebe1a5'
length = 0
alpha = 0
beta = 0
delta = 0
theta = 0
id = 0


# State         Frequency range     State of mind
# Delta         0.5Hz–4Hz           Deep sleep
# Theta         4Hz–8Hz             Drowsiness (also first stage of sleep)
# Alpha         8Hz–14Hz            Relaxed but alert
# Beta          14Hz–30Hz           Highly alert and focused

# Prepare Values
def prepareVal():
    date = str(datetime.datetime.now())
    hour = int(date[11:13])+6
    minute = int(date[14:16])
    # print("Time: " + str(datetime.datetime.now()))
    print("Current Hour: " + str(hour))
    print("Current Minute: " + str(minute))
    # Student 1
    # Morning: most energetic
    # Afternoon: energetic
    # Night: less energetic
    # Midnight: tired
    signal = 0
    meditation = 0
    # Morning
    if hour > 7 and hour <= 12:
        signal = random.uniform(13.5, 30.0)
        signal = float("{0:.2f}".format(signal))
        meditation = random.uniform(50, 80)
        meditation = float("{0:.2f}".format(signal))
    # Afternoon
    if hour > 12 and hour <= 18:
        signal = random.uniform(9.0, 16.0)
        signal = float("{0:.2f}".format(signal))
        meditation = random.uniform(10, 50)
        meditation = float("{0:.2f}".format(signal))
    # Night
    if hour > 18 and hour <= 21:
        signal = random.uniform(6.0, 12.0)
        signal = float("{0:.2f}".format(signal))
        meditation = random.uniform(40, 70)
        meditation = float("{0:.2f}".format(signal))
    # Midnight
    if hour > 21 or hour <= 1:
        signal = random.uniform(4.0, 10.0)
        signal = float("{0:.2f}".format(signal))
        meditation = random.uniform(60, 80)
        meditation = float("{0:.2f}".format(signal))
    # Sleep
    if hour > 1 and hour <= 7:
        signal = random.uniform(0.5, 4.5)
        signal = float("{0:.2f}".format(signal))
        meditation = random.uniform(80, 100)
        meditation = float("{0:.2f}".format(signal))

    global alpha, beta, delta, theta
    if signal <= 4.0:
        delta+=1
    elif signal <= 8.0:
        theta+=1
    elif signal <= 14.0:
        alpha+=1
    else:
        beta+=1
    print('delta level: ' + str(delta))
    print('theta level: ' + str(theta))
    print('alpha level: ' + str(alpha))
    print('beta level: ' + str(beta))
    return signal, meditation

class FocusGUI:
    def __init__(self, master):
        self.master = master
        master.title("Focus Up!")

        self.filler = Label(master, bg=BGCOLOR, pady=40 ,text="")
        self.filler.pack()

        label = Label(master, bg=BGCOLOR, text="Welcome to Focus-Up Application!!")
        self.label = label
        self.label.pack()

        self.signal = None
        self.attentionLvl = None
        self.meditationLvl = None

        # self.greet_button = Button(master, text="Greet", width=25, command=self.greet)
        # self.greet_button.pack()

        self.filler = Label(master, bg=BGCOLOR, pady=25 ,text="")
        self.filler.pack()

        self.entry_button = Button(master, text="Start Program", width=25, highlightbackground=COLOR, pady=10, command=self.start)
        self.entry_button.pack()

        # self.pause_button = Button(self.master, text='Pause Program', width=25, highlightbackground=COLOR, pady=10, command=self.pause)
        # self.pause_button.pack()

        bgImage = tk.PhotoImage(file = "pic.png")
        # self.close_button = Button(master, text="Close Window", width=25, highlightbackground=COLOR, pady=10, command=master.quit)
        self.close_button = Button(master, text="Close Window", width=25, highlightbackground=COLOR, pady=10, command=master.quit)
        self.close_button.pack()

    def reading(self):
        if running:  # Only do this if the Stop button has not been clicked
            brain_signal, meditation_lvl = prepareVal()
            if self.signal != None:
                self.signal.destroy()
                self.attentionLvl.destroy()
                self.meditationLvl.destroy()
            else:
                self.read = Label(self.master, bg=BGCOLOR, text="Reading Your Current Brain Signal...")
                self.read.pack()
            self.signal = Label(self.master, bg=BGCOLOR, text="Your Current Brain Signal: "+str(brain_signal)+"Hz")
            self.signal.pack()
            attention_lvl = brain_signal/30*100
            attention_lvl = str(float("{0:.2f}".format(attention_lvl)))
            meditation_lvl = str(float("{0:.2f}".format(meditation_lvl)))
            print('brain signal: ' + str(brain_signal))
            print('attention level: ' + attention_lvl)
            print('meditation level: ' + meditation_lvl)
            self.attentionLvl = Label(self.master, bg=BGCOLOR, fg="blue", text="Your Attention Level: " + attention_lvl + "/100")
            self.meditationLvl = Label(self.master, bg=BGCOLOR, fg="blue", text="Your Meditation Level: " + meditation_lvl + "/100")
            if float(meditation_lvl) < 30:
                self.meditationLvl.configure(fg="red")
            elif float(meditation_lvl) < 60:
                self.meditationLvl.configure(fg="orange")
            if float(attention_lvl) < 30:
                self.attentionLvl.configure(fg="red")
            elif float(attention_lvl) < 60:
                self.attentionLvl.configure(fg="orange")
            self.attentionLvl.pack()
            self.meditationLvl.pack()
        global id
        id = self.master.after(1000, self.reading)
        global length
        length+=1
        global alpha, beta, delta, theta
        if alpha > 60 or theta > 20 or delta > 5 or length > 1800:
            self.takeRest()


    def start(self):
        """Enable scanning by setting the global flag to True."""
        global running
        running = True
        self.reading()
        #self.start_button.destroy()
        #self.start_button = Button(self.master, text='Pause Program', width=25, highlightbackground=COLOR, pady=10, command=self.pause)
        self.entry_button.configure(text='Pause Program', width=25, highlightbackground=COLOR, bg=COLOR, pady=10, command=self.pause)

    def pause(self):
        """Stop scanning by setting the global flag to False."""
        global running, id
        running = False
        self.master.after_cancel(id)
        self.entry_button.configure(text="Start Program", width=25, highlightbackground=COLOR, bg=COLOR, pady=10, command=self.start)
        # print('id in pause is: '+str(id))

    def takeRest(self):
        messagebox.showinfo('Take a Rest!!', 'You are not concentrating well enough, \
            take a rest before working on anything else!!!!! We will now play a song for you to relax! \
            Feel free to stop the music as you like:)')
        #self.master.quit()
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('mus.mp3')
        self.playMusic()
        self.resetValues();

    def resetValues(self):
        global length, theta, delta
        length = 0
        theta = 0
        delta = 0

    def playMusic(self):
        pygame.mixer.music.play()
        self.pause()
        self.entry_button.configure(text='Stop Music', width=25, highlightbackground='red', bg='red', pady=10, command=self.stopMusic)

    def stopMusic(self):
        pygame.mixer.music.stop()
        self.entry_button.configure(text="Start Program", width=25, highlightbackground=COLOR, bg=COLOR, pady=10, command=self.start)

window = Tk()
my_gui = FocusGUI(window)
window.geometry('600x400')
window.configure(background=BGCOLOR)
print('HERE ARE THE LOGS:')
window.mainloop()









