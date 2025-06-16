import file_management
import tkinter as tk # yeah, i know, but hear me out
import customtkinter as ctk
import pyperclip
import yaml


class Toolbar(tk.Menu):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # File
        self.file_option = tk.Menu(self, tearoff = 0)

        self.add_cascade(label = 'File', menu = self.file_option)

        # Help
        self.help_option = tk.Menu(self, tearoff = 0)

        self.add_cascade(label = 'Help', menu = self.help_option)

        
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

        def change_color(value):
            self.Red = int(self.red_slider.get())
            self.Green = int(self.green_slider.get())
            self.Blue = int(self.blue_slider.get())

            self.color_print_hex = '%02X%02X%02X' % (self.Red, self.Green, self.Blue)

            self.color_preview.configure(background = f'#{self.color_print_hex}')

            self.color_hex_entry.delete(0, ctk.END)
            self.color_hex_entry.insert(0, self.color_print_hex)

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
        self.red_slider = RGBSlider(master, 16, command = change_color)
                
        self.letter_g = RGBLetter(master, 1, 50)
        self.green_slider = RGBSlider(master, 66, command = change_color)

        self.letter_b = RGBLetter(master, 2, 82)
        self.blue_slider = RGBSlider(master, 116, command = change_color)


        hex_related_x_position: int = 225
        hex_related_y_position: int = 170

        self.color_hex_label = ctk.CTkLabel(master, text = 'HEX Color:')
        
        
        self.color_hex_entry = ctk.CTkEntry(master)
        
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


class ExportWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        export_toplevel_width: int = 350
        export_toplevel_height: int = 225
        
        self.title('Export Code')
        self.geometry(f'{export_toplevel_width}x{export_toplevel_height}')
        self.resizable(False, False)


        def disable_export_ncl_button(value):
            # use 'or' to apply this conditional to multiple supported versions
            if game_title_option.get() != 'LBP2': 
                new_export_ncl_button.configure(state = 'disabled')
            else:
                new_export_ncl_button.configure(state = 'normal')
        

        code_caption_label = ctk.CTkLabel(self, text = 'Caption for NCL:')
        code_caption_entry = ctk.CTkEntry(self, width = 190)
        code_caption_note = ctk.CTkLabel(self, text = 'It\'s optional, but it helps.')
        

        game_title = ctk.CTkLabel(self, text = 'Game Title:')

        game_title_default_option = ctk.StringVar(value = 'LBP2')
        game_title_option = ctk.CTkOptionMenu(self)
        game_title_option.configure(
            values = [
                    'LBP1',
                    'LBP2',
                    'LBP3'
                ],
            variable = game_title_default_option,
            command = disable_export_ncl_button
            )

        game_title_note = ctk.CTkLabel(self, text = 'LBP1 doesn\'t use the Emphasis Color.')

        new_export_yaml_button = ctk.CTkButton(
            self, 
            text = 'Export YAML',
            command = None
            )

        new_export_ncl_button = ctk.CTkButton(
            self, 
            text = 'Export NCL',
            command = None
            )


        # Edit these values to change the Widgets' Position
        export_row_1: int = 17
        export_row_2: int = 70

        export_text_x_position: int = 22
        export_option_x_offset: int = 20
        export_note_y_position: int = 30

        export_code_buttons_x_offset: int = 90
        export_code_buttons_y_position: int = 45
        

        # Do NOT look at the mess overloaded with Variables
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
            anchor = 'n', 
            x = 233, 
            y = (export_row_1 + export_note_y_position)
            )


        game_title.place(
            anchor = 'nw', 
            x = export_text_x_position, 
            y = (export_row_1 + export_row_2)
            )

        game_title_option.place(
            anchor = 'ne', 
            x = (export_toplevel_width - export_option_x_offset), 
            y = (export_row_1 + export_row_2)
            )
        
        game_title_note.place(
            anchor = 'n', 
            x = 233, 
            y = (export_row_1 + export_row_2 + export_note_y_position)
            )


        new_export_yaml_button.place(
            anchor = 'n', 
            x = export_code_buttons_x_offset, 
            y = (export_toplevel_height - export_code_buttons_y_position)
            )
        
        new_export_ncl_button.place(
            anchor = 'n', 
            x = (export_toplevel_width - export_code_buttons_x_offset), 
            y = (export_toplevel_height - export_code_buttons_y_position)
            )


class ColorTabList(ctk.CTkTabview):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.test_toolbar = Toolbar(master)

        master.configure(menu = self.test_toolbar)

        self.test_toolbar.file_option.add_command(
            label = 'Save YAML', 
            command = lambda: file_management.export_yaml(
                code_caption.get(),
                self.primary_colortab.color_preview.cget('background')[1:],
                self.secondary_colortab.color_preview.cget('background')[1:],
                self.tertiary_colortab.color_preview.cget('background')[1:],
                self.emphasis_colortab.color_preview.cget('background')[1:]
                )
            )

        self.test_toolbar.file_option.add_command(
            label = 'Save NCL', 
            command = lambda: file_management.export_ncl(
                code_caption.get(),
                self.primary_colortab.color_preview.cget('background')[1:],
                self.secondary_colortab.color_preview.cget('background')[1:],
                self.tertiary_colortab.color_preview.cget('background')[1:],
                self.emphasis_colortab.color_preview.cget('background')[1:]
                )
            )

        self.test_toolbar.file_option.add_command(
            state = tk.DISABLED,
            label = f'can\'t open files for now',
            command = None
            )


        # Help Commands
        self.test_toolbar.help_option.add_command(
            label = 'About',
            command = None
            )


        self.add('Primary')
        self.add('Secondary')
        self.add('Tertiary')
        self.add('Emphasis')
        self.add('Export')
        self.add('Test')

        self.set('Primary')
 
        self.primary_colortab = ColorTab(self.tab('Primary'))
        self.secondary_colortab = ColorTab(self.tab('Secondary'))
        self.tertiary_colortab = ColorTab(self.tab('Tertiary'))
        self.emphasis_colortab = ColorTab(self.tab('Emphasis'))

        # Export Tab Functions
        # def import_yaml():
        #     yaml_load_location = tk.filedialog.askopenfilename(
        #         title = "Import YAML Config", 
        #         initialdir = "./save"
        #         )
        # 
        #     if yaml_load_location is None:
        #         return
        # 
        #     with open("color_path.yaml", "w") as color_path_file:
        #         color_path_file.truncate(0)
        #         color_path_file.write(
        #             'color-path:\n' + 
        #             f'  set-yaml: \"{str(yaml_load_location)}\"' # Path to recently saved Color YAML file
        #             )


        # Export Tab UI
        export_tab = ctk.CTkFrame(self.tab('Export'))
        export_text_preview = ctk.CTkLabel(
            export_tab, 
            text = f'If you are finished with your Popit color theme,\ngive it a Code Name and export a cheat file!', 
            width = 525
            )

        code_caption = ctk.CTkEntry(export_tab, placeholder_text = 'Code Name')

        save_yaml_button = ctk.CTkButton(
            export_tab, 
            text = 'Save YAML', 
            command = lambda: file_management.export_yaml(
                code_caption.get(),
                self.primary_colortab.color_preview.cget('background')[1:],
                self.secondary_colortab.color_preview.cget('background')[1:],
                self.tertiary_colortab.color_preview.cget('background')[1:],
                self.emphasis_colortab.color_preview.cget('background')[1:]
                )
            )

        save_ncl_button = ctk.CTkButton(
            export_tab, 
            text = 'Save NCL', 
            command = lambda: file_management.export_ncl(
                code_caption.get(),
                self.primary_colortab.color_preview.cget('background')[1:],
                self.secondary_colortab.color_preview.cget('background')[1:],
                self.tertiary_colortab.color_preview.cget('background')[1:],
                self.emphasis_colortab.color_preview.cget('background')[1:]
                )
            )

        # export_ncl_button = ctk.CTkButton(
            # export_tab, 
            # text = "import yaml", 
            # command = lambda: convert_yaml_to_ncl()
            # )

        export_text_preview.grid(row = 0, pady = 5)
        code_caption.grid(row = 1, pady = 10)
        save_yaml_button.grid(row = 2, pady = 10)
        save_ncl_button.grid(row = 3, pady = 10)

        # export_ncl_button.grid(row = 3, pady = 10)

        
        export_tab.grid(row = 0, column = 0)


        new_export_ui = ctk.CTkFrame(self.tab('Test'), width = 250, height = 150)


        def show_export_toplevel():
            test_export_window = ExportWindow(self)


        show_export_toplevel_button = ctk.CTkButton(new_export_ui, text = 'Show Toplevel', command = show_export_toplevel)
        
        show_export_toplevel_button.place(anchor = 'center', x = 125, y = 75)


        new_export_ui.configure(fg_color = 'red')
        new_export_ui.place(x = 125, y = 20)
        
        
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

        self.mainloop()


if __name__ == '__main__':
    MainProgram() # it was about time i did this
