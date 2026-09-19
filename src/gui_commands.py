from dontexecuteme import *

import external_objects

import customtkinter as ctk
import pyperclip

def copy_hex_color(text):
    pyperclip.copy(text)

def change_color_sliders(
    red: int, green: int, blue: int,
    hexField, colorSquare
    ):

    color_print_hex = '%02X%02X%02X' % (red, green, blue)

    hexField.delete(0, ctk.END)
    hexField.insert(0, color_print_hex)

    newColorHex = hexField._textvariable.get()
    
    colorSquare.configure(
        background = f'#{newColorHex}'
    )

    return newColorHex

def change_slider_values(hex_value, red_value, green_value, blue_value):
    red_change = int(hex_value[:2], 16)
    green_change = int(hex_value[2:4], 16)
    blue_change = int(hex_value[4:], 16)

    red_value.set(red_change)
    green_value.set(green_change)
    blue_value.set(blue_change)


def main():
    dont_execute_me()

if __name__ == '__main__':
    main()