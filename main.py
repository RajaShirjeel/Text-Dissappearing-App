from tkinter import *

class TypingProgram:
    def __init__(self):
        self.started_typing = False
        self.timer_choice = 10
        self.timer = self.timer_choice
        self.window = Tk()
        self.window.geometry('600x400')
        self.window.title("Text Dissappearing App")
        rules_label = Label(text = "The text will disappear in 10 seconds if you do not write anything.",  font=("Helvetica", 12), pady=15, wraplength=500 )
        rules_label.pack()
        self.text = Text(wrap=WORD)
        self.text.pack()
        self.counter_label = Label(text=self.timer, relief=RAISED)
        self.counter_label.pack()
        self.text.bind("<Key>", self.typing_started)
        mainloop()

    def countdown(self):
        if self.started_typing:
            self.timer -= 1
            if self.timer == 0:
                self.delete_reset()
            self.window.after(1000, self.countdown)
            if self.timer != self.timer_choice:
                self.counter_label.config(text=self.timer)
            else:
                self.counter_label.config(text=0)

    def delete_reset(self):
        self.text.delete(1.0, "end")
        self.started_typing = False
        self.timer = self.timer_choice

    def reset_timer(self):
        self.timer = self.timer_choice

    def typing_started(self, key):
        if self.started_typing:
            self.reset_timer()
        else:
            self.started_typing = True
            self.countdown()


if __name__ == "__main__":
    key = TypingProgram()
