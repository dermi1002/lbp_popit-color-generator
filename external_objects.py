import tkinter as tk
from tkinter import messagebox


def export_yaml(
    caption, 
    primary_color, 
    secondary_color, 
    tertiary_color, 
    emphasis_color
    ):

    yaml_save_location = tk.filedialog.asksaveasfile(
        title = "Export YAML Dictionary", 
        initialdir = "./save", 
        filetypes = (("YAML Dictionary File", "*.yaml"), ("All Files", "*.*")), 
        defaultextension = '.yaml'
        )
                
    if yaml_save_location is None:
        return

    yaml_content = str(
        'color-code:\n' +
        '  caption: \"' + caption + '\"\n' +

        '  primcolor: \"' + primary_color + '\"\n' +
        '  primopacity: \"FF\"\n' +

        '  seccolor: \"' + secondary_color + '\"\n' +
        '  secopacity: \"FF\"\n' +

        '  tertcolor: \"' + tertiary_color + '\"\n' +
        '  tertopacity: \"FF\"\n' +

        '  emphcolor: \"' + emphasis_color + '\"\n' +
        '  emphopacity: \"FF\"\n' +

        '  save: \"export\\\\\"'
        )
    yaml_save_location.write(yaml_content)
    yaml_save_location.close()


def export_ncl(
    caption, 
    primary_color, 
    secondary_color, 
    tertiary_color, 
    emphasis_color
    ):

    player_color_pointer: str = "00DC5E8C"

    player_color_pointer_value = ["00000000", "00000004", "00000008", "0000000C"]

    netcheat_zeroes: str = "0 00000000"

    ncl_save_location = tk.filedialog.asksaveasfile(
        title = "Export NetCheat List", 
        initialdir = "./save", 
        filetypes = [("NetCheat List File", "*.ncl"), ("All Files", "*.*")], 
        defaultextension = ".ncl"
        )
                
    if ncl_save_location is None:
        return

    ncl_content = str(
        f'{caption}\n0\n' + 

        f'6 {player_color_pointer} {player_color_pointer_value[0]}\n' + 
        f'{netcheat_zeroes} FF{primary_color}\n' + 

        f'6 {player_color_pointer} {player_color_pointer_value[1]}\n' + 
        f'{netcheat_zeroes} FF{secondary_color}\n' + 

        f'6 {player_color_pointer} {player_color_pointer_value[2]}\n' + 
        f'{netcheat_zeroes} FF{tertiary_color}\n' + 
                
        f'6 {player_color_pointer} {player_color_pointer_value[3]}\n' + 
        f'{netcheat_zeroes} FF{emphasis_color}\n#\n'
        )
    ncl_save_location.write(ncl_content)
    ncl_save_location.close()


def closing_prompt(master):
    if messagebox.askyesno('Close the Program?', 'Are you sure you want to close the program?'):
        master.destroy()


class Toolbar(tk.Menu):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # File
        self.file_option = tk.Menu(self, tearoff = 0)

        self.add_cascade(label = 'File', menu = self.file_option)

        # Help
        self.help_option = tk.Menu(self, tearoff = 0)

        self.add_cascade(label = 'Help', menu = self.help_option)
