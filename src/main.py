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


class ColorTab(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        def change_color_hex(value):
            gui_commands.change_slider_values(
                self.hexColorField._textvariable.get(),
                self.red_slider.value_variable,
                self.green_slider.value_variable,
                self.blue_slider.value_variable
                )

            self.color_preview.configure(
                background = f'#{self.hexColorField._textvariable.get()}'
            )

        def color_slider_command(value):
            newColorHex = gui_commands.change_color_sliders(
                self.red_slider.value_variable.get(),
                self.green_slider.value_variable.get(),
                self.blue_slider.value_variable.get(),
                self.hexColorField,
                self.color_preview
            )

            return newColorHex


        self.color_preview = tk.Frame(
            master, 
            background = f'#{startingColorValue}', 
            width = 200, height = 200
            )

        self.color_preview.place(y = 4)

        
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
    
    # TODO: get rid of this code
    @property
    def color_preview(self): return self._color_preview.cget('background')[1:]

    @color_preview.setter
    def color_preview(self, value):
        self._color_preview = value
        if value: print(value)


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

        # TODO: fix non-updated values
        self.popitColorValues: list = [
            self.primary_colortab.color_preview.cget('background')[1:],
            self.secondary_colortab.color_preview.cget('background')[1:],
            self.tertiary_colortab.color_preview.cget('background')[1:],
            self.emphasis_colortab.color_preview.cget('background')[1:]
        ]

        self.tabExport = export_tab.ExportTab(
            self.tab('Export'),
            *self.popitColorValues,
        )

        self.exportWindow = None

        def show_export_window():
            if self.exportWindow is None or not self.exportWindow.winfo_exists():
                self.exportWindow = export_window.ExportWindowIII(
                    *self.popitColorValues
                )
                self.exportWindow.focus()
            else:
                self.exportWindow.focus()


        # Toolbar
        self.test_toolbar = gui_objects.Toolbar(master)

        master.configure(menu = self.test_toolbar)


        self.test_toolbar.file_option.add_command(
            label = "New",
            command = lambda: discard_changes_new_file()
        )

        self.test_toolbar.file_option.add_separator()

        self.test_toolbar.file_option.add_command(
            state = tk.DISABLED,
            label = 'Open Value List',
            command = lambda: discard_changes_valuelist()
        )

        self.test_toolbar.file_option.add_command(
            # state = tk.DISABLED,
            label = 'Open YAML Dict.',
            command = lambda: discard_changes_yaml_dictionary()
        )


        def discard_changes_new_file():
            if messagebox.askyesno(
                    "Discard Changes?",
                    f"You are about to start a new file.\nDiscard changes to current session?"
            ):
                batch_change_color_elements(
                    startingColorValue,
                    startingColorValue,
                    startingColorValue,
                    startingColorValue
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

        self.test_toolbar.file_option.add_separator()

        self.test_toolbar.file_option.add_command(
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
                    batch_change_color_elements(
                        f'{primary_color_line[9:15]}',
                        f'{secondary_color_line[11:17]}', 
                        f'{tertiary_color_line[10:16]}',
                        startingColorValue # Godot made me let go of that lol 
                        )

                # turns out storing them in variables did the trick
                if 'LBP2' in game_line or 'LBP3' in game_line:
                    emphasis_color_line: str = old_valuelist_content.readline()
                    # print(emphasis_color_line)

                    batch_change_color_elements(
                        f'{primary_color_line[11:17]}',
                        f'{secondary_color_line[13:19]}', 
                        f'{tertiary_color_line[12:18]}',
                        f'{emphasis_color_line[12:18]}'
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

                    yaml_primary_color = opened_yaml_values['primcolor'] # yikes! shortened "variables"! could've been worse...
                    yaml_secondary_color = opened_yaml_values['seccolor']
                    yaml_tertiary_color = opened_yaml_values['tertcolor']
                    yaml_emphasis_color = opened_yaml_values['emphcolor']

                    batch_change_color_elements(
                        f'{yaml_primary_color}',
                        f'{yaml_secondary_color}',
                        f'{yaml_tertiary_color}',
                        f'{yaml_emphasis_color}'
                    )


        def batch_change_color_elements(
            primary_color, secondary_color, tertiary_color, emphasis_color
            ):

            external_objects.open_color_file(
                primary_color,
                self.primary_colortab.color_preview,
                self.primary_colortab.hexColorField,
                self.primary_colortab.red_slider.value_variable,
                self.primary_colortab.green_slider.value_variable,
                self.primary_colortab.blue_slider.value_variable,
                ctk.END
            )

            external_objects.open_color_file(
                secondary_color,
                self.secondary_colortab.color_preview,
                self.secondary_colortab.hexColorField,
                self.secondary_colortab.red_slider.value_variable,
                self.secondary_colortab.green_slider.value_variable,
                self.secondary_colortab.blue_slider.value_variable,
                ctk.END
            )

            external_objects.open_color_file(
                tertiary_color,
                self.tertiary_colortab.color_preview,
                self.tertiary_colortab.hexColorField,
                self.tertiary_colortab.red_slider.value_variable,
                self.tertiary_colortab.green_slider.value_variable,
                self.tertiary_colortab.blue_slider.value_variable,
                ctk.END
            )

            external_objects.open_color_file(
                emphasis_color,
                self.emphasis_colortab.color_preview,
                self.emphasis_colortab.hexColorField,
                self.emphasis_colortab.red_slider.value_variable,
                self.emphasis_colortab.green_slider.value_variable,
                self.emphasis_colortab.blue_slider.value_variable,
                ctk.END
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
