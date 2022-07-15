import time
from turtle import width
from db import *
import tkinter as tk
import os
path = os.getcwd()
if not os.path.isfile('main.db'):
    with open(os.path.join(path, 'main.db'), 'w+') as file:
        pass

WIDTH = 200
HEIGHT = 190
window_size = str(WIDTH)+'x'+str(HEIGHT)

light_teal_bg_color = '#dbfcf1'
font_color = '#27322e'


class MainWindow(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # Just start from zero.
        self.timer = 0
        self.render_widgets()
        self.increment()
        self.clockTimer()
        self.pack()

        # Position the window
        c = self.place_window_center(WIDTH, HEIGHT, -300)
        self.master.geometry("%dx%d+%d+%d" % (c[0], c[1], c[2], c[3]))

    def render_widgets(self):
        self.greeting = tk.Label(
            self.master, text='Code Timer', fg=font_color, bg=light_teal_bg_color, font=10)

        self.sign_on_time = tk.Label(
            self.master, text='Start time:   ' + time.strftime("%I:%M %p"), fg=font_color, bg=light_teal_bg_color)
        self.current_time = tk.Label(
            self.master, fg=font_color, bg=light_teal_bg_color)

        self.count = tk.Label(
            self.master, text=self.timer, fg=font_color, bg=light_teal_bg_color)
        self.pauseBtn = tk.Button(
            self.master, text="Pause", command=self.pause, fg=font_color)

        self.greeting.place(x=61, y=17)
        self.sign_on_time.place(x=48, y=50)
        self.current_time.place(x=40, y=75)
        self.count.place(x=53, y=100)
        self.pauseBtn.place(x=83, y=130)

    def clockTimer(self):

        current_time = 'Current time: ' + time.strftime("%I:%M %p")
        self.current_time.config(text=current_time)
        self.current_time.after(100, self.clockTimer)

    # Start the timer
    def increment(self):
        global routine
        self.timer += 1
        increment_timer(self.timer)
        self.count['text'] = 'Total time: ' + str(self.timer) + ' min'
        routine = self.after(60000, self.increment)
        return routine

    def pause(self):
        global routine
        self.after_cancel(routine)

        if self.pauseBtn.cget('text') == 'Pause':
            # Upon restart, offsets the added minute from increment()
            self.timer -= 1
            self.pauseBtn.config(text='Start')
            self.after_cancel(routine)

        else:
            self.pauseBtn.config(text='Pause')
            self.increment()

    # Enter window size, and a height-offset if ness., returns coords
    def place_window_center(self, width, height, height_offset=0):
        monitor_width = self.master.winfo_screenwidth()
        monitor_height = self.master.winfo_screenheight()

        x_coord = (monitor_width/2) - (width/2)
        y_coord = (monitor_height/2) - (height/2)
        if height_offset != 0:
            y_coord += height_offset
        return width, height, x_coord, y_coord


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry(window_size)

    # timer = start_timer()
    root.title('Code Timer')
    root.config(bg=light_teal_bg_color)
    root.resizable(False, False)
    app = MainWindow(master=root)
    app.mainloop()
