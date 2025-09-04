import external_objects
import tkinter as tk # yeah, i know, but hear me out
from tkinter import messagebox
import customtkinter as ctk
import pyperclip
import yaml


class RGBSlider(ctk.CTkSlider):
    def __init__(self, master, slider_y_position, *args, **kwargs):
        super().__init__(master, slider_y_position, *args, **kwargs)

        slider_max_value: int = 255
        slider_value_range: int = 256
                
        slider_x_position: int = 260
        slider_y_position: int = slider_y_position

        self.configure(
            from_ = 0, to = slider_max_value, 
            width = slider_value_range, 
            number_of_steps = slider_value_range
            )

        self.set(0)
        self.place(x = slider_x_position, y = slider_y_position)

class RGBLetter(ctk.CTkLabel):
    def __init__(self, master, rgb_letter_selection, rgb_letter_y_position, *args):
        super().__init__(master, rgb_letter_selection, rgb_letter_y_position, *args)

        rgb_letter_x_position: int = 225
        rgb_letter_y_position: int = rgb_letter_y_position

        rgb_letter_text = ['R', 'G', 'B', 'H', 'S', 'V']
        rgb_letter_selection: int = rgb_letter_text[rgb_letter_selection]

        self.configure(text = rgb_letter_selection)

        self.place(x = rgb_letter_x_position, y = rgb_letter_y_position)

class ColorTab(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        def change_color_sliders(value):
            self.Red = int(self.red_slider.get())
            self.Green = int(self.green_slider.get())
            self.Blue = int(self.blue_slider.get())

            self.color_print_hex = '%02X%02X%02X' % (self.Red, self.Green, self.Blue)

            self.color_hex_entry.delete(0, ctk.END)
            self.color_hex_entry.insert(0, self.color_print_hex)

            self.color_preview.configure(background = f'#{self.color_hex_entry.get()}')

        def change_color_hex(value):
            self.hex_Red = self.color_hex_entry.get()[:2]
            self.hex_Green = self.color_hex_entry.get()[2:4]
            self.hex_Blue = self.color_hex_entry.get()[4:]

            self.hex_Red_int = int(self.hex_Red, 16)
            self.hex_Green_int = int(self.hex_Green, 16)
            self.hex_Blue_int = int(self.hex_Blue, 16)

            self.red_slider.set(self.hex_Red_int)
            self.green_slider.set(self.hex_Green_int)
            self.blue_slider.set(self.hex_Blue_int)

            self.color_preview.configure(background = f'#{self.color_hex_entry.get()}')


        def copy_color_hex_entry():
            pyperclip.copy(self.color_hex_entry.get())

        color_beginning_value: str = '000000'

        self.color_preview = tk.Frame(
            master, 
            background = f'#{color_beginning_value}', 
            width = 200, height = 200
            )

        self.color_preview.place(y = 4)

        
        self.letter_r = RGBLetter(master, 0, 17)
        self.red_slider = RGBSlider(master, 16, command = change_color_sliders)
                
        self.letter_g = RGBLetter(master, 1, 50)
        self.green_slider = RGBSlider(master, 66, command = change_color_sliders)

        self.letter_b = RGBLetter(master, 2, 82)
        self.blue_slider = RGBSlider(master, 116, command = change_color_sliders)


        hex_related_x_position: int = 225
        hex_related_y_position: int = 170

        self.color_hex_label = ctk.CTkLabel(master, text = 'HEX Color:')
        
        # Maybe I should turn this whole Hex entry thing into a class...
        def uppercaseletters(*args):
            self.hex_entry_text.set(self.hex_entry_text.get().upper())

        def hex_certain_characters(event):
            if event.char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f'):
                return True
            elif event.keysym not in ('Alt_r', 'Alt_L', 'F4', 'BackSpace', 'Return', 'Left', 'Right'):
                return 'break'
            else:
                return False

        def testlimit(P):
            try:
                self.hex_entry_text.trace_add('write', uppercaseletters)
            except AttributeError:
                # if you somehow got to open this gui program in python 3.6.0 or lower
                self.hex_entry_text.trace_add('w', uppercaseletters)

            if len(P) <= 6:
                return True
            else:
                self.bell()
                return False
        
        vcmd = (self.register(testlimit), '%P')

        self.hex_entry_text = tk.StringVar(master)
        self.color_hex_entry = ctk.CTkEntry(master, textvariable = self.hex_entry_text, validate = 'key', validatecommand = vcmd)
        
        self.color_hex_copy_button = ctk.CTkButton(
            master, 
            text = 'Copy', 
            width = 50, 
            command = copy_color_hex_entry
            )
        
            
        self.color_hex_label.place(x = hex_related_x_position, y = hex_related_y_position)
        
        self.color_hex_copy_button.place(x = 450, y = hex_related_y_position)

        self.color_hex_entry.place(x = 297, y = hex_related_y_position)
        self.color_hex_entry.insert(ctk.END, color_beginning_value)
        self.color_hex_entry.bind('<Return>', change_color_hex)
        self.color_hex_entry.bind('<KeyPress>', hex_certain_characters)


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
                initialdir = './save'
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


class ColorTabList(ctk.CTkTabview):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.add('Primary')
        self.add('Secondary')
        self.add('Tertiary')
        self.add('Emphasis')
        self.add('Export')

        self.set('Primary')
 
        self.primary_colortab = ColorTab(self.tab('Primary'))
        self.secondary_colortab = ColorTab(self.tab('Secondary'))
        self.tertiary_colortab = ColorTab(self.tab('Tertiary'))
        self.emphasis_colortab = ColorTab(self.tab('Emphasis'))


        # Export Tab UI
        export_tab = ctk.CTkFrame(self.tab('Export'))
        
        def disable_export_ncl_button(value):
            if game_title_option.get() != 'LBP2 (BCUS98245 | 1.33)': 
                new_export_ncl_button.configure(state = 'disabled')
            else:
                new_export_ncl_button.configure(state = 'normal')


        export_option_width: int = 190
        
        code_caption_label = ctk.CTkLabel(export_tab, text = 'NetCheat Code Name:')
        code_caption_entry = ctk.CTkEntry(export_tab, width = export_option_width)
        code_caption_note = ctk.CTkLabel(export_tab, text = 'It\'s optional, but it helps.')
        

        game_title = ctk.CTkLabel(export_tab, text = 'Game Title:')

        game_title_default_option = ctk.StringVar(value = 'LBP2 (BCUS98245 | 1.33)')
        game_title_option = ctk.CTkOptionMenu(export_tab)
        game_title_option.configure(
            width = export_option_width,
            values = ['LBP1 (BCUS98148 | 1.30)', 'LBP2 (BCUS98245 | 1.33)', 'LBP3 (BCUS98362 | 1.26)'],
            variable = game_title_default_option,
            command = disable_export_ncl_button
            )

        game_title_note = ctk.CTkLabel(export_tab, text = 'LBP1 doesn\'t use the Emphasis Color.')

        export_button_frame = ctk.CTkFrame(export_tab, fg_color = 'transparent')

        new_export_ncl_button = ctk.CTkButton(
            export_button_frame, 
            text = 'Save NCL',
            width = 85,
            command = lambda: external_objects.new_export_ncl(
                code_caption_entry.get(),
                self.primary_colortab.color_preview.cget('background')[1:],
                self.secondary_colortab.color_preview.cget('background')[1:],
                self.tertiary_colortab.color_preview.cget('background')[1:],
                self.emphasis_colortab.color_preview.cget('background')[1:]
                )
            )

        new_save_text_button = ctk.CTkButton(
            export_button_frame, 
            text = 'Save Value List',
            width = 105,
            command = lambda: external_objects.export_value_list(
                game_title_option.get(),
                self.primary_colortab.color_preview.cget('background')[1:],
                self.secondary_colortab.color_preview.cget('background')[1:],
                self.tertiary_colortab.color_preview.cget('background')[1:],
                self.emphasis_colortab.color_preview.cget('background')[1:]
                )
            )

        new_export_yaml_button = ctk.CTkButton(
            export_button_frame, 
            text = 'Save YAML (Old)',
            width = 125,
            command = lambda: external_objects.new_export_yaml(
                code_caption_entry.get(),
                self.primary_colortab.color_preview.cget('background')[1:],
                self.secondary_colortab.color_preview.cget('background')[1:],
                self.tertiary_colortab.color_preview.cget('background')[1:],
                self.emphasis_colortab.color_preview.cget('background')[1:]
                )
            )

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

        export_tab.place(x = 80, y = 10)


        self.test_export_window_iii = None

        def show_export_window_iii():
            if self.test_export_window_iii is None or not self.test_export_window_iii.winfo_exists():
                self.test_export_window_iii = ExportWindowIII(
                    self.primary_colortab.color_preview.cget('background')[1:],
                    self.secondary_colortab.color_preview.cget('background')[1:],
                    self.tertiary_colortab.color_preview.cget('background')[1:],
                    self.emphasis_colortab.color_preview.cget('background')[1:]
                    )
                self.test_export_window_iii.focus()
            else:
                self.test_export_window_iii.focus()


        # Toolbar
        self.test_toolbar = external_objects.Toolbar(master)

        master.configure(menu = self.test_toolbar)


        self.test_toolbar.file_option.add_command(
            label = "Save Code",
            command = show_export_window_iii
            )

        self.test_toolbar.file_option.add_command(
            state = tk.DISABLED,
            label = f'can\'t open files for now',
            command = None
            )

        self.test_toolbar.file_option.add_command(
            state = tk.DISABLED,
            label = '[Test] Open Value List',
            command = lambda: external_objects.read_text_list()
            )

        self.place_configure(width = 530, height = 254)
        self.place(x = 5)

    
class MainProgram(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("LBP2 Color Generator")
        self.geometry('540x260')
        self.resizable(False, False)

        # Program
        ColorTabList(self)

        self.protocol('WM_DELETE_WINDOW', lambda: external_objects.closing_prompt(self))
        self.mainloop()


if __name__ == '__main__':
    MainProgram() # it was about time i did this
