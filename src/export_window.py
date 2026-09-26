from dontexecuteme import dont_execute_me

import customtkinter as ctk
import tkinter as tk
import file_management

class ExportWindowIII(ctk.CTkToplevel):
    def __init__(
        self,
        colorPrimary, colorSecondary, colorTertiary, colorEmphasis,
        *args, **kwargs
        ):

        super().__init__(*args, **kwargs)

        self.colorPrimary = colorPrimary
        self.colorSecondary = colorSecondary
        self.colorTertiary = colorTertiary
        self.colorEmphasis = colorEmphasis

        exportWindowWidth: int = 385
        exportWindowHeight: int = 355
        
        self.title('Export Code')
        self.geometry(f'{exportWindowWidth}x{exportWindowHeight}')
        self.resizable(False, False)
        self.grab_set()


        def change_file_directory_entry():
            directoryLocation = tk.filedialog.askdirectory(
                title = 'Browse Directory',
                initialdir = '../save'
            )

            if directoryLocation is None or directoryLocation == ():
                return

            directoryLocationOutput: str = f'{directoryLocation}'
            
            codeFilePathField.delete(0, ctk.END)
            codeFilePathField.insert(0, directoryLocationOutput)

        def disable_filetype_ncl(value):
            if gameTitleOption.get() != 'LBP2 (BCUS98245 | 1.33)': 
                codeFileTypeOption.configure(
                    values = ['Value List (.TXT)', 'YAML Dictionary (Old)']
                )
            else:
                codeFileTypeOption.configure(
                    values = [
                        'NetCheat List (.NCL)',
                        'Value List (.TXT)',
                        'YAML Dictionary (Old)'
                    ]
                )

            if codeFileTypeOption.get() == 'NetCheat List (.NCL)' and gameTitleOption.get() != 'LBP2 (BCUS98245 | 1.33)':
                codeFileTypeOption.set('Value List (.TXT)')

        gridLayout = ctk.CTkFrame(self, fg_color = 'transparent')

        exportOptionWidth: int = 190
        
        codeCaptionLabel = ctk.CTkLabel(gridLayout, text = 'Code Name:')
        codeCaptionField = ctk.CTkEntry(gridLayout, width = exportOptionWidth)
        codeCapitonNote = ctk.CTkLabel(gridLayout, text = 'This is included in the exported NCL')

        codeFilePathLabel = ctk.CTkLabel(gridLayout, text = 'File Path:')
        codeFilePathField = ctk.CTkEntry(gridLayout, width = exportOptionWidth)
        codeFilePathBrowse = ctk.CTkButton(
            gridLayout, 
            width = 70,
            text = 'Browse',
            command = change_file_directory_entry
        )


        gameTitleLabel = ctk.CTkLabel(gridLayout, text = 'Game Title:')

        gameTitleDefault = ctk.StringVar(value = 'LBP2 (BCUS98245 | 1.33)')
        gameTitleOption = ctk.CTkOptionMenu(gridLayout)
        gameTitleOption.configure(
            width = exportOptionWidth,
            values = [
                'LBP1 (BCUS98148 | 1.30)',
                'LBP2 (BCUS98245 | 1.33)',
                'LBP3 (BCUS98362 | 1.26)'
            ],
            variable = gameTitleDefault,
            command = disable_filetype_ncl
        )

        gameTitleNote = ctk.CTkLabel(gridLayout, text = 'LBP1 doesn\'t use the Emphasis Color.')


        artemisPrefixOption = ctk.CTkCheckBox(
            gridLayout,
            text = 'Prefix Game Info (Artemis)',
            checkbox_height = 18,
            checkbox_width = 18
        )
        

        codeFileTypeLabel = ctk.CTkLabel(gridLayout, text = 'File Type:')

        codeFileTypeDefault = ctk.StringVar(value = 'Value List (.TXT)')
        codeFileTypeOption = ctk.CTkOptionMenu(gridLayout)
        codeFileTypeOption.configure(
            width = exportOptionWidth,
            values = [
                'NetCheat List (.NCL)',
                'Value List (.TXT)',
                'YAML Dictionary (Old)'
            ],
            variable = codeFileTypeDefault,
            command = None
        )

        codeFileTypeNote = ctk.CTkLabel(
            self,
            text = 'YAML Dictionary Support is\ndeprecated and will be\ndiscontinued in 1.0.0.'
        )

        gameTitleSupportNote = ctk.CTkLabel(
            self,
            justify = 'left',
            text = 'NOTE: This program doesn\'t\nsupport all LBP Titles yet.'
        )


        codeExportButton = ctk.CTkButton(
            self, 
            text = 'Save File',
            width = 125,
            command = lambda: file_management.export_any_format(
                codeFileTypeOption.get(), 
                codeFilePathField.get(),
                gameTitleOption.get(),
                codeCaptionField.get(),
                artemisPrefixOption.get(),
                self.colorPrimary,
                self.colorSecondary,
                self.colorTertiary,
                self.colorEmphasis,
            )
        )
        

        # Edit these values to change the Widgets' Position
        exportWindowCenter = int(exportWindowWidth / 2)
        exportObjectCenter = int(exportWindowCenter - 18)
        
        exportOffsetY: int = 17
        
        exportObjectOffsetX: int = 20
        
        exportObjectRight = int(exportWindowWidth - exportObjectOffsetX)

        exportCodeButtonsBottom = int(exportWindowHeight - exportOffsetY)
        

        # Do NOT look at this mess full of Variables
        codeCaptionLabel.grid(sticky = 'sw', column = 0, row = 0, pady = exportOffsetY)
        codeCaptionField.grid(sticky = 'sw', column = 1, row = 0, padx = 10, pady = exportOffsetY)

        codeCapitonNote.place(anchor = 'n', x = exportObjectCenter, y = 45)


        codeFilePathLabel.grid(sticky = 'nw', column = 0, row = 2, pady = exportOffsetY)
        codeFilePathField.grid(sticky = 'nw', column = 1, row = 2, padx = 10, pady = exportOffsetY)
        codeFilePathBrowse.grid(sticky = 'nw', column = 2, row = 2, pady = exportOffsetY)


        gameTitleLabel.grid(sticky = 'nw', column = 0, row = 3)
        gameTitleOption.grid(sticky = 'nw', column = 1, row = 3, padx = 10)
        gameTitleNote.place(anchor = 'n', x = exportObjectCenter, y = 153)


        artemisPrefixOption.place(anchor = 'n', x = exportObjectCenter, y = 184)
        
        
        codeFileTypeLabel.grid(sticky = 'nw', column = 0, row = 6, pady = 65)
        codeFileTypeOption.grid(sticky = 'nw', column = 1, row = 6, padx = 10, pady = 65)
        codeFileTypeNote.place(anchor = 'n', x = exportWindowCenter, y = 248)

        
        gameTitleSupportNote.place(anchor = 'sw', x = 22, y = exportCodeButtonsBottom)
        codeExportButton.place(anchor = 'se', x = exportObjectRight, y = exportCodeButtonsBottom)

        gridLayout.grid(padx = 22)

def main():
    dont_execute_me()

if __name__ == '__main__':
    main()