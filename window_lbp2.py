import customtkinter as ctk
import pyperclip
import yaml


class ColorTabList(ctk.CTkTabview):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.place_configure(width=530, height=254)

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
                    self.R = int(self.red_slider.get())
                    self.G = int(self.green_slider.get())
                    self.B = int(self.blue_slider.get())

                    self._hexprint = '%02X%02X%02X' % (self.R, self.G, self.B)

                    self.color_preview.configure(bg_color=f'#{self._hexprint}')

                    self._hexentry.delete(0, ctk.END)
                    self._hexentry.insert(0, self._hexprint)

                def copy_hexentry():
                    pyperclip.copy(self._hexentry.get())


                self.color_preview = ctk.CTkLabel(master, text='', bg_color='#000', width=200, height=200)
                self.color_preview.place(y=4)


                self.letter_r = ctk.CTkLabel(master, text='R').place(x=225, y=10)
                self.red_slider = ctk.CTkSlider(master, from_=0, to=255, width=256, command=change_color)

                self.letter_g = ctk.CTkLabel(master, text='G').place(x=225, y=60)
                self.green_slider = ctk.CTkSlider(master, from_=0, to=255, width=256, command=change_color)

                self.letter_b = ctk.CTkLabel(master, text='B').place(x=225, y=110)
                self.blue_slider = ctk.CTkSlider(master, from_=0, to=255, width=256, command=change_color)


                self.red_slider.place(x=260, y=16)
                self.red_slider.configure(number_of_steps=256)
                self.red_slider.set(0)

                self.green_slider.place(x=260, y=66)
                self.green_slider.configure(number_of_steps=256)
                self.green_slider.set(0)

                self.blue_slider.place(x=260, y=116)
                self.blue_slider.configure(number_of_steps=256)
                self.blue_slider.set(0)


                self._hexdisplay = ctk.CTkLabel(master, text='HEX Color:').place(x=225, y=170)
                self._hexentry = ctk.CTkEntry(master)
                self._hexcopy = ctk.CTkButton(master, text='Copy', width=50, command=copy_hexentry).place(x=450, y=170)

                self._hexentry.place(x=297, y=170)
                self._hexentry.insert(ctk.END, '000000')

        self.pri_colortab = ColorTab(self.tab('Primary'))
        self.sec_colortab = ColorTab(self.tab('Secondary'))
        self.ter_colortab = ColorTab(self.tab('Tertiary'))
        self.emp_colortab = ColorTab(self.tab('Emphasis'))


        # Export Tab
        def export_yaml():
            config_export = ctk.filedialog.asksaveasfile(title="Export YAML Config", initialdir="./save", filetypes=(("YAML Configuration", "*.yaml"), ("All Files", "*.*")), defaultextension='.yaml')
            if config_export is None:
                return
            color_config = str(f'color-code:\n  caption: \"{code_name.get()}\"\n  primcolor: \"{self.pri_colortab._hexentry.get()}\"\n  primopacity: \"FF\"\n  seccolor: \"{self.sec_colortab._hexentry.get()}\"\n  secopacity: \"FF\"\n  tertcolor: \"{self.ter_colortab._hexentry.get()}\"\n  tertopacity: \"FF\"\n  emphcolor: \"{self.emp_colortab._hexentry.get()}\"\n  emphopacity: \"FF\"\n  save: \"export\\\\\"')
            config_export.write(color_config)
            config_export.close() # can i optimize this?


        def color_convert():
            yaml_set = ctk.filedialog.askopenfilename(title="Import YAML Config", initialdir="./save")
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


            player_id = "00DC5E8C"

            profile_id_1 = ["00000000", "00000004", "00000008", "0000000C"]

            _zeroes = "0 00000000 "

            ncl_save = ctk.filedialog.asksaveasfile(title="Export NCL Code", initialdir="export", filetypes=[("NetCheat List File", "*.ncl"), ("All Files", "*.*")], defaultextension=".ncl")
            if ncl_save is None:
                return
            color_code = str(
                db_config['caption'] + '\n' + '0\n' + 
                '6 ' + player_id + ' ' + profile_id_1[0] + '\n' + 
                _zeroes + db_config['primopacity'] + db_config['primcolor'] + '\n' + 
                '6 ' + player_id + ' ' + profile_id_1[1] + '\n' + 
                _zeroes + db_config['secopacity'] + db_config['seccolor'] + '\n' + 
                '6 ' + player_id + ' ' + profile_id_1[2] + '\n' + 
                _zeroes + db_config['tertopacity'] + db_config['tertcolor'] + '\n' + 
                '6 ' + player_id + ' ' + profile_id_1[3] + '\n' + 
                _zeroes + db_config['emphopacity'] + db_config['emphcolor'] + '\n' + '#\n'
                )
            ncl_save.write(color_code)
            ncl_save.close()

        #tab here
        expframe = ctk.CTkFrame(self.tab('Export'))
        expframe.grid(row=0, column=0)

        exp_text_preview = ctk.CTkLabel(expframe, text=f'If you are finished with your Popit color theme,\ngive it a Code Name and export a cheat file!', width=525)

        exp_text_preview.grid(row=0, pady=5)

        code_name = ctk.CTkEntry(expframe, placeholder_text='Code Name')

        _savebutton = ctk.CTkButton(expframe, text='Save YAML Config', command=export_yaml)

        _exportbutton = ctk.CTkButton(expframe, text="Convert to NCL", command=export_ncl)

        code_name.grid(row=1, pady=10)
        _savebutton.grid(row=2, pady=10)
        _exportbutton.grid(row=3, pady=10)

        self.place(x=5)

    
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
