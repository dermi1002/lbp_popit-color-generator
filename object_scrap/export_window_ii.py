class ExportWindowII(ctk.CTkToplevel):
    def __init__(self, primary_color, secondary_color, tertiary_color, emphasis_color, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        export_toplevel_width: int = 385
        export_toplevel_height: int = 400
        
        self.title('Export Code')
        self.geometry(f'{export_toplevel_width}x{export_toplevel_height}')
        self.resizable(False, False)


        def disable_filetype_ncl(value):
            if game_title_option.get() != 'LBP2 (BCUS98245 | 1.33)': 
                export_filetype_option.configure(
                    values = ['Value List (.TXT)', 'YAML Dictionary (Old)']
                    )
            else:
                export_filetype_option.configure(
                    values = ['NetCheat List (.NCL)', 'Value List (.TXT)', 'YAML Dictionary (Old)']
                    )

            if export_filetype_option.get() == 'NetCheat List (.NCL)' and game_title_option.get() != 'LBP2 (BCUS98245 | 1.33)':
                export_filetype_option.set('Value List (.TXT)')


        export_option_width: int = 190
        
        code_caption_label = ctk.CTkLabel(self, text = 'Code Name:')
        code_caption_entry = ctk.CTkEntry(self, width = export_option_width)
        code_caption_note = ctk.CTkLabel(
            self, 
            justify = 'right',
            text = 'This will also be the Caption\nin the exported NCL'
            )

        code_filepath_label = ctk.CTkLabel(self, text = 'File Path:')
        code_filepath_entry = ctk.CTkEntry(self, width = export_option_width)
        code_filepath_browse = ctk.CTkButton(
            self, 
            width = 70,
            text = 'Browse',
            command = None
            )


        game_title = ctk.CTkLabel(self, text = 'Game Title:')

        game_title_default_option = ctk.StringVar(value = 'LBP2 (BCUS98245 | 1.33)')
        game_title_option = ctk.CTkOptionMenu(self)
        game_title_option.configure(
            width = export_option_width,
            values = ['LBP1 (BCUS98148 | 1.30)', 'LBP2 (BCUS98245 | 1.33)', 'LBP3 (BCUS98362 | 1.26)'],
            variable = game_title_default_option,
            command = disable_filetype_ncl
            )

        game_title_note = ctk.CTkLabel(
            self, 
            justify = 'right',
            text = 'LBP1 doesn\'t use the\nEmphasis Color.'
            )


        export_filename_prefix = ctk.CTkCheckBox(
            self,
            text = 'Prefix Game Info (Artemis)',
            checkbox_height = 18,
            checkbox_width = 18,
            command = None
            )
        

        export_filetype = ctk.CTkLabel(self, text = 'File Type:')

        export_filetype_default_option = ctk.StringVar(value = 'Value List (.TXT)')
        export_filetype_option = ctk.CTkOptionMenu(self)
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

        export_filetype_note = ctk.CTkLabel(
            self, 
            justify = 'right',
            text = 'YAML Dictionary Support is\ndeprecated and will be\ndiscontinued in 1.0.0.'
            )

        export_bottomrow_note = ctk.CTkLabel(
            self,
            justify = 'left',
            text = 'NOTE: This program doesn\'t\nsupport all LBP Titles yet.'
            )


        new_export_button = ctk.CTkButton(
            self, 
            text = 'Save File',
            width = 125,
            command = None
            )


        # Edit these values to change the Widgets' Position
        export_y_offset: int = 17
        export_next_row: int = 70

        # def export_next_row(value): 
        #     int(export_y_offset + (70 * value))

        export_row_2 = int(export_y_offset + export_next_row + 12)
        export_row_3 = int(export_y_offset + (export_next_row * 2))
        export_row_4 = int(export_y_offset + (export_next_row * 3))
        export_row_5 = int(export_y_offset + (export_next_row * 3) + 40)

        export_text_x_position: int = 22
        export_object_x_offset: int = 20
        export_note_y_position: int = 30

        export_object_right = int(export_toplevel_width - export_object_x_offset)

        export_code_buttons_bottom = int(export_toplevel_height - export_y_offset)
        

        # Do NOT look at this mess full of Variables
        code_caption_label.place(anchor = 'nw', x = export_text_x_position, y = export_y_offset)

        code_caption_entry.place(anchor = 'ne', x = export_object_right, y = export_y_offset)

        code_caption_note.place(
            anchor = 'ne', 
            x = export_object_right, 
            y = (export_y_offset + export_note_y_position)
            )


        code_filepath_label.place(anchor = 'nw', x = export_text_x_position, y = export_row_2)

        code_filepath_entry.place(anchor = 'ne', x = (export_object_right - 85), y = export_row_2)

        code_filepath_browse.place(anchor = 'ne', x = export_object_right, y = export_row_2)


        game_title.place(anchor = 'nw', x = export_text_x_position, y = export_row_3)

        game_title_option.place(anchor = 'ne', x = export_object_right, y = export_row_3)
        
        game_title_note.place(
            anchor = 'ne', 
            x = export_object_right, 
            y = (export_row_3 + export_note_y_position)
            )


        export_filename_prefix.place(anchor = 'nw', x = export_text_x_position, y = export_row_4)
        
        
        export_filetype.place(anchor = 'nw', x = export_text_x_position, y = export_row_5)

        export_filetype_option.place(anchor = 'ne', x = export_object_right, y = export_row_5)
        
        export_filetype_note.place(
            anchor = 'ne', 
            x = export_object_right, 
            y = (export_row_5 + export_note_y_position)
            )

        
        export_bottomrow_note.place(anchor = 'sw', x = export_text_x_position, y = export_code_buttons_bottom)
        
        new_export_button.place(anchor = 'se', x = export_object_right, y = export_code_buttons_bottom)
