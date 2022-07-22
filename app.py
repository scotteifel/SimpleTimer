import tkinter as tk
from winsound import Beep

import time

from db import *
from config import *

init_db()


class MainWindow(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        # Start the total time at 0 minutes
        self.timer = 0

        self.timer_val = tk.StringVar(self.master)

        self.render_widgets()
        self.increment()
        self.clock_timer()
        self.pack()

        # Position where the window appears
        c = self.place_window_center(WIDTH, HEIGHT, -300)
        self.master.geometry("%dx%d+%d+%d" % (c[0], c[1], c[2], c[3]))

    def render_widgets(self):
        self.greeting = tk.Label(
            self.master, text='Code Timer', fg=font_color, bg=light_teal_bg_color, font=(font_type, hero_font_size))

        self.sign_on_time = tk.Label(
            self.master, text='Start:  ' + time.strftime("%I:%M %p"), fg=font_color, bg=light_teal_bg_color)
        self.current_time = tk.Label(
            self.master, fg=font_color, bg=light_teal_bg_color)

        self.count = tk.Label(
            self.master, text=self.timer, fg=font_color, bg=light_teal_bg_color)
        self.timer_count = tk.Label(
            self.master, textvariable=self.timer_val, fg=font_color, bg=light_teal_bg_color)
        self.timer_btn = tk.Button(
            self.master, text="Set timer", command=self.set_time, fg=font_color, bg=btn_bg_color)
        self.timer_entry = tk.Entry(
            self.master, width=5,  fg=font_color, bg=btn_bg_color)
        self.pause_btn = tk.Button(
            self.master, text="Pause", command=self.pause, fg=font_color, bg=btn_bg_color)

        self.greeting.place(x=58, y=17)
        self.sign_on_time.place(x=64, y=50)
        self.current_time.place(x=52, y=75)

        self.count.place(x=67, y=97)

        self.timer_count.place(x=61, y=117)

        self.timer_btn.place(x=50, y=142)
        self.timer_entry.place(x=115, y=146)
        self.pause_btn.place(x=83, y=177)

    def clock_timer(self):

        total_time = 'Current:  ' + time.strftime("%I:%M %p")
        self.current_time.config(text=total_time)
        self.current_time.after(100, self.clock_timer)

    def set_time(self):
        timer = self.timer_entry.get()
        self.timer_val.set('Timer: ' + str(timer) + ' mins')
        self.timer_entry.after(int(timer)*60000, self.timer_expired)

    def timer_expired(self):
        self.alert_win = tk.Toplevel(self.master, bg=timer_green_bg)
        self.alert_win.resizable(False, False)

        WIDTH_HEIGHT = 200, 100
        c = self.place_window_center(
            WIDTH_HEIGHT[0], WIDTH_HEIGHT[1], height_offset=-200)
        self.alert_win.geometry("%dx%d+%d+%d" % (c[0], c[1], c[2], c[3]))

        self.message = tk.Label(self.alert_win, text="Times Up.")
        self.message.place(x=72, y=35)

        # Make windows appear on top of other windows
        self.alert_win.attributes('-topmost', True)
        self.alert_win.update()
        self.alert_win.attributes('-topmost', False)

        # Produce beeping noises to show timer is expired
        Beep(2000, 110)
        Beep(2000, 110)
        Beep(2000, 110)

    # Start the timer
    def increment(self):
        global routine
        self.timer += 1
        increment_timer(self.timer)
        self.count['text'] = 'Total: ' + str(self.timer) + ' min'
        routine = self.after(60000, self.increment)
        return routine

    def pause(self):
        global routine
        self.after_cancel(routine)

        if self.pause_btn.cget('text') == 'Pause':
            # Upon restart, offset the added minute from increment()
            self.timer -= 1
            self.pause_btn.config(text='Start')
            self.after_cancel(routine)

        else:
            self.pause_btn.config(text='Pause')
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

    root.title('Code Timer')
    root.config(bg=light_teal_bg_color)
    root.resizable(False, False)

    app = MainWindow(master=root)
    app.mainloop()
