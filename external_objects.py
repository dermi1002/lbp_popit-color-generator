import tkinter as tk
from tkinter import messagebox
from pathlib import Path


def get_yaml_content(
        caption, 
        primary_color, 
        secondary_color, 
        tertiary_color, 
        emphasis_color
    ):
    
    yaml_content = str(
        'color-code:\n' +
        f'  caption: \"{caption}\"\n' +

        f'  primcolor: \"{primary_color}\"\n' +
        '  primopacity: \"FF\"\n' +

        f'  seccolor: \"{secondary_color}\"\n' +
        '  secopacity: \"FF\"\n' +

        f'  tertcolor: \"{tertiary_color}\"\n' +
        '  tertopacity: \"FF\"\n' +

        f'  emphcolor: \"{emphasis_color}\"\n' +
        '  emphopacity: \"FF\"\n' +

        '  save: \"save\\\\\"'
        )
    
    return yaml_content

def new_export_yaml(
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

    test_output = get_yaml_content(
        caption, 
        primary_color, 
        secondary_color, 
        tertiary_color, 
        emphasis_color
    )

    yaml_save_location.write(test_output)
    yaml_save_location.close()


def get_ncl_content(
    caption, 
    primary_color, 
    secondary_color, 
    tertiary_color, 
    emphasis_color
    ):

    player_color_pointer: str = "00DC5E8C"

    player_color_pointer_value = ["00000000", "00000004", "00000008", "0000000C"]

    netcheat_zeroes: str = "0 00000000"

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
    
    return ncl_content

def new_export_ncl(
    caption, 
    primary_color, 
    secondary_color, 
    tertiary_color, 
    emphasis_color
    ):

    ncl_save_location = tk.filedialog.asksaveasfile(
        title = "Export NetCheat List", 
        initialdir = "./save", 
        filetypes = [("NetCheat List File", "*.ncl"), ("All Files", "*.*")], 
        defaultextension = ".ncl"
        )
                
    if ncl_save_location is None:
        return

    test_output = get_ncl_content(
        caption, 
        primary_color, 
        secondary_color, 
        tertiary_color, 
        emphasis_color
        )

    ncl_save_location.write(test_output)
    ncl_save_location.close()


def make_value_list(
    game, 
    primary_color, 
    secondary_color, 
    tertiary_color, 
    emphasis_color
    ):

    shortened_game = game[:4]

    if game == 'LBP1 (BCUS98148 | 1.30)':
        test_output = str(
            f'Game: {shortened_game}\n' +
            f'Primary: {primary_color}FF\n' +
            f'Secondary: {secondary_color}FF\n' +
            f'Tertiary: {tertiary_color}FF\n'
        )
    else:
        test_output = str(
            f'Game: {shortened_game}\n' +
            f'Primary: FF{primary_color}\n' +
            f'Secondary: FF{secondary_color}\n' +
            f'Tertiary: FF{tertiary_color}\n' +
            f'Emphasis: FF{emphasis_color}\n'
        )

    return test_output

def export_value_list(
    game, 
    primary_color, 
    secondary_color, 
    tertiary_color, 
    emphasis_color
    ):

    value_list_save_location = tk.filedialog.asksaveasfile(
        title = "Export Value List", 
        initialdir = "./save", 
        filetypes = (("Plain Text", "*.txt"), ("All Files", "*.*")), 
        defaultextension = '.txt'
        )

    value_list_content: str = make_value_list(
        game, 
        primary_color, 
        secondary_color, 
        tertiary_color, 
        emphasis_color
        )

    value_list_save_location.write(value_list_content)
    value_list_save_location.close()


def prefix_game_info(game):
    if game == 'LBP1 (BCUS98148 | 1.30)':
        output: str = ".LBP1 BCUS98148 1.30"
        
        return output

    if game == "LBP2 (BCUS98245 | 1.33)":
        output: str = ".LBP2 BCUS98245 1.33"

        return output

    if game == "LBP3 (BCUS98362 | 1.26)":
        output: str = ".LBP3 BCUS98362 1.26"

        return output


def export_any_format(
    file_type,
    folder_location,
    game,
    caption,  
    checkbox_value,
    primary_color, 
    secondary_color, 
    tertiary_color, 
    emphasis_color
    ):
    
    # file types
    def any_format_content(
        file_type,
        folder_location,
        game,
        caption,  
        primary_color, 
        secondary_color, 
        tertiary_color, 
        emphasis_color
        ):

        if file_type == "NetCheat List (.NCL)":
            output = get_ncl_content( 
                caption,  
                primary_color, 
                secondary_color, 
                tertiary_color, 
                emphasis_color
                )

            return output

        if file_type == "Value List (.TXT)":
            output = make_value_list(
                game,
                primary_color, 
                secondary_color, 
                tertiary_color, 
                emphasis_color
                )

            return output
    
        if file_type == "YAML Dictionary (Old)":
            output = get_yaml_content(
                caption,  
                primary_color, 
                secondary_color, 
                tertiary_color, 
                emphasis_color
                )

            return output

    def find_file_extension(file_type):
        if file_type == "NetCheat List (.NCL)":
            file_extension = ".ncl"

            return file_extension
        
        if file_type == "Value List (.TXT)":
            file_extension = ".txt"

            return file_extension
        
        if file_type == "YAML Dictionary (Old)":
            file_extension = ".yaml"
            
            return file_extension

    def determine_codename(game, caption, checkbox_value):
        if checkbox_value == 1:
            code_filename = f"{prefix_game_info(game)} Custom Popit Color - {caption}"

            print(code_filename)

            return code_filename
        else:
            code_filename = caption
            
            print(code_filename)

            return code_filename

    determined_export_filename = determine_codename(game, caption, checkbox_value)

    file_extension_output: str = find_file_extension(file_type)

    full_file_path = f"{folder_location}/{determined_export_filename}{file_extension_output}"
        
    any_format_output = any_format_content(
        file_type,
        folder_location,
        game,
        caption,  
        primary_color, 
        secondary_color, 
        tertiary_color, 
        emphasis_color
        )

    def check_existing_file():
        current_export = Path(full_file_path)
        if current_export.is_file():
            if tk.messagebox.askyesno(
                title = "Replace Exising Code?", 
                message = 
                    "A Code with the same name and format has been found.\nWould you like to replace it?"
                ):
                
                final_code_export()
        else:
            final_code_export()

    def final_code_export():
        with open(full_file_path, "w") as final_exported_code:
            final_exported_code.write(any_format_output)

        tk.messagebox.showinfo(title = "Export Success", message = "Popit Color Code successfully exported!")


    if folder_location == "" or caption == "":
        incomplete_info_error = tk.messagebox.showerror(
            title = "Inconplete Code Information",
            message = "The text fields for Code Name or File Path are empty.\nFill in both to export the file."
            )
    else:
        check_existing_file()

def read_text_list():
    valuelist_load = tk.filedialog.askopenfilename(
        title = 'Test - Load Value List',
        initialdir = './save',
        filetypes = [('Value List', '*.txt'), ('All Files', '*.*')],
        defaultextension = '.txt'
        )

    if valuelist_load is None:
        return

    value_list_path = rf"{valuelist_load}"
    print(value_list_path)

    with open(value_list_path) as valuelist_content:
        if valuelist_content.read()[6:10] == 'LBP1':
            print(
                'The Game selected in this file is LittleBigPlanet 1.\n' +
                'Therefore, the program will read the first six hexadecimals of a Value as the Color,\n' +
                'and potentially the last two as its Transparency.\n\n' +
                f'Primary Color = {valuelist_content.read()}'
                )
    
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

        self.help_option.add_command(
            label = 'About',
            command = None
            )


if __name__ == '__main__':
    print(
        'This is an external module loaded by the LBP Popit Color Generator\'s Main Program, main.py.\n' +
        'It is not meant to be loaded as a standalone script.\n' +
        'If you want to use its functions, use the Main Program (for the time being).'
        ) # just because