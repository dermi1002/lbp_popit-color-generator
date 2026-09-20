import export_tab
import export_window
import external_objects
import gui_objects
import gui_commands

import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import yaml


startingColorValue: str = '000000'
blankString: str = ''


class ColorTab(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        def change_color_hex(value):
            updateColorHex = self.hexColorField._textvariable.get()

            gui_commands.change_slider_values(
                updateColorHex,
                self.red_slider.value_variable,
                self.green_slider.value_variable,
                self.blue_slider.value_variable
                )

            self.colorPreview.configure(
                background = f'#{updateColorHex}'
            )

            self.colorValue = self.colorPreview.cget('background')[1:]

        def color_slider_command(value):
            gui_commands.change_color_sliders(
                self.red_slider.value_variable.get(),
                self.green_slider.value_variable.get(),
                self.blue_slider.value_variable.get(),
                self.hexColorField,
                self.colorPreview
            )

            self.colorValue = self.colorPreview.cget('background')[1:]

        self.colorPreview = tk.Frame(
            master, 
            background = f'#{startingColorValue}', 
            width = 200, height = 200
            )

        self.colorPreview.place(y = 4)

        self.colorValue: str = self.colorPreview.cget('background')[1:]

        
        self.letter_r = gui_objects.RGBLetter(master, 0, 17)
        self.red_slider = gui_objects.RGBSlider(master, 16, command = color_slider_command)
                
        self.letter_g = gui_objects.RGBLetter(master, 1, 50)
        self.green_slider = gui_objects.RGBSlider(master, 66, command = color_slider_command)

        self.letter_b = gui_objects.RGBLetter(master, 2, 82)
        self.blue_slider = gui_objects.RGBSlider(master, 116, command = color_slider_command)


        hex_related_x_position: int = 225
        hex_related_y_position: int = 170

        self.hexColorLabel = ctk.CTkLabel(master, text = 'HEX Color:')
        
        # I think it's done now
        self.hexColorField = gui_objects.HexColorField(
            master,
            hex_related_y_position
        )
        
        self.color_hex_copy_button = ctk.CTkButton(
            master, 
            text = 'Copy', 
            width = 50, 
            command = lambda: gui_commands.copy_hex_color(self.hexColorField.get())
        )
        
        self.hexColorField.insert(ctk.END, startingColorValue)
        
        self.hexColorField.bind('<Return>', change_color_hex)
        
        self.hexColorLabel.place(x = hex_related_x_position, y = hex_related_y_position)
        
        self.color_hex_copy_button.place(x = 450, y = hex_related_y_position)


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

        # Export Tab Commands
        self.tabExport = export_tab.ExportTab(self.tab('Export'))

        self.tabExport.new_export_ncl_button.configure(
            command = lambda: external_objects.new_export_ncl(
                self.tabExport.code_caption_entry.get(),
                self.primary_colortab.colorValue,
                self.secondary_colortab.colorValue,
                self.tertiary_colortab.colorValue,
                self.emphasis_colortab.colorValue
            )
        )

        self.tabExport.new_save_text_button.configure(
            command = lambda: external_objects.export_value_list(
                self.tabExport.game_title_option.get(),
                self.primary_colortab.colorValue,
                self.secondary_colortab.colorValue,
                self.tertiary_colortab.colorValue,
                self.emphasis_colortab.colorValue
            )
        )

        self.tabExport.new_export_yaml_button.configure(
            command = lambda: external_objects.new_export_yaml(
                self.tabExport.code_caption_entry.get(),
                self.primary_colortab.colorValue,
                self.secondary_colortab.colorValue,
                self.tertiary_colortab.colorValue,
                self.emphasis_colortab.colorValue
            )
        )

        self.exportWindow = None

        def show_export_window():
            if self.exportWindow is None or not self.exportWindow.winfo_exists():
                self.exportWindow = export_window.ExportWindowIII(
                    self.primary_colortab.colorValue,
                    self.secondary_colortab.colorValue,
                    self.tertiary_colortab.colorValue,
                    self.emphasis_colortab.colorValue
                )
                self.exportWindow.focus()
            else:
                self.exportWindow.focus()


        # Toolbar
        self.menuBar = gui_objects.Toolbar(master)

        master.configure(menu = self.menuBar)


        self.menuBar.file_option.add_command(
            label = "New",
            command = lambda: discard_changes_new_file()
        )

        self.menuBar.file_option.add_separator()

        self.menuBar.file_option.add_command(
            state = tk.DISABLED,
            label = 'Open Value List',
            command = lambda: discard_changes_valuelist()
        )

        self.menuBar.file_option.add_command(
            # state = tk.DISABLED,
            label = 'Open YAML Dict.',
            command = lambda: discard_changes_yaml_dictionary()
        )


        def discard_changes_new_file():
            if messagebox.askyesno(
                    "Discard Changes?",
                    f"You are about to start a new file.\nDiscard changes to current session?"
            ):
                gui_commands.batch_change_color_elements(
                    startingColorValue, startingColorValue,
                    startingColorValue, startingColorValue,
                    self.primary_colortab, self.secondary_colortab,
                    self.tertiary_colortab, self.emphasis_colortab,
                    self.tabExport, blankString, ctk.END
                )

        def discard_changes_valuelist():
            if messagebox.askyesno(
                    "Discard Changes?",
                    f"You are about to open a Value List.\nDiscard changes to current session?"
            ):
                open_text_list()

        def discard_changes_yaml_dictionary():
            if messagebox.askyesno(
                    "Discard Changes?",
                    f"You are about to open a YAML Dictionary.\nDiscard changes to current session?"
            ):
                open_yaml_dictionary()

        self.menuBar.file_option.add_separator()

        self.menuBar.file_option.add_command(
            label = "Save Code",
            command = show_export_window
        )

        def open_text_list():
            valuelist_load = tk.filedialog.askopenfilename(
                title = 'Test - Load Value List',
                initialdir = '../save',
                filetypes = [('Value List', '*.txt'), ('All Files', '*.*')],
                defaultextension = '.txt'
            )

            if valuelist_load is None or valuelist_load == ():
                return

            value_list_path = rf"{valuelist_load}"
            # print(value_list_path)

            with open(value_list_path, 'r+') as old_valuelist_content:
                # write sub-optimal code, and once you find an optimization, optimize it
                game_line: str = old_valuelist_content.readline()
                primary_color_line: str = old_valuelist_content.readline()
                secondary_color_line: str = old_valuelist_content.readline()
                tertiary_color_line: str = old_valuelist_content.readline()

                # print(f'{game_line}\n{primary_color_line}\n{secondary_color_line}\n{tertiary_color_line}')

                if 'LBP1' in game_line:
                    gui_commands.batch_change_color_elements(
                        f'{primary_color_line[9:15]}', f'{secondary_color_line[11:17]}', 
                        f'{tertiary_color_line[10:16]}', startingColorValue,
                        self.primary_colortab, self.secondary_colortab,
                        self.tertiary_colortab, self.emphasis_colortab,
                        self.tabExport, blankString, ctk.END
                    )

                # turns out storing them in variables did the trick
                if 'LBP2' in game_line or 'LBP3' in game_line:
                    emphasis_color_line: str = old_valuelist_content.readline()
                    # print(emphasis_color_line)

                    gui_commands.batch_change_color_elements(
                        f'{primary_color_line[11:17]}', f'{secondary_color_line[13:19]}', 
                        f'{tertiary_color_line[12:18]}', f'{emphasis_color_line[12:18]}',
                        self.primary_colortab, self.secondary_colortab,
                        self.tertiary_colortab, self.emphasis_colortab,
                        self.tabExport, blankString, ctk.END
                    )


        def open_yaml_dictionary():
            yaml_dictionary_load = tk.filedialog.askopenfilename(
                title = 'Test - Load YAML Dictionary',
                initialdir = '../save',
                filetypes = [('YAML Dictionary', '*.yaml'), ('All Files', '*.*')],
                defaultextension = '.yaml'
            )

            # finally got to fix this error
            if yaml_dictionary_load is None or yaml_dictionary_load == ():
                return
            else:
                yaml_dictionary_path = rf"{yaml_dictionary_load}"
                with open(yaml_dictionary_path, 'r+') as yaml_dictionary_content:
                    opened_yaml_dictionary = yaml.safe_load(yaml_dictionary_content)

                    opened_yaml_values = opened_yaml_dictionary['color-code']

                    yaml_primary_color = opened_yaml_values['primcolor']
                    yaml_secondary_color = opened_yaml_values['seccolor']
                    yaml_tertiary_color = opened_yaml_values['tertcolor']
                    yaml_emphasis_color = opened_yaml_values['emphcolor']
                    yamlCaption = opened_yaml_values['caption']

                    gui_commands.batch_change_color_elements(
                        f'{yaml_primary_color}', f'{yaml_secondary_color}',
                        f'{yaml_tertiary_color}', f'{yaml_emphasis_color}',
                        self.primary_colortab, self.secondary_colortab,
                        self.tertiary_colortab, self.emphasis_colortab,
                        self.tabExport, f'{yamlCaption}', ctk.END
                    )


        self.place_configure(width = 530, height = 254)
        self.place(x = 5)


class MainProgram(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("LBP Popit Color Generator") # i mean it was able to export files for more than lbp2 
        self.geometry('540x260')          # for a while so i might as well...
        self.resizable(False, False)

        # Program
        ColorTabList(self)

        # Program Closing Function
        def program_close():
            if messagebox.askyesno(
                "Discard Changes?",
                f"You are about to quit the program.\nDiscard changes to current session?"
            ):
                self.destroy()

        self.protocol('WM_DELETE_WINDOW', lambda: program_close())
        self.mainloop()


def main():
    MainProgram()

if __name__ == '__main__':
    main() 
