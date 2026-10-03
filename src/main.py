import gui_layout

import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

class MainProgram(ctk.CTk):
    def program_close(self):
        if messagebox.askyesno(
            "Discard Changes?",
            f"You are about to quit the program.\nDiscard changes to current session?"
        ):
            self.destroy()

    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("LBP Popit Color Generator")
        self.geometry('540x260')
        self.resizable(False, False)

        # Program
        gui_layout.ColorTabList(self)

        self.protocol('WM_DELETE_WINDOW', lambda: self.program_close())
        self.mainloop()


def main():
    MainProgram()

if __name__ == '__main__':
    main() 
