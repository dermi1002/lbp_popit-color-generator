from dontexecuteme import dont_execute_me

import gui_commands

import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import yaml


def get_yaml_content(
        codeCaption, 
        colorPrimary, 
        colorSecondary, 
        colorTertiary, 
        colorEmphasis
    ):
    
    fileContentYaml = str(
        'color-code:\n' +
        f'  caption: \"{codeCaption}\"\n' +

        f'  primcolor: \"{colorPrimary}\"\n' +
        '  primopacity: \"FF\"\n' +

        f'  seccolor: \"{colorSecondary}\"\n' +
        '  secopacity: \"FF\"\n' +

        f'  tertcolor: \"{colorTertiary}\"\n' +
        '  tertopacity: \"FF\"\n' +

        f'  emphcolor: \"{colorEmphasis}\"\n' +
        '  emphopacity: \"FF\"\n' +

        '  save: \"save\\\\\"'
    )
    
    return fileContentYaml

def new_export_yaml(
    codeCaption, 
    colorPrimary, 
    colorSecondary, 
    colorTertiary, 
    colorEmphasis
    ):

    saveLocationYaml = tk.filedialog.asksaveasfile(
        title = "Export YAML Dictionary", 
        initialdir = "../save", 
        filetypes = (("YAML Dictionary File", "*.yaml"), ("All Files", "*.*")), 
        defaultextension = '.yaml'
    )

    if saveLocationYaml is None or saveLocationYaml == ():
        return
    else:
        outputYaml = get_yaml_content(
            codeCaption, 
            colorPrimary, 
            colorSecondary, 
            colorTertiary, 
            colorEmphasis
        )

        saveLocationYaml.write(outputYaml)
        saveLocationYaml.close()


def get_ncl_content(
    codeCaption, 
    colorPrimary, 
    colorSecondary, 
    colorTertiary, 
    colorEmphasis
    ):

    playerColorPointer: str = "00DC5E8C"
    playerColorPointerOffsets = ["00000000", "00000004", "00000008", "0000000C"]
    netCheatCommand: str = "0 00000000"

    fileContentNetCheat = str(
        f'{codeCaption}\n0\n' + 

        f'6 {playerColorPointer} {playerColorPointerOffsets[0]}\n' + 
        f'{netCheatCommand} FF{colorPrimary}\n' + 

        f'6 {playerColorPointer} {playerColorPointerOffsets[1]}\n' + 
        f'{netCheatCommand} FF{colorSecondary}\n' + 

        f'6 {playerColorPointer} {playerColorPointerOffsets[2]}\n' + 
        f'{netCheatCommand} FF{colorTertiary}\n' + 
                
        f'6 {playerColorPointer} {playerColorPointerOffsets[3]}\n' + 
        f'{netCheatCommand} FF{colorEmphasis}\n#\n'
    )
    
    return fileContentNetCheat

def new_export_ncl(
    codeCaption, 
    colorPrimary, 
    colorSecondary, 
    colorTertiary, 
    colorEmphasis
    ):

    saveLocationNetCheat = tk.filedialog.asksaveasfile(
        title = "Export NetCheat List", 
        initialdir = "../save", 
        filetypes = [("NetCheat List File", "*.ncl"), ("All Files", "*.*")], 
        defaultextension = ".ncl"
    )
                
    if saveLocationNetCheat is None or saveLocationNetCheat == ():
        return
    else:
        outputNetCheat = get_ncl_content(
            codeCaption, 
            colorPrimary, 
            colorSecondary, 
            colorTertiary, 
            colorEmphasis
        )

        saveLocationNetCheat.write(outputNetCheat)
        saveLocationNetCheat.close()


def make_value_list(
    game, 
    colorPrimary, 
    colorSecondary, 
    colorTertiary, 
    colorEmphasis
    ):

    shortenedGame = game[:4]

    if game == 'LBP1 (BCUS98148 | 1.30)':
        outputValueList = str(
            f'Game: {shortenedGame}\n' +
            f'Primary: {colorPrimary}FF\n' +
            f'Secondary: {colorSecondary}FF\n' +
            f'Tertiary: {colorTertiary}FF\n'
        )
    else:
        outputValueList = str(
            f'Game: {shortenedGame}\n' +
            f'Primary: FF{colorPrimary}\n' +
            f'Secondary: FF{colorSecondary}\n' +
            f'Tertiary: FF{colorTertiary}\n' +
            f'Emphasis: FF{colorEmphasis}\n'
        )

    return outputValueList

def export_value_list(
    game, 
    colorPrimary, 
    colorSecondary, 
    colorTertiary, 
    colorEmphasis
    ):

    value_list_save_location = tk.filedialog.asksaveasfile(
        title = "Export Value List", 
        initialdir = "./save", 
        filetypes = (("Plain Text", "*.txt"), ("All Files", "*.*")), 
        defaultextension = '.txt'
    )

    value_list_content: str = make_value_list(
        game, 
        colorPrimary, 
        colorSecondary, 
        colorTertiary, 
        colorEmphasis
    )

    value_list_save_location.write(value_list_content)
    value_list_save_location.close()


def prefix_game_info(game):
    if game == 'LBP1 (BCUS98148 | 1.30)':
        output: str = "- LBP1 BCUS98148 01.30" # game versions will finally show up on artemis lol
        return output

    if game == "LBP2 (BCUS98245 | 1.33)":
        output: str = "- LBP2 BCUS98245 01.33"
        return output

    if game == "LBP3 (BCUS98362 | 1.26)":
        output: str = "- LBP3 BCUS98362 01.26"
        return output


def export_any_format(
    fileType,
    folderLocation,
    game,
    codeCaption,  
    prefixInfoChecked,
    colorPrimary, 
    colorSecondary, 
    colorTertiary, 
    colorEmphasis
    ):
    
    # file types
    def any_format_content(
        game,
        codeCaption,  
        colorPrimary, 
        colorSecondary, 
        colorTertiary, 
        colorEmphasis
        ):

        if fileType == "NetCheat List (.NCL)":
            output = get_ncl_content( 
                codeCaption,  
                colorPrimary, 
                colorSecondary, 
                colorTertiary, 
                colorEmphasis
            )

            return output

        if fileType == "Value List (.TXT)":
            output = make_value_list(
                game,
                colorPrimary, 
                colorSecondary, 
                colorTertiary, 
                colorEmphasis
            )

            return output
    
        if fileType == "YAML Dictionary (Old)":
            output = get_yaml_content(
                codeCaption,  
                colorPrimary, 
                colorSecondary, 
                colorTertiary, 
                colorEmphasis
            )

            return output

    def find_file_extension(fileType):
        if fileType == "NetCheat List (.NCL)":
            fileExtension = ".ncl"
            return fileExtension
        
        if fileType == "Value List (.TXT)":
            fileExtension = ".txt"
            return fileExtension
        
        if fileType == "YAML Dictionary (Old)":
            fileExtension = ".yaml"
            return fileExtension

    def set_codename(game, codeCaption, prefixInfoChecked):
        if prefixInfoChecked == 1:
            code_filename = f"{prefix_game_info(game)} Custom Popit Color - {codeCaption}"
            return code_filename
        else:
            code_filename = codeCaption
            return code_filename

    finalCodeName = set_codename(game, codeCaption, prefixInfoChecked)

    outputFileExtension: str = find_file_extension(fileType)

    fullFilePath = f"{folderLocation}/{finalCodeName}{outputFileExtension}"
        
    anyFormatOutput = any_format_content(
        fileType,
        folderLocation,
        game,
        codeCaption,  
        colorPrimary, 
        colorSecondary, 
        colorTertiary, 
        colorEmphasis
        )

    def check_existing_file():
        selectedFilePath = Path(fullFilePath)
        if selectedFilePath.is_file():
            if tk.messagebox.askyesno(
                title = "Replace Exising Code?", 
                message = 
                    "A Code with the same name and format has been found.\nWould you like to replace it?"
            ):
                final_code_export()
        else:
            final_code_export()

    def final_code_export():
        with open(fullFilePath, "w") as exportFinalCode:
            exportFinalCode.write(anyFormatOutput)

        tk.messagebox.showinfo(
            title = "Export Success!",
            message = "Popit Color Code successfully exported!"
        )


    if folderLocation == "" or codeCaption == "":
        incomplete_info_error = tk.messagebox.showerror(
            title = "Inconplete Code Information",
            message =
                "The text fields for Code Name or File Path are empty.\nFill in both to export the file."
        )
    else:
        check_existing_file()


def open_color_file(
    colorValue,
    previewObject,
    hexField,
    openValueRed,
    openValueGreen,
    openValueBlue,
    whichEnd
    ):

    previewObject.configure(background = f'#{colorValue}')
    hexField.delete(0, whichEnd)
    hexField.insert(0, str(previewObject.cget('background')[1:]))

    gui_commands.change_slider_values(
        hexField.get(),
        openValueRed,
        openValueGreen,
        openValueBlue
    )


def open_yaml_dictionary(
    tabColorPrimary, tabColorSecondary, tabColorTertiary, tabColorEmphasis,
    tabExport, whichEnd
    ):

    loadFileYaml = tk.filedialog.askopenfilename(
        title = 'Test - Load YAML Dictionary',
        initialdir = '../save',
        filetypes = [('YAML Dictionary', '*.yaml'), ('All Files', '*.*')],
        defaultextension = '.yaml'
    )

    # finally got to fix this error
    if loadFileYaml is None or loadFileYaml == ():
        return
    else:
        getPathYaml = rf"{loadFileYaml}"
        with open(getPathYaml, 'r+') as fileContentYaml:
            openedFileYaml = yaml.safe_load(fileContentYaml)

            fileValuesYaml = openedFileYaml['color-code']

            yamlColorPrimary = fileValuesYaml['primcolor']
            yamlColorSecondary = fileValuesYaml['seccolor']
            yamlColorTertiary = fileValuesYaml['tertcolor']
            yamlColorEmphasis = fileValuesYaml['emphcolor']
            yamlCaption = fileValuesYaml['caption']

            gui_commands.batch_change_color_elements(
                f'{yamlColorPrimary}', f'{yamlColorSecondary}',
                f'{yamlColorTertiary}', f'{yamlColorEmphasis}',
                tabColorPrimary, tabColorSecondary,
                tabColorTertiary, tabColorEmphasis,
                tabExport, f'{yamlCaption}', whichEnd
            )


def main():
    dont_execute_me()

if __name__ == '__main__':
    main()
