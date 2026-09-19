from dontexecuteme import *

import external_objects

import customtkinter as ctk

class ExportTab(ctk.CTkFrame):
    def __init__(
        self, master,
        *args, **kwargs
        ):

        super().__init__(
            master,
            *args, **kwargs
        )

        self.gameTitles: list = [
            'LBP1 (BCUS98148 | 1.30)',
            'LBP2 (BCUS98245 | 1.33)',
            'LBP3 (BCUS98362 | 1.26)'
        ]

        def disable_export_ncl_button(value):
            if self.game_title_option.get() != str(self.gameTitles[1]): 
                self.new_export_ncl_button.configure(state = 'disabled')
            else:
                self.new_export_ncl_button.configure(state = 'normal')
        
        exportOptionWidth: int = 190

        code_caption_label = ctk.CTkLabel(self, text = 'NetCheat Code Name:')
        self.code_caption_entry = ctk.CTkEntry(self, width = exportOptionWidth)
        code_caption_note = ctk.CTkLabel(self, text = 'It\'s optional, but it helps.')

        game_title = ctk.CTkLabel(self, text = 'Game Title:')

        game_title_default_option = ctk.StringVar(value = self.gameTitles[1])
        self.game_title_option = ctk.CTkOptionMenu(self)
        self.game_title_option.configure(
            width = exportOptionWidth,
            values = self.gameTitles,
            variable = game_title_default_option,
            command = disable_export_ncl_button
        )

        game_title_note = ctk.CTkLabel(
            self, text = 'LBP1 doesn\'t use the Emphasis Color.'
        )

        export_button_frame = ctk.CTkFrame(self, fg_color = 'transparent')

        self.new_export_ncl_button = ctk.CTkButton(
            export_button_frame, 
            text = 'Save NCL',
            width = 85
        )

        self.new_save_text_button = ctk.CTkButton(
            export_button_frame, 
            text = 'Save Value List',
            width = 105
        )

        self.new_export_yaml_button = ctk.CTkButton(
            export_button_frame, 
            text = 'Save YAML (Old)',
            width = 125
        )

        def place_elements():
            code_caption_label.grid(sticky = 'nw', row = 0, column = 0, padx = (0, 5))
            self.code_caption_entry.grid(sticky = 'ne', row = 0, column = 1)
            code_caption_note.grid(sticky = 'ne', row = 1, column = 1, pady = (0, 15))

            game_title.grid(sticky = 'nw', row = 2, column = 0)
            self.game_title_option.grid(sticky = 'ne', row = 2, column = 1)
            game_title_note.grid(sticky = 'ne', row = 3, column = 1)
        
            export_button_frame.grid(sticky = 's', row = 4, columnspan = 2, pady = (10, 0))

            self.new_export_ncl_button.grid(sticky = 'sw', row = 4, column = 0)
            self.new_save_text_button.grid(sticky = 's', row = 4, column = 1, padx = 10, ipadx = 10)
            self.new_export_yaml_button.grid(sticky = 'se', row = 4, column = 2)
        
        place_elements()

        self.place(x = 80, y = 10)

def main():
    dont_execute_me()

if __name__ == '__main__':
    main()