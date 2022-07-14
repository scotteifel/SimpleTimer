import tkinter as tk
from db import *
import time


class MainWindow(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # Just start from zero.
        self.timer = 0
        self.increment()
        self.clockTimer()

        self.render_widgets()
        self.pack()

    def render_widgets(self):
        self.greeting = tk.Label(self.master, text='Welcome')

        self.sign_on_time = tk.Label(
            self.master, text='Start time: ' + time.strftime("%I:%M %p"))
        self.current_time = tk.Label(
            self.master)

        self.count = tk.Label(
            self.master, text=self.timer)
        self.pauseBtn = tk.Button(
            self.master, text="Pause", command=self.pause)

        self.greeting.place(x=65, y=15)
        self.sign_on_time.place(x=45, y=40)
        self.current_time.place(x=37, y=65)
        self.count.place(x=85, y=90)
        self.pauseBtn.place(x=72, y=120)

    def clockTimer(self):

        current_time = 'Current time: ' + time.strftime("%I:%M %p")
        self.current_time.config(text=current_time)
        self.current_time.after(100, self.clockTimer)

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
    root = tk.Tk()
    root.geometry("200x180")

    # timer = start_timer()
    root.title('Code Timer')
    app = MainWindow(master=root)
    app.mainloop()
