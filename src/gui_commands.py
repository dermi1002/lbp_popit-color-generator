from dontexecuteme import dont_execute_me

import external_objects
import export_window

import customtkinter as ctk
from tkinter import messagebox
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

    colorSquare.configure(
        background = f'#{hexField._textvariable.get()}'
    )

def change_slider_values(hex_value, red_value, green_value, blue_value):
    red_change = int(hex_value[:2], 16)
    green_change = int(hex_value[2:4], 16)
    blue_change = int(hex_value[4:], 16)

    red_value.set(red_change)
    green_value.set(green_change)
    blue_value.set(blue_change)


def batch_change_color_elements(
    colorPrimary: str, colorSecondary: str, colorTertiary: str, colorEmphasis: str,
    tabColorPrimary, tabColorSecondary, tabColorTertiary, tabColorEmphasis,
    tabExport, codeCaption: str, whichEnd
    ):

    external_objects.open_color_file(
        colorPrimary,
        tabColorPrimary.colorPreview,
        tabColorPrimary.hexColorField,
        tabColorPrimary.red_slider.value_variable,
        tabColorPrimary.green_slider.value_variable,
        tabColorPrimary.blue_slider.value_variable,
        whichEnd
    )

    external_objects.open_color_file(
        colorSecondary,
        tabColorSecondary.colorPreview,
        tabColorSecondary.hexColorField,
        tabColorSecondary.red_slider.value_variable,
        tabColorSecondary.green_slider.value_variable,
        tabColorSecondary.blue_slider.value_variable,
        whichEnd
    )

    external_objects.open_color_file(
        colorTertiary,
        tabColorTertiary.colorPreview,
        tabColorTertiary.hexColorField,
        tabColorTertiary.red_slider.value_variable,
        tabColorTertiary.green_slider.value_variable,
        tabColorTertiary.blue_slider.value_variable,
        whichEnd
    )

    external_objects.open_color_file(
        colorEmphasis,
        tabColorEmphasis.colorPreview,
        tabColorEmphasis.hexColorField,
        tabColorEmphasis.red_slider.value_variable,
        tabColorEmphasis.green_slider.value_variable,
        tabColorEmphasis.blue_slider.value_variable,
        whichEnd
    )

    tabExport.code_caption_entry.delete(0, whichEnd)
    tabExport.code_caption_entry.insert(0, codeCaption)

def discard_changes_new_file(
    colorPrimary: str, colorSecondary: str, colorTertiary: str, colorEmphasis: str,
    tabColorPrimary, tabColorSecondary, tabColorTertiary, tabColorEmphasis,
    tabExport, codeCaption: str, whichEnd
    ):

    if messagebox.askyesno(
        "Discard Changes?",
        f"You are about to start a new file.\nDiscard changes to current session?"
    ):
        batch_change_color_elements(
            colorPrimary, colorSecondary, colorTertiary, colorEmphasis,
            tabColorPrimary, tabColorSecondary, tabColorTertiary, tabColorEmphasis,
            tabExport, codeCaption, whichEnd
        )

def discard_changes_yaml_dictionary(
    tabColorPrimary, tabColorSecondary, tabColorTertiary, tabColorEmphasis,
    tabExport, whichEnd
    ):

    if messagebox.askyesno(
        "Discard Changes?",
        f"You are about to open a YAML Dictionary.\nDiscard changes to current session?"
    ):
        external_objects.open_yaml_dictionary(
            tabColorPrimary, tabColorSecondary,
            tabColorTertiary, tabColorEmphasis,
            tabExport, whichEnd
        )


def show_export_window(
    exportWindowInstance,
    colorPrimary, colorSecondary, colorTertiary, colorEmphasis
    ):

    if exportWindowInstance is None or not exportWindowInstance.winfo_exists():
        exportWindowInstance = export_window.ExportWindowIII(
            colorPrimary, colorSecondary,
            colorTertiary, colorEmphasis
        )
        exportWindowInstance.focus()
    else:
        exportWindowInstance.focus()

def main():
    dont_execute_me()

if __name__ == '__main__':
    main()