class ExportWindow(ctk.CTkToplevel):
    def __init__(self, primary_color, secondary_color, tertiary_color, emphasis_color, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.tertiary_color = tertiary_color
        self.emphasis_color = emphasis_color
        
        export_toplevel_width: int = 375
        export_toplevel_height: int = 225
        
        self.title('Export Code')
        self.geometry(f'{export_toplevel_width}x{export_toplevel_height}')
        self.resizable(False, False)
        self.grab_set()


        def disable_export_ncl_button(value):
            # use 'or' to apply this conditional to multiple supported versions
            if game_title_option.get() != 'LBP2 (BCUS98245 | 1.33)': 
                new_export_ncl_button.configure(state = 'disabled')
            else:
                new_export_ncl_button.configure(state = 'normal')


        export_option_width: int = 190
        
        code_caption_label = ctk.CTkLabel(self, text = 'NetCheat Code Name:')
        code_caption_entry = ctk.CTkEntry(self, width = export_option_width)
        code_caption_note = ctk.CTkLabel(self, text = 'It\'s optional, but it helps.')
        

        game_title = ctk.CTkLabel(self, text = 'Game Title:')

        game_title_default_option = ctk.StringVar(value = 'LBP2 (BCUS98245 | 1.33)')
        game_title_option = ctk.CTkOptionMenu(self)
        game_title_option.configure(
            width = export_option_width,
            values = ['LBP1 (BCUS98148 | 1.30)', 'LBP2 (BCUS98245 | 1.33)', 'LBP3 (BCUS98362 | 1.26)'],
            variable = game_title_default_option,
            command = disable_export_ncl_button
            )

        game_title_note = ctk.CTkLabel(self, text = 'LBP1 doesn\'t use the Emphasis Color.')

        new_export_ncl_button = ctk.CTkButton(
            self, 
            text = 'Save NCL',
            width = 85,
            command = lambda: external_objects.new_export_ncl(
                code_caption_entry.get(),
                self.primary_color,
                self.secondary_color,
                self.tertiary_color,
                self.emphasis_color
                )
            )

        new_save_text_button = ctk.CTkButton(
            self, 
            text = 'Save Value List',
            width = 105,
            command = lambda: external_objects.export_value_list(
                game_title_option.get(),
                self.primary_color,
                self.secondary_color,
                self.tertiary_color,
                self.emphasis_color
                )
            )

        new_export_yaml_button = ctk.CTkButton(
            self, 
            text = 'Save YAML (Old)',
            width = 125,
            command = lambda: external_objects.new_export_yaml(
                code_caption_entry.get(),
                self.primary_color,
                self.secondary_color,
                self.tertiary_color,
                self.emphasis_color
                )
            )


        # Edit these values to change the Widgets' Position
        export_row_1: int = 17
        export_next_row: int = 70

        export_text_x_position: int = 22
        export_option_x_offset: int = 20
        export_note_y_position: int = 30

        export_code_buttons_x_offset: int = 20
        export_code_buttons_y_position: int = 45
        

        # Do NOT look at this mess full of Variables
        code_caption_label.place(
            anchor = 'nw', 
            x = export_text_x_position, 
            y = export_row_1
            )

        code_caption_entry.place(
            anchor = 'ne', 
            x = (export_toplevel_width - export_option_x_offset), 
            y = export_row_1
            )

        code_caption_note.place(
            anchor = 'ne', 
            x = (export_toplevel_width - export_option_x_offset), 
            y = (export_row_1 + export_note_y_position)
            )


        game_title.place(
            anchor = 'nw', 
            x = export_text_x_position, 
            y = (export_row_1 + export_next_row)
            )

        game_title_option.place(
            anchor = 'ne', 
            x = (export_toplevel_width - export_option_x_offset), 
            y = (export_row_1 + export_next_row)
            )
        
        game_title_note.place(
            anchor = 'ne', 
            x = (export_toplevel_width - export_option_x_offset), 
            y = (export_row_1 + export_next_row + export_note_y_position)
            )

        
        new_export_ncl_button.place(
            anchor = 'nw', 
            x =  export_code_buttons_x_offset, 
            y = (export_toplevel_height - export_code_buttons_y_position)
            )

        new_save_text_button.place(
            anchor = 'n', 
            x = 167, 
            y = (export_toplevel_height - export_code_buttons_y_position)
            )

        new_export_yaml_button.place(
            anchor = 'ne', 
            x = (export_toplevel_width - export_code_buttons_x_offset),
            y = (export_toplevel_height - export_code_buttons_y_position)
            )