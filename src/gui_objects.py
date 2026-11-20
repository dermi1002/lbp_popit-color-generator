from dontexecuteme import dont_execute_me

import customtkinter as ctk
import tkinter as tk

class Toolbar(tk.Menu):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # File
        self.optionFile = tk.Menu(self, tearoff = 0)

        self.add_cascade(label = 'File', menu = self.optionFile)

        # Help
        self.optionHelp = tk.Menu(self, tearoff = 0)

        self.add_cascade(label = 'Help', menu = self.optionHelp)

        self.optionHelp.add_command(
            label = 'About',
            command = None
        )

class RGBSlider(ctk.CTkSlider):
    def __init__(self, master, sliderPositionY, *args, **kwargs):
        super().__init__(master, sliderPositionY, *args, **kwargs)

        sliderMaxValue: int = 255
        sliderValueRange: int = 256
                
        sliderPositionX: int = 260
        sliderPositionY: int = sliderPositionY

        self.numberValue = tk.IntVar(master)

        self.configure(
            from_ = 0, to = sliderMaxValue, 
            width = sliderValueRange, 
            number_of_steps = sliderValueRange,
            variable = self.numberValue
        )

        self.numberValue.set(0)
        self.place(x = sliderPositionX, y = sliderPositionY)

class RGBLetter(ctk.CTkLabel):
    def __init__(self, master, rgbLetterSelection, rgbLetterPositionY, *args):
        super().__init__(master, rgbLetterSelection, rgbLetterPositionY, *args)

        rgbLetterPositionX: int = 225
        rgbLetterPositionY: int = rgbLetterPositionY

        rgbLetterText = ['R', 'G', 'B', 'H', 'S', 'V', 'A']
        rgbLetterSelection: int = rgbLetterText[rgbLetterSelection]

        self.configure(text = rgbLetterSelection)

        self.place(x = rgbLetterPositionX, y = rgbLetterPositionY)

class HexColorField(ctk.CTkEntry):
    def certain_characters(self, event):
        if event.char in (
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'A', 'B', 'C', 'D', 'E', 'F',
            'a', 'b', 'c', 'd', 'e', 'f'
        ):
            return True
        elif event.keysym not in (
            'Alt_L', 'F4',
            'BackSpace', 'Return', 'Left', 'Right',
            'Control_L', 'V'
        ):
            return 'break'
        else:
            return False

    def hex_length_limit(self, P):
        if len(P) <= 6:
            return True
        else:
            self.bell()
            return False
    
    def __init__(self, master, positionY: int, *args, **kwargs):
        super().__init__(master, positionY, *args, **kwargs)

        def set_uppercase(*args):
            uppercaseVersion: str = self.hexFieldText.get().upper()
            self.hexFieldText.set(uppercaseVersion)

        self.positionX = 297
        self.positionY = positionY

        self.hexFieldText = tk.StringVar(master)
        self.hexFieldText.trace_add('write', set_uppercase)

        self.lengthCommand = (master.register(self.hex_length_limit), '%P')

        self.configure(
            width = 140,
            validate = 'key',
            validatecommand = self.lengthCommand,
            textvariable = self.hexFieldText
        )

        self.bind('<KeyPress>', self.certain_characters)

        self.place(x = self.positionX, y = self.positionY)


def main():
    dont_execute_me()

if __name__ == '__main__':
    main()