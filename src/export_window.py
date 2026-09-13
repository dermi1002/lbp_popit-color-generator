import customtkinter as ctk
import tkinter as tk
import external_objects

class ExportWindowIII(ctk.CTkToplevel):
    def __init__(self, primary_color, secondary_color, tertiary_color, emphasis_color, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.tertiary_color = tertiary_color
        self.emphasis_color = emphasis_color

        export_toplevel_width: int = 385
        export_toplevel_height: int = 355
        
        self.title('Export Code')
        self.geometry(f'{export_toplevel_width}x{export_toplevel_height}')
        self.resizable(False, False)
        self.grab_set()


        def change_file_directory_entry():
            directory_location = tk.filedialog.askdirectory(
                title = 'Browse Directory',
                initialdir = '../save'
            )

            if directory_location is None:
                return

            directory_location_entry: str = f'{directory_location}'
            
            code_filepath_entry.delete(0, ctk.END)
            code_filepath_entry.insert(0, directory_location_entry)

        def disable_filetype_ncl(value):
            if game_title_option.get() != 'LBP2 (BCUS98245 | 1.33)': 
                export_filetype_option.configure(values = ['Value List (.TXT)', 'YAML Dictionary (Old)'])
            else:
                export_filetype_option.configure(
                    values = ['NetCheat List (.NCL)', 'Value List (.TXT)', 'YAML Dictionary (Old)']
                )

            if export_filetype_option.get() == 'NetCheat List (.NCL)' and game_title_option.get() != 'LBP2 (BCUS98245 | 1.33)':
                export_filetype_option.set('Value List (.TXT)')

        test_grid = ctk.CTkFrame(self, fg_color = 'transparent')

        export_option_width: int = 190
        
        code_caption_label = ctk.CTkLabel(test_grid, text = 'Code Name:')
        code_caption_entry = ctk.CTkEntry(test_grid, width = export_option_width)
        code_caption_note = ctk.CTkLabel(test_grid, text = 'This is included in the exported NCL')

        code_filepath_label = ctk.CTkLabel(test_grid, text = 'File Path:')
        code_filepath_entry = ctk.CTkEntry(test_grid, width = export_option_width)
        code_filepath_browse = ctk.CTkButton(
            test_grid, 
            width = 70,
            text = 'Browse',
            command = change_file_directory_entry
        )


        game_title = ctk.CTkLabel(test_grid, text = 'Game Title:')

        game_title_default_option = ctk.StringVar(value = 'LBP2 (BCUS98245 | 1.33)')
        game_title_option = ctk.CTkOptionMenu(test_grid)
        game_title_option.configure(
            width = export_option_width,
            values = ['LBP1 (BCUS98148 | 1.30)', 'LBP2 (BCUS98245 | 1.33)', 'LBP3 (BCUS98362 | 1.26)'],
            variable = game_title_default_option,
            command = disable_filetype_ncl
        )

        game_title_note = ctk.CTkLabel(test_grid, text = 'LBP1 doesn\'t use the Emphasis Color.')


        export_filename_prefix = ctk.CTkCheckBox(
            test_grid,
            text = 'Prefix Game Info (Artemis)',
            checkbox_height = 18,
            checkbox_width = 18,
        )
        

        export_filetype = ctk.CTkLabel(test_grid, text = 'File Type:')

        export_filetype_default_option = ctk.StringVar(value = 'Value List (.TXT)')
        export_filetype_option = ctk.CTkOptionMenu(test_grid)
        export_filetype_option.configure(
            width = export_option_width,
            values = [
                'NetCheat List (.NCL)',
                'Value List (.TXT)',
                'YAML Dictionary (Old)'
            ],
            variable = export_filetype_default_option,
            command = None
        )

        export_filetype_note = ctk.CTkLabel(self, text = 'YAML Dictionary Support is\ndeprecated and will be\ndiscontinued in 1.0.0.')

        export_bottomrow_note = ctk.CTkLabel(
            self,
            justify = 'left',
            text = 'NOTE: This program doesn\'t\nsupport all LBP Titles yet.'
        )


        new_export_button = ctk.CTkButton(
            self, 
            text = 'Save File',
            width = 125,
            command = lambda: external_objects.export_any_format(
                export_filetype_option.get(), 
                code_filepath_entry.get(),
                game_title_option.get(),
                code_caption_entry.get(),
                export_filename_prefix.get(),
                self.primary_color,
                self.secondary_color,
                self.tertiary_color,
                self.emphasis_color,
            )
        )
        

        # Edit these values to change the Widgets' Position
        export_toplevel_x_center = int(export_toplevel_width / 2)
        export_object_center = int((export_toplevel_width / 2) - 18)
        
        export_y_offset: int = 17
        export_next_row: int = 70

        export_object_x_offset: int = 20
        export_note_y_position: int = 30

        export_object_right = int(export_toplevel_width - export_object_x_offset)

        export_code_buttons_bottom = int(export_toplevel_height - export_y_offset)
        

        # Do NOT look at this mess full of Variables
        code_caption_label.grid(sticky = 'sw', column = 0, row = 0, pady = export_y_offset)
        code_caption_entry.grid(sticky = 'sw', column = 1, row = 0, padx = 10, pady = export_y_offset)

        code_caption_note.place(anchor = 'n', x = export_object_center, y = 45)


        code_filepath_label.grid(sticky = 'nw', column = 0, row = 2, pady = export_y_offset)
        code_filepath_entry.grid(sticky = 'nw', column = 1, row = 2, padx = 10, pady = export_y_offset)
        code_filepath_browse.grid(sticky = 'nw', column = 2, row = 2, pady = export_y_offset)


        game_title.grid(sticky = 'nw', column = 0, row = 3)
        game_title_option.grid(sticky = 'nw', column = 1, row = 3, padx = 10)
        game_title_note.place(anchor = 'n', x = export_object_center, y = 153)


        export_filename_prefix.place(anchor = 'n', x = export_object_center, y = 184)
        
        
        export_filetype.grid(sticky = 'nw', column = 0, row = 6, pady = 65)
        export_filetype_option.grid(sticky = 'nw', column = 1, row = 6, padx = 10, pady = 65)
        export_filetype_note.place(anchor = 'n', x = export_toplevel_x_center, y = 248)

        
        export_bottomrow_note.place(anchor = 'sw', x = 22, y = export_code_buttons_bottom)
        new_export_button.place(anchor = 'se', x = export_object_right, y = export_code_buttons_bottom)

        test_grid.grid(padx = 22)

def main():
    external_objects.dont_execute_module()

if __name__ == '__main__':
    main()