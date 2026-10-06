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
- Module to imply that certain modules used by the Main Python file aren't meant to be executed
- Functionality that interacts with the 'Code Caption' text field in the Main Python file's Export Tab class instance
- Change Log document (this file)
- Contributing document

### Changed

- Move the Export Window class from the Main Python file to its own module

- [x] Move Objects from Main Python file to their own module
- [x] Move Objects' command funcitons from Main Python to their own module

- Reformat Function names to Snake Case
- Reformat Class names to Pascal Case
- Reformat Variable names to Camel Case
- Renamed 'External Objects' Module to 'File Management'

### Deprecated

- Disable ability to open Value List (.TXT) files

### Fixed

- Added check for if Dialogs for opening files end up with a blank tuple next to None value

### Removed

## [0.4.0-alpha] 2026-09-12

### Added

- Automated Setup Scripts, written in Batch for Windows and in Bash for (Ubuntu) Linux

### Changed

- [x] Optimize Shell Script and check for errors
- [x] Change the README.md document accordingly
- [x] Add checks for Virtual Environments in both scripts
- [x] Wrap Instruction Sequences into Functions in Ubuntu Script
- [x] Add checks for the Main Python file in both scripts

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