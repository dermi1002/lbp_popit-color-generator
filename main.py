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

        self._set_appearance_mode('light')
        self.configure(fg_color = '#242424')
        self.mainloop()


if __name__ == '__main__':
    MainProgram() # it was about time i did this
