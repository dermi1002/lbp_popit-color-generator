import export_window
import external_objects
import gui_objects
import gui_commands

import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import yaml


color_beginning_value: str = '000000'


class ColorTab(ctk.CTkFrame):

    def hex_certain_characters(master, event):
        if event.char in (
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'A', 'B', 'C', 'D', 'E', 'F',
            'a', 'b', 'c', 'd', 'e', 'f'
        ):
            return True
        elif event.keysym not in (
            'Alt_L', 'F4',
            'BackSpace', 'Return', 'Left', 'Right',
            'Control_L' 'V'
        ):
            return 'break'
        else:
            return False

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        def testlimit(P):
            print(P)
            try:
                self.hex_color_field._textvariable.trace_add('write', uppercaseletters)
            except AttributeError:
                # if you somehow got to open this gui program in python 3.6.0 or lower
                self.hex_color_field._textvariable.trace_add('w', uppercaseletters)

            if len(P) <= 6:
                return True
            else:
                self.bell()
                return False

        def change_color_sliders_new(red: int, green: int, blue: int):
            self.color_print_hex = '%02X%02X%02X' % (red, green, blue)

            self.hex_color_field.delete(0, ctk.END)
            self.hex_color_field.insert(0, self.color_print_hex)

            self.color_preview.configure(
                background = f'#{self.hex_color_field._textvariable.get()}'
            )

        def change_color_hex(value):
            external_objects.change_slider_values(
                self.hex_entry_text.get(),
                self.red_slider.value_variable,
                self.green_slider.value_variable,
                self.blue_slider.value_variable
                )

            self.color_preview.configure(background = f'#{self.hex_entry_text.get()}')

        def color_slider_command(value):
            change_color_sliders_new(
                self.red_slider.value_variable.get(),
                self.green_slider.value_variable.get(),
                self.blue_slider.value_variable.get()
            )


        self.color_preview = tk.Frame(
            master, 
            background = f'#{color_beginning_value}', 
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

        self.color_hex_label = ctk.CTkLabel(master, text = 'HEX Color:')
        
        # Doing that right now...
        self.hex_entry_text = tk.StringVar(master)

        vcmd = (self.register(testlimit), '%P')

        self.hex_color_field = gui_objects.HexColorField(
            master,
            hex_related_y_position
            # self.hex_entry_text
        )
        
        # TODO: figure out why 3 arguments are taken from this function
        def uppercaseletters(arg0, arg1, arg2):
            print(arg0, ',', arg1, ',', arg2)
            self.hex_color_field._textvariable.set(self.hex_color_field._textvariable.get().upper())

        self.color_hex_copy_button = ctk.CTkButton(
            master, 
            text = 'Copy', 
            width = 50, 
            command = lambda: gui_commands.copy_hex_color(self.hex_color_field.get())
        )
        
        self.hex_color_field.configure(
            textvariable = self.hex_entry_text,
            validatecommand = vcmd
        )

        self.hex_color_field.insert(ctk.END, color_beginning_value)
        self.hex_color_field.bind('<KeyPress>', self.hex_certain_characters)
        self.hex_color_field.bind('<Return>', change_color_hex)
        
        self.color_hex_label.place(x = hex_related_x_position, y = hex_related_y_position)
        
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
                self.test_export_window_iii = export_window.ExportWindowIII(
                    self.primary_colortab.color_preview.cget('background')[1:],
                    self.secondary_colortab.color_preview.cget('background')[1:],
                    self.tertiary_colortab.color_preview.cget('background')[1:],
                    self.emphasis_colortab.color_preview.cget('background')[1:]
                    )
                self.test_export_window_iii.focus()
            else:
                self.test_export_window_iii.focus()


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
                    color_beginning_value,
                    color_beginning_value,
                    color_beginning_value,
                    color_beginning_value
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
            command = show_export_window_iii
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
                        color_beginning_value # Godot made me let go of that lol 
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


        def batch_change_color_elements(primary_color, secondary_color, tertiary_color, emphasis_color):
            external_objects.open_color_file(
                primary_color,
                self.primary_colortab.color_preview,
                self.primary_colortab.hex_color_field,
                self.primary_colortab.red_slider.value_variable,
                self.primary_colortab.green_slider.value_variable,
                self.primary_colortab.blue_slider.value_variable,
                ctk.END
            )

            external_objects.open_color_file(
                secondary_color,
                self.secondary_colortab.color_preview,
                self.secondary_colortab.hex_color_field,
                self.secondary_colortab.red_slider.value_variable,
                self.secondary_colortab.green_slider.value_variable,
                self.secondary_colortab.blue_slider.value_variable,
                ctk.END
            )

            external_objects.open_color_file(
                tertiary_color,
                self.tertiary_colortab.color_preview,
                self.tertiary_colortab.hex_color_field,
                self.tertiary_colortab.red_slider.value_variable,
                self.tertiary_colortab.green_slider.value_variable,
                self.tertiary_colortab.blue_slider.value_variable,
                ctk.END
            )

            external_objects.open_color_file(
                emphasis_color,
                self.emphasis_colortab.color_preview,
                self.emphasis_colortab.hex_color_field,
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
