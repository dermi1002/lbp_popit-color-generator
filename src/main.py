import export_tab
import file_management
import gui_objects
import gui_commands

import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk


startingColorValue: str = '000000'


class ColorTab(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        def change_color_hex(value):
            updateColorHex = self.hexColorField._textvariable.get()

            gui_commands.change_slider_values(
                updateColorHex,
                self.sliderRed.value_variable,
                self.sliderGreen.value_variable,
                self.sliderBlue.value_variable
                )

            self.colorPreview.configure(
                background = f'#{updateColorHex}'
            )

            self.colorValue = self.colorPreview.cget('background')[1:]

        def color_slider_command(value):
            gui_commands.change_color_sliders(
                self.sliderRed.value_variable.get(),
                self.sliderGreen.value_variable.get(),
                self.sliderBlue.value_variable.get(),
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

        
        self.letterR = gui_objects.RGBLetter(master, 0, 17)
        self.sliderRed = gui_objects.RGBSlider(master, 16, command = color_slider_command)
                
        self.letterG = gui_objects.RGBLetter(master, 1, 50)
        self.sliderGreen = gui_objects.RGBSlider(master, 66, command = color_slider_command)

        self.letterB = gui_objects.RGBLetter(master, 2, 82)
        self.sliderBlue = gui_objects.RGBSlider(master, 116, command = color_slider_command)


        hexRelatedPositionX: int = 225
        hexRelatedPositionY: int = 170

        self.hexColorLabel = ctk.CTkLabel(master, text = 'HEX Color:')

        self.hexColorField = gui_objects.HexColorField(
            master,
            hexRelatedPositionY
        )
        
        self.color_hex_copy_button = ctk.CTkButton(
            master, 
            text = 'Copy', 
            width = 50, 
            command = lambda: gui_commands.copy_hex_color(self.hexColorField.get())
        )
        
        self.hexColorField.insert(ctk.END, startingColorValue)
        
        self.hexColorField.bind('<Return>', change_color_hex)
        
        self.hexColorLabel.place(x = hexRelatedPositionX, y = hexRelatedPositionY)
        
        self.color_hex_copy_button.place(x = 450, y = hexRelatedPositionY)


class ColorTabList(ctk.CTkTabview):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        blankString: str = ''

        self.add('Primary')
        self.add('Secondary')
        self.add('Tertiary')
        self.add('Emphasis')
        self.add('Export')

        self.set('Primary')

        self.tabColorPrimary = ColorTab(self.tab('Primary'))
        self.tabColorSecondary = ColorTab(self.tab('Secondary'))
        self.tabColorTertiary = ColorTab(self.tab('Tertiary'))
        self.tabColorEmphasis = ColorTab(self.tab('Emphasis'))

        # Export Tab Commands
        # TODO: change variables in export tab python file
        self.tabExport = export_tab.ExportTab(self.tab('Export'))

        self.tabExport.new_export_ncl_button.configure(
            command = lambda: file_management.new_export_ncl(
                self.tabExport.code_caption_entry.get(),
                self.tabColorPrimary.colorValue,
                self.tabColorSecondary.colorValue,
                self.tabColorTertiary.colorValue,
                self.tabColorEmphasis.colorValue
            )
        )

        self.tabExport.new_save_text_button.configure(
            command = lambda: file_management.export_value_list(
                self.tabExport.game_title_option.get(),
                self.tabColorPrimary.colorValue,
                self.tabColorSecondary.colorValue,
                self.tabColorTertiary.colorValue,
                self.tabColorEmphasis.colorValue
            )
        )

        self.tabExport.new_export_yaml_button.configure(
            command = lambda: file_management.new_export_yaml(
                self.tabExport.code_caption_entry.get(),
                self.tabColorPrimary.colorValue,
                self.tabColorSecondary.colorValue,
                self.tabColorTertiary.colorValue,
                self.tabColorEmphasis.colorValue
            )
        )


        self.exportWindow = None

        # Toolbar
        self.menuBar = gui_objects.Toolbar(master)

        master.configure(menu = self.menuBar)


        self.menuBar.file_option.add_command(
            label = "New",
            command = lambda: gui_commands.discard_changes_new_file(
                startingColorValue, startingColorValue,
                startingColorValue, startingColorValue,
                self.tabColorPrimary, self.tabColorSecondary,
                self.tabColorTertiary, self.tabColorEmphasis,
                self.tabExport, blankString, ctk.END
            )
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
            command = lambda: gui_commands.discard_changes_yaml_dictionary(
                self.tabColorPrimary, self.tabColorSecondary,
                self.tabColorTertiary, self.tabColorEmphasis,
                self.tabExport, ctk.END
            )
        )


        def discard_changes_valuelist():
            if messagebox.askyesno(
                "Discard Changes?",
                f"You are about to open a Value List.\nDiscard changes to current session?"
            ):
                open_text_list()

        self.menuBar.file_option.add_separator()

        self.menuBar.file_option.add_command(
            label = "Save Code",
            command = lambda: gui_commands.show_export_window(
                self.exportWindow,
                self.tabColorPrimary.colorValue,
                self.tabColorSecondary.colorValue,
                self.tabColorTertiary.colorValue,
                self.tabColorEmphasis.colorValue
            )
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
                        self.tabColorPrimary, self.tabColorSecondary,
                        self.tabColorTertiary, self.tabColorEmphasis,
                        self.tabExport, blankString, ctk.END
                    )

                # turns out storing them in variables did the trick
                if 'LBP2' in game_line or 'LBP3' in game_line:
                    emphasis_color_line: str = old_valuelist_content.readline()
                    # print(emphasis_color_line)

                    gui_commands.batch_change_color_elements(
                        f'{primary_color_line[11:17]}', f'{secondary_color_line[13:19]}', 
                        f'{tertiary_color_line[12:18]}', f'{emphasis_color_line[12:18]}',
                        self.tabColorPrimary, self.tabColorSecondary,
                        self.tabColorTertiary, self.tabColorEmphasis,
                        self.tabExport, blankString, ctk.END
                    )


        self.place_configure(width = 530, height = 254)
        self.place(x = 5)


class MainProgram(ctk.CTk):
    def program_close(self):
        if messagebox.askyesno(
            "Discard Changes?",
            f"You are about to quit the program.\nDiscard changes to current session?"
        ):
            self.destroy()

    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("LBP Popit Color Generator")
        self.geometry('540x260')
        self.resizable(False, False)

        # Program
        ColorTabList(self)

        self.protocol('WM_DELETE_WINDOW', lambda: self.program_close())
        self.mainloop()


def main():
    MainProgram()

if __name__ == '__main__':
    main() 
