# Changelog

<sub>Written by dermi1002</sub>

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

**Author Note**: This is a **work in progress**. Many changes haven't been documented; and it will take a while to complete it. Contributions are welcome, however!

## [Unreleased] 2026-10-23

### Added

- Module for GUI Objects (`src/gui_objects.py`).
- Module for GUI Layout (`src/gui_layout.py`).
- Module for GUI Commands (`src/gui_commands.py`).
- Module for Export Tab (`src/export_tab.py`).
- Module for Export Window (`src/export_window.py`).
- Module to indicate that a module script isn't meant to be executed (`src/dontexecuteme.py`).
- Functionality that interacts with the 'Code Caption' text field in the `src/main.py` script's Export Tab class instance.
- Changelog document (this file).
- Contributing document.

### Changed

- Move the Export Window class from the `src/main.py` script to Module `src/export_window.py`.
- Move the Export Tab's code from `src/main.py` to Module `src/export_tab.py`.
- Move Objects from `src/main.py` script to Module `src/gui_objects.py`.
- Move Objects' command funcitons from `src/main.py` to Module `src/gui_commands.py`.
- Reformat Function names to Snake Case.
- Reformat Class names to Pascal Case.
- Reformat Variable names to Camel Case.
- Rename Module `src/external_objects.py` to `src/file_management.py`.

### Deprecated

- Disable ability to open Value List (`.txt`) files.

### Fixed

- Add check for if Dialogs for opening files end up with a blank tuple next to None value.
- Add filter `lbp_pcg.bat` for `.gitignore` File in root directory.

### Removed

## [0.4.0-alpha] 2026-09-12

### Added

- Automated Setup Script for Windows, written in Batch.
- Automated Setup Script for Ubuntu (Linux), written in Bash.
- `src/` Directory for Python Scripts and Requirements File.

### Changed

- Move Python Scripts, Requirements File, and `.gitignore` File to `src/` Directory.
- Add filters in the `.gitignore` File in root directory for Files/Directories created by Automated Setup Scripts.

### Deprecated

### Fixed

### Removed

## [0.3.0-alpha] 2025-10-20

### Added

- [x] Add a toolbar to the program
- [x] Add top-level windows for File Export and window closing prompt
- [x] Add a new plain text Value list to deprecate .YAML support
- [x] Add functionality to change colors via hex color entry and .TXT/.YAML importing

### Changed

- [x] Figure out what to do with the Export Tab

### Deprecated

### Fixed

### Removed

## [0.2.0-alpha] 2025-09-03

### Added

### Changed

- Separate functions to their own script

### Deprecated

### Fixed

### Removed

## [0.1.1-alpha] 2025-06-13

### Added

### Changed

- Edit code functions, values, etc., for extra readability among project contributors

### Deprecated

### Fixed

- Change the source value of colors from Hex text field's content to Color Preview's background color in exporting functionality

### Removed

## [0.1.0-alpha] 2025-06-02 [YANKED]

### Added

- Example Popit Color file for demonstration purposes (`save/demo popit color.yaml`).
- Empty `.gitignore` file.
- Section covering how to use the program in `README.md`.
- Section covering how NetCheat List files (`.ncl`) work in `README.md`.
- To-do List covering tasks to work on and completed tasks in `README.md`.
- Image showing the UI of the Primary Color Tab of the program (`.readme_pictures/main_firstlook.png`).
- Image showing the use of the Primary Color Tab of the program (`.readme_pictures/main_changecolor.png`).
- Image showing the UI of the Export Tab of the program (`.readme_pictures/main_export.png`).
- Image showing the use of the Code Name text field in the Export Tab of the program (`.readme_pictures/main_exportcodename.png`).
- `CTkFrame` Object `ColorTab` which contains code for the Color Tab UI in `main.py`.
- `CTkSlider` Object `RGBSlider` which contains specific configurations for the RGB Sliders in `main.py`.
- `CTkLabel` Object `RGBLetter` which contains code for which letter to display next to its associated RGB Slider in `main.py`.
- `CTkTabView` Object `ColorTabList` which contains the GUI layout for the program in `main.py`.
- Class `MainProgram` which sets up the program window and loads Layout `ColorTabList` in `main.py`.

### Changed

- Rework the code into classes and functions for easier functionality with other games and versions in `main.py`.
- Reword the Warning in `README.md`.
- Specify CustomTkinter Version (`5.2.2`) in `requirements.txt`.
- Specify Version Pyperclip Version (`1.9.0`) in `requirements.txt`.
- Specify VersionPyYAML Version (`6.0.2`) in `requirements.txt`.

### Removed

- Duplicates of objects for each Color Tab and their respective functions in `main.py`.
- Instruction to import the OS module in `main.py`.

<!-- Version Links -->

[unreleased]: https://github.com/dermi1002/lbp_popit-color-generator/compare/v0.4.0-alpha...code-refactor
[0.4.0-alpha]: https://github.com/dermi1002/lbp_popit-color-generator/compare/v0.3.0-alpha...v0.4.0-alpha
[0.3.0-alpha]: https://github.com/dermi1002/lbp_popit-color-generator/compare/v0.2.0-alpha...v0.3.0-alpha
[0.2.0-alpha]: https://github.com/dermi1002/lbp_popit-color-generator/compare/v0.1.1-alpha...v0.2.0-alpha
[0.1.1-alpha]: https://github.com/dermi1002/lbp_popit-color-generator/compare/v0.1.0-alpha...v0.1.1-alpha
[0.1.0-alpha]: https://github.com/dermi1002/lbp_popit-color-generator/compare/1edc69e4bb9b0e1c33b3fbd6c14e7d9901fd9de6...v0.1.0-alpha