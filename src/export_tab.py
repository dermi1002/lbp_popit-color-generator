from dontexecuteme import *

import external_objects

import customtkinter as ctk

class ExportTab(ctk.CTkFrame):
    def __init__(
        self, master,
        colorPrimary: str, colorSecondary: str, colorTertiary: str, colorEmphasis: str,
        *args, **kwargs
        ):

        super().__init__(
            master,
            *args, **kwargs
        )

        self.colorPrimary = colorPrimary
        self.colorSecondary = colorSecondary
        self.colorTertiary = colorTertiary
        self.colorEmphasis = colorEmphasis

        self.popitColorValues = [
            self.colorPrimary,
            self.colorSecondary,
            self.colorTertiary,
            self.colorEmphasis
        ]

        self.gameTitles: list = [
            'LBP1 (BCUS98148 | 1.30)',
            'LBP2 (BCUS98245 | 1.33)',
            'LBP3 (BCUS98362 | 1.26)'
        ]

        def disable_export_ncl_button(value):
            if game_title_option.get() != self.gameTitles[1]: 
                new_export_ncl_button.configure(state = 'disabled')
            else:
                new_export_ncl_button.configure(state = 'normal')
        
        exportOptionWidth: int = 190

        code_caption_label = ctk.CTkLabel(self, text = 'NetCheat Code Name:')
        code_caption_entry = ctk.CTkEntry(self, width = exportOptionWidth)
        code_caption_note = ctk.CTkLabel(self, text = 'It\'s optional, but it helps.')

        game_title = ctk.CTkLabel(self, text = 'Game Title:')

        game_title_default_option = ctk.StringVar(value = self.gameTitles[1])
        game_title_option = ctk.CTkOptionMenu(self)
        game_title_option.configure(
            width = exportOptionWidth,
            values = self.gameTitles,
            variable = game_title_default_option,
            command = lambda: disable_export_ncl_button()
        )

        game_title_note = ctk.CTkLabel(
            self,
            text = 'LBP1 doesn\'t use the Emphasis Color.'
        )

        export_button_frame = ctk.CTkFrame(self, fg_color = 'transparent')

        new_export_ncl_button = ctk.CTkButton(
            export_button_frame, 
            text = 'Save NCL',
            width = 85,
            command = lambda: external_objects.new_export_ncl(
                code_caption_entry.get(),
                *self.popitColorValues
            )
        )

        new_save_text_button = ctk.CTkButton(
            export_button_frame, 
            text = 'Save Value List',
            width = 105,
            command = lambda: external_objects.export_value_list(
                game_title_option.get(),
                *self.popitColorValues
            )
        )

        new_export_yaml_button = ctk.CTkButton(
            export_button_frame, 
            text = 'Save YAML (Old)',
            width = 125,
            command = lambda: external_objects.new_export_yaml(
                code_caption_entry.get(),
                *self.popitColorValues
            )
        )

        def place_elements():
            code_caption_label.grid(sticky = 'nw', row = 0, column = 0, padx = (0, 5))
            code_caption_entry.grid(sticky = 'ne', row = 0, column = 1)
            code_caption_note.grid(sticky = 'ne', row = 1, column = 1, pady = (0, 15))

            game_title.grid(sticky = 'nw', row = 2, column = 0)
            game_title_option.grid(sticky = 'ne', row = 2, column = 1)
            game_title_note.grid(sticky = 'ne', row = 3, column = 1)
        
            export_button_frame.grid(sticky = 's', row = 4, columnspan = 2, pady = (10, 0))

            new_export_ncl_button.grid(sticky = 'sw', row = 4, column = 0)
            new_save_text_button.grid(sticky = 's', row = 4, column = 1, padx = 10, ipadx = 10)
            new_export_yaml_button.grid(sticky = 'se', row = 4, column = 2)
        
        place_elements()

        self.place(x = 80, y = 10)

def main():
    dont_execute_me()

if __name__ == '__main__':
    main()