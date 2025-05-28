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

        class ColorTab(ctk.CTkFrame):
            def __init__(self, master, *args, **kwargs):
                super().__init__(master, *args, **kwargs)
                
                def change_color(value):
                    self.Red = int(self.red_slider.get())
                    self.Green = int(self.green_slider.get())
                    self.Blue = int(self.blue_slider.get())

                    self._hexprint = '%02X%02X%02X' % (self.Red, self.Green, self.Blue)

                    self.color_preview.configure(bg_color = f'#{self._hexprint}')

                    self._hexentry.delete(0, ctk.END)
                    self._hexentry.insert(0, self._hexprint)

                def copy_hexentry():
                    pyperclip.copy(self._hexentry.get())

                color_beginning_value:str = '000000'

                self.color_preview = ctk.CTkLabel(
                    master, 
                    text = '', 
                    bg_color = f'#{color_beginning_value}', 
                    width = 200, 
                    height = 200
                    )

                self.color_preview.place(y = 4)

                # am i coupling code at this point
                class RGBSlider(ctk.CTkSlider): # Unused
                    def __init__(self, master, slider_y_position, *args, **kwargs):
                        super().__init__(master, slider_y_position, *args, **kwargs)

                        slider_x_position:int = 260
                        slider_y_position:int = slider_y_position
                        
                        self = ctk.CTkSlider(
                            master, 
                            from_ = 0, to = 255, 
                            width = 256, 
                            command = change_color
                            )

                        self.configure(number_of_steps = 256)
                        self.set(0)
                        self.place(x = slider_x_position, y = slider_y_position)

                slider_value_range:int = 256
                slider_x_position:int = 260    
                rgb_letter_x_position:int = 225
                hex_related_y_position:int = 170

                # i really wish i could get the slider class to work but i can't use the command therefrom
                self.letter_r = ctk.CTkLabel(master, text = 'R').place(x = rgb_letter_x_position, y = 10)
                self.red_slider = ctk.CTkSlider(master, from_ = 0, to = 255, width = 256, command = change_color)

                self.letter_g = ctk.CTkLabel(master, text = 'G').place(x = rgb_letter_x_position, y = 60)
                self.green_slider = ctk.CTkSlider(master, from_ = 0, to = 255, width = 256, command = change_color)

                self.letter_b = ctk.CTkLabel(master, text = 'B').place( x = rgb_letter_x_position, y = 110)
                self.blue_slider = ctk.CTkSlider(master, from_ = 0, to = 255, width = 256, command = change_color)


                self.red_slider.configure(number_of_steps = slider_value_range)
                self.red_slider.set(0)
                self.red_slider.place(x = slider_x_position, y = 16)

                self.green_slider.configure(number_of_steps = slider_value_range)
                self.green_slider.set(0)
                self.green_slider.place(x = slider_x_position, y = 66)

                self.blue_slider.configure(number_of_steps = slider_value_range)
                self.blue_slider.set(0)
                self.blue_slider.place(x = slider_x_position, y = 116)


                self._hexdisplay = ctk.CTkLabel(master, text = 'HEX Color:').place(x = rgb_letter_x_position, y = hex_related_y_position)
                self._hexentry = ctk.CTkEntry(master)
                self._hexcopy = ctk.CTkButton(master, text = 'Copy', width = 50, command = copy_hexentry).place(x = 450, y = hex_related_y_position)

                self._hexentry.place(x = 297, y = hex_related_y_position)
                self._hexentry.insert(ctk.END, color_beginning_value)

        self.primary_colortab = ColorTab(self.tab('Primary'))
        self.secondary_colortab = ColorTab(self.tab('Secondary'))
        self.tertiary_colortab = ColorTab(self.tab('Tertiary'))
        self.emphasis_colortab = ColorTab(self.tab('Emphasis'))


        # Export Tab
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

                f'  primcolor: \"{self.primary_colortab._hexentry.get()}\"\n' +
                f'  primopacity: \"FF\"\n' +

                f'  seccolor: \"{self.secondary_colortab._hexentry.get()}\"\n'
                f'  secopacity: \"FF\"\n' +

                f'  tertcolor: \"{self.tertiary_colortab._hexentry.get()}\"\n' +
                f'  tertopacity: \"FF\"\n' +

                f'  emphcolor: \"{self.emphasis_colortab._hexentry.get()}\"\n' +
                f'  emphopacity: \"FF\"\n' +

                f'  save: \"export\\\\\"'
                )
            config_export.write(color_config)
            config_export.close() # can i optimize this?


        def color_convert():
            yaml_set = ctk.filedialog.askopenfilename(title = "Import YAML Config", initialdir = "./save")
            if yaml_set is None:
                return
            with open("color_path.yaml", "w") as fo:
                fo.truncate(0)
                fo.write(
                    "color-path:\n" + 
                    "  set-yaml: " + "\"" + str(yaml_set) + "\"" # path to recently saved color yaml file
                )

        def export_ncl():
            color_convert()
            
            with open("color_path.yaml", 'r') as path_set:
                current_yaml = yaml.safe_load(path_set)

            current_color = current_yaml['color-path']

            with open(current_color['set-yaml'], 'r') as file:
                config = yaml.safe_load(file)

            db_config = config['color-code']


            player_id:str = "00DC5E8C"

            profile_id_1 = ["00000000", "00000004", "00000008", "0000000C"]

            netcheat_zeroes:str = "0 00000000 "

            ncl_save = ctk.filedialog.asksaveasfile(
                title = "Export NCL Code", 
                initialdir = "export", 
                filetypes = [("NetCheat List File", "*.ncl"), ("All Files", "*.*")], 
                defaultextension = ".ncl"
                )

            if ncl_save is None:
                return

            color_code = str(
                db_config['caption'] + '\n' + '0\n' + 

                f'6 {player_id} {profile_id_1[0]}\n' + 
                netcheat_zeroes + db_config['primopacity'] + db_config['primcolor'] + '\n' + 

                f'6 {player_id} {profile_id_1[1]}\n' + 
                netcheat_zeroes + db_config['secopacity'] + db_config['seccolor']+ '\n' + 

                f'6 {player_id} {profile_id_1[2]}\n' + 
                netcheat_zeroes + db_config['tertopacity'] + db_config['tertcolor'] + '\n' + 
                
                f'6 {player_id} {profile_id_1[3]}\n' + 
                netcheat_zeroes + db_config['emphopacity'] + db_config['emphcolor'] + '\n#\n'
                )
            ncl_save.write(color_code)
            ncl_save.close()

        #tab here
        expframe = ctk.CTkFrame(self.tab('Export'))
        expframe.grid(row = 0, column = 0)

        exp_text_preview = ctk.CTkLabel(
            expframe, 
            text = f'If you are finished with your Popit color theme,\ngive it a Code Name and export a cheat file!', 
            width = 525
            )

        exp_text_preview.grid(row = 0, pady = 5)

        code_name = ctk.CTkEntry(expframe, placeholder_text = 'Code Name')

        _savebutton = ctk.CTkButton(expframe, text = 'Save YAML Config', command = export_yaml)

        _exportbutton = ctk.CTkButton(expframe, text = "Convert to NCL", command = export_ncl)

        code_name.grid(row = 1, pady = 10)
        _savebutton.grid(row = 2, pady = 10)
        _exportbutton.grid(row = 3, pady = 10)

        self.place(x = 5)

    
class WindowLBP2USNormal(ctk.CTk):
    def __init__(self):
        super().__init__()

        # window setup
        self.title("LBP2 Color Generator")
        self.geometry('540x260')
        self.resizable(False, False)

        # program
        ColorTabList(self)

        self.mainloop()


def main():
    WindowLBP2USNormal()

if __name__ == '__main__':
    main()
