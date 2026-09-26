from dontexecuteme import dont_execute_me

import file_management
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

    sliderHexConvert = '%02X%02X%02X' % (red, green, blue)

    hexField.delete(0, ctk.END)
    hexField.insert(0, sliderHexConvert)

    colorSquare.configure(
        background = f'#{hexField._textvariable.get()}'
    )

def change_slider_values(valueHex, valueRed, valueGreen, valueBlue):
    changeRed = int(valueHex[:2], 16)
    changeGreen = int(valueHex[2:4], 16)
    changeBlue = int(valueHex[4:], 16)

    valueRed.set(changeRed)
    valueGreen.set(changeGreen)
    valueBlue.set(changeBlue)

def batch_change_color_elements(
    colorPrimary: str, colorSecondary: str, colorTertiary: str, colorEmphasis: str,
    tabColorPrimary, tabColorSecondary, tabColorTertiary, tabColorEmphasis,
    tabExport, codeCaption: str, whichEnd
    ):

    file_management.open_color_file(
        colorPrimary,
        tabColorPrimary.colorPreview,
        tabColorPrimary.hexColorField,
        tabColorPrimary.sliderRed.value_variable,
        tabColorPrimary.sliderGreen.value_variable,
        tabColorPrimary.sliderBlue.value_variable,
        whichEnd
    )

    file_management.open_color_file(
        colorSecondary,
        tabColorSecondary.colorPreview,
        tabColorSecondary.hexColorField,
        tabColorSecondary.sliderRed.value_variable,
        tabColorSecondary.sliderGreen.value_variable,
        tabColorSecondary.sliderBlue.value_variable,
        whichEnd
    )

    file_management.open_color_file(
        colorTertiary,
        tabColorTertiary.colorPreview,
        tabColorTertiary.hexColorField,
        tabColorTertiary.sliderRed.value_variable,
        tabColorTertiary.sliderGreen.value_variable,
        tabColorTertiary.sliderBlue.value_variable,
        whichEnd
    )

    file_management.open_color_file(
        colorEmphasis,
        tabColorEmphasis.colorPreview,
        tabColorEmphasis.hexColorField,
        tabColorEmphasis.sliderRed.value_variable,
        tabColorEmphasis.sliderGreen.value_variable,
        tabColorEmphasis.sliderBlue.value_variable,
        whichEnd
    )

    tabExport.codeCaptionField.delete(0, whichEnd)
    tabExport.codeCaptionField.insert(0, codeCaption)

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
        file_management.open_yaml_dictionary(
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