import tkinter as tk
from db import *
import datetime


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
        self.greeting.place(x=65, y=40)
        self.count.place(x=85, y=60)

        self.sign_on_time = tk.Label(self.master, text='Start time:   ' +
                                     str(self.timer))

        self.sign_on_time.place(x=60, y=15)

    def increment(self):
        new_time = int(self.count['text']) + 1
        increment_timer(new_time)
        self.count['text'] = str(new_time)
        this = self.after(60000, self.increment)

    # def save_day():
    #
    #     info = self.count['text']
    #     crnt_time = datetime.time
    #     print(datetime)
    #     if
    #
    #     with open('record.txt', 'a+') as file:
    #         file.write(info)


if __name__ == "__main__":
    timer = start_timer()
    root = tk.Tk()
    root.geometry("200x150")
    root.title('Code Timer')
    app = MainWindow(master=root)
    app.mainloop()
