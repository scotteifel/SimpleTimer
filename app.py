import os
path = os.getcwd()
if not os.path.isfile('main.db'):
   with open(os.path.join(path, 'main.db'), 'w+') as file:
     pass

import tkinter as tk
from db import *
from datetime import datetime

start_time = datetime.now().strftime("%I:%M %p")

class MainWindow(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.timer = start_timer()[0]
        # Just start from zero.
        self.timer = 0
        self.render_widgets()
        self.pack()
        self.increment()

    def render_widgets(self):
        self.greeting = tk.Label(self.master, text='Welcome')
        self.count = tk.Label(self.master, text=self.timer)
        self.sign_on_time = tk.Label(self.master, text='Start time: ' +
                                     start_time)
        self.pauseBtn = tk.Button(
            self.master, text="Pause", command=self.pause)

        self.greeting.place(x=65, y=15)

        self.sign_on_time.place(x=45, y=40)

        self.count.place(x=85, y=65)

        self.pauseBtn.place(x=74, y=100)

    # Starts the timer count
    def increment(self):
        global routine
        new_time = int(self.count['text']) + 1
        increment_timer(new_time)
        self.count['text'] = str(new_time)
        routine = self.after(60000, self.increment)
        return routine

    def pause(self):
        global routine
        self.after_cancel(routine)

        if self.pauseBtn.cget('text') == 'Pause':
            self.pauseBtn.config(text='Start')
            self.after_cancel(routine)

        else:
            self.pauseBtn.config(text='Pause')
            self.increment()


if __name__ == "__main__":
    timer = start_timer()
    root = tk.Tk()
    root.geometry("200x150")
    root.title('Code Timer')
    app = MainWindow(master=root)
    app.mainloop()
