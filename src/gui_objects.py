from dontexecuteme import *

import customtkinter as ctk
import tkinter as tk

class Toolbar(tk.Menu):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # File
        self.file_option = tk.Menu(self, tearoff = 0)

        self.add_cascade(label = 'File', menu = self.file_option)

        # Help
        self.help_option = tk.Menu(self, tearoff = 0)

        self.add_cascade(label = 'Help', menu = self.help_option)

        self.help_option.add_command(
            label = 'About',
            command = None
        )

class RGBSlider(ctk.CTkSlider):
    def __init__(self, master, slider_y_position, *args, **kwargs):
        super().__init__(master, slider_y_position, *args, **kwargs)

        slider_max_value: int = 255
        slider_value_range: int = 256
                
        slider_x_position: int = 260
        slider_y_position: int = slider_y_position

        self.value_variable = tk.IntVar(master)

        self.configure(
            from_ = 0, to = slider_max_value, 
            width = slider_value_range, 
            number_of_steps = slider_value_range,
            variable = self.value_variable
        )

        self.value_variable.set(0)
        self.place(x = slider_x_position, y = slider_y_position)

class RGBLetter(ctk.CTkLabel):
    def __init__(self, master, rgb_letter_selection, rgb_letter_y_position, *args):
        super().__init__(master, rgb_letter_selection, rgb_letter_y_position, *args)

        rgb_letter_x_position: int = 225
        rgb_letter_y_position: int = rgb_letter_y_position

        rgb_letter_text = ['R', 'G', 'B', 'H', 'S', 'V', 'A']
        rgb_letter_selection: int = rgb_letter_text[rgb_letter_selection]

        self.configure(text = rgb_letter_selection)

        self.place(x = rgb_letter_x_position, y = rgb_letter_y_position)

class HexColorField(ctk.CTkEntry):
    def __init__(self, master, positionY: int, *args, **kwargs):
        super().__init__(master, positionY, *args, **kwargs)

        self.positionX = 297
        self.positionY = positionY

        self.configure(
            width = 140,
            validate = 'key'
        )

        self.place(x = self.positionX, y = self.positionY)


def main():
    dont_execute_me()

if __name__ == '__main__':
    main()