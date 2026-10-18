# Change Log

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] 2026-10-06

### Added

- Module for GUI Objects
- Module for GUI Layout
- Module for GUI Commands
- Module for Export Tab
- Module for Export Window
- Module to indicate that certain modules used by the `main.py` script aren't meant to be executed
- Functionality that interacts with the 'Code Caption' text field in the `main.py` script's Export Tab class instance
- Change Log document (this file)
- Contributing document

### Changed

- Move the Export Window class from the `main.py` script to Module `export_window.py`
- Move Objects from `main.py` script to Module `gui_objects.py`
- Move Objects' command funcitons from `main.py` to Module `gui_commands.py`
- Reformat Function names to Snake Case
- Reformat Class names to Pascal Case
- Reformat Variable names to Camel Case
- Renamed Module `external_objects.py` to `file_management.py`

### Deprecated

- Disable ability to open Value List (.TXT) files

### Fixed

- Added check for if Dialogs for opening files end up with a blank tuple next to None value

### Removed

## [0.4.0-alpha] 2026-09-12

### Added

- Automated Setup Scripts, written in Batch for Windows and in Bash for Ubuntu (Linux)
- `/src` Directory for Python Scripts and Requirements File

### Changed

- Move Python Scripts, Requirements File, and `.gitignore` File to `/src` Directory
- Cater the root `.gitignore` File for Files/Directories created by Automated Setup Scripts

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

## [0.1.0-alpha] 2025-06-02

### Added

### Changed

- Rework the code into classes and functions for easier functionality with other games and versions

### Deprecated

### Fixed

### Removed