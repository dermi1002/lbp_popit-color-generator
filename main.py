import customtkinter as ctk
import pyperclip
import yaml


class ColorTabList(ctk.CTkTabview):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.place_configure(width = 530, height = 254)

        self.add('Primary')
        self.add('Secondary')
        self.add('Tertiary')
        self.add('Emphasis')
        self.add('Export')

        self.set('Primary')
 
        # The Meat And Potatoes of the Program
        class ColorTab(ctk.CTkFrame):
            def __init__(self, master, *args, **kwargs):
                super().__init__(master, *args, **kwargs)
                
                def change_color(value):
                    self.Red = int(self.red_slider.get())
                    self.Green = int(self.green_slider.get())
                    self.Blue = int(self.blue_slider.get())

                    # color slider debugging
                    # print(f'Current Color: {self.Red}, {self.Green}, {self.Blue}')

                    self.color_print_hex = '%02X%02X%02X' % (self.Red, self.Green, self.Blue)

                    self.color_preview.configure(bg_color = f'#{self.color_print_hex}')

                    self.color_hex_entry.delete(0, ctk.END)
                    self.color_hex_entry.insert(0, self.color_print_hex)

                def copy_color_hex_entry():
                    pyperclip.copy(self.color_hex_entry.get())

                color_beginning_value: str = '000000'

                self.color_preview = ctk.CTkLabel(
                    master, 
                    text = '', 
                    bg_color = f'#{color_beginning_value}', 
                    width = 200, height = 200
                    )

                self.color_preview.place(y = 4)

                slider_max_value: int = 255
                slider_value_range: int = 256
                slider_x_position: int = 260


                class RGBSlider(ctk.CTkSlider):
                    def __init__(self, master, slider_y_position, *args, **kwargs):
                        super().__init__(master, slider_y_position, *args, **kwargs)

                        slider_x_position: int = 260
                        slider_y_position: int = slider_y_position
                        
                        self.configure(
                            from_ = 0, to = slider_max_value, 
                            width = slider_value_range, 
                            command = change_color, 
                            number_of_steps = slider_value_range
                            )

                        self.set(0)
                        self.place(x = slider_x_position, y = slider_y_position)
                

                rgb_letter_x_position: int = 225
                

                class RGBLetter(ctk.CTkLabel):
                    def __init__(self, master, rgb_letter_selection, rgb_letter_y_position, *args, **kwargs):
                        super().__init__(master, rgb_letter_selection, rgb_letter_y_position, *args, **kwargs)

                        rgb_letter_y_position: int = rgb_letter_y_position

                        rgb_letter_text = ['R', 'G', 'B', 'H', 'S', 'V']
                        rgb_letter_selection: int = rgb_letter_text[rgb_letter_selection]

                        self.configure(text = rgb_letter_selection)

                        self.place(x = rgb_letter_x_position, y = rgb_letter_y_position)


                hex_related_y_position: int = 170
                
                # i made the class for the rgb letters just to get the question off my mind
                self.letter_r = RGBLetter(master, 0, 17)
                self.red_slider = RGBSlider(master, 16)
                
                self.letter_g = RGBLetter(master, 1, 50)
                self.green_slider = RGBSlider(master, 66)

                self.letter_b = RGBLetter(master, 2, 82)
                self.blue_slider = RGBSlider(master, 116)


                self.color_hex_label = ctk.CTkLabel(master, text = 'HEX Color:').place(x = rgb_letter_x_position, y = hex_related_y_position)
                self.color_hex_entry = ctk.CTkEntry(master)
                self.color_hex_copy_button = ctk.CTkButton(master, text = 'Copy', width = 50, command = copy_color_hex_entry).place(x = 450, y = hex_related_y_position)

                self.color_hex_entry.place(x = 297, y = hex_related_y_position)
                self.color_hex_entry.insert(ctk.END, color_beginning_value)

        self.primary_colortab = ColorTab(self.tab('Primary'))
        self.secondary_colortab = ColorTab(self.tab('Secondary'))
        self.tertiary_colortab = ColorTab(self.tab('Tertiary'))
        self.emphasis_colortab = ColorTab(self.tab('Emphasis'))

        # Export Tab Functions
        def export_yaml():
            config_export = ctk.filedialog.asksaveasfile(
                title = "Export YAML Config", 
                initialdir = "./save", 
                filetypes = (("YAML Configuration", "*.yaml"), ("All Files", "*.*")), 
                defaultextension = '.yaml'
                )
                
            if config_export is None:
                return

            color_config = str(
                'color-code:\n' +
                f'  caption: \"{code_name.get()}\"\n' +

                f'  primcolor: \"{self.primary_colortab.color_hex_entry.get()}\"\n' +
                f'  primopacity: \"FF\"\n' +

                f'  seccolor: \"{self.secondary_colortab.color_hex_entry.get()}\"\n'
                f'  secopacity: \"FF\"\n' +

                f'  tertcolor: \"{self.tertiary_colortab.color_hex_entry.get()}\"\n' +
                f'  tertopacity: \"FF\"\n' +

                f'  emphcolor: \"{self.emphasis_colortab.color_hex_entry.get()}\"\n' +
                f'  emphopacity: \"FF\"\n' +

                f'  save: \"export\\\\\"'
                )
            config_export.write(color_config)
            config_export.close()


        def color_convert():
            yaml_set = ctk.filedialog.askopenfilename(title = "Import YAML Config", initialdir = "./save")
            if yaml_set is None:
                return
            with open("color_path.yaml", "w") as color_path_file:
                color_path_file.truncate(0)
                color_path_file.write(
                    'color-path:\n' + 
                    f'  set-yaml: \"{str(yaml_set)}\"' # Path to recently saved Color YAML file
                )

        def export_ncl():
            color_convert()
            
            with open("color_path.yaml", 'r') as path_set:
                current_yaml = yaml.safe_load(path_set)

            current_color = current_yaml['color-path']

            with open(current_color['set-yaml'], 'r') as file:
                config = yaml.safe_load(file)

            yaml_config = config['color-code']


            player_color_pointer: str = "00DC5E8C"

            player_color_pointer_value = ["00000000", "00000004", "00000008", "0000000C"]

            netcheat_zeroes: str = "0 00000000 "

            ncl_save = ctk.filedialog.asksaveasfile(
                title = "Export NCL Code", 
                initialdir = "export", 
                filetypes = [("NetCheat List File", "*.ncl"), ("All Files", "*.*")], 
                defaultextension = ".ncl"
                )

            if ncl_save is None:
                return

            color_code = str(
                yaml_config['caption'] + '\n0\n' + 

                # i couldn't put yaml variables inside formatted strings so
                f'6 {player_color_pointer} {player_color_pointer_value[0]}\n' + 
                netcheat_zeroes + yaml_config['primopacity'] + yaml_config['primcolor'] + '\n' + 

                f'6 {player_color_pointer} {player_color_pointer_value[1]}\n' + 
                netcheat_zeroes + yaml_config['secopacity'] + yaml_config['seccolor']+ '\n' + 

                f'6 {player_color_pointer} {player_color_pointer_value[2]}\n' + 
                netcheat_zeroes + yaml_config['tertopacity'] + yaml_config['tertcolor'] + '\n' + 
                
                f'6 {player_color_pointer} {player_color_pointer_value[3]}\n' + 
                netcheat_zeroes + yaml_config['emphopacity'] + yaml_config['emphcolor'] + '\n#\n'
                )
            ncl_save.write(color_code)
            ncl_save.close()

        # Export Tab UI
        export_tab = ctk.CTkFrame(self.tab('Export'))
        export_tab.grid(row = 0, column = 0)

        export_text_preview = ctk.CTkLabel(
            export_tab, 
            text = f'If you are finished with your Popit color theme,\ngive it a Code Name and export a cheat file!', 
            width = 525
            )

        export_text_preview.grid(row = 0, pady = 5)

        code_name = ctk.CTkEntry(export_tab, placeholder_text = 'Code Name')

        save_yaml_button = ctk.CTkButton(export_tab, text = 'Save YAML Config', command = export_yaml)

        export_ncl_button = ctk.CTkButton(export_tab, text = "Convert to NCL", command = export_ncl)

        code_name.grid(row = 1, pady = 10)
        save_yaml_button.grid(row = 2, pady = 10)
        export_ncl_button.grid(row = 3, pady = 10)

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


def main():
    MainProgram()

if __name__ == '__main__':
    main()
