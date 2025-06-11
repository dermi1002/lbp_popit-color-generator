# LittleBigPlanet Popit Color Generator
A Python GUI program that generates NetCheat List files to modify LittleBigPlanet Popit Color Themes

README Document written by dermi1002

# Heads Up & Remark
I'm going to be wrapping things up until I either make a new branch or make a new repository and make this one a **Public Archive.** If the former happens, support for the Python branch will be dropped. If the ladder happens, support for the whole repo will be dropped, and a link to the newer repo will be included in this document before it gets archived.

Seeing as it takes extra steps to install CustomTkinter to Linux, I figured I might as well rewrite the whole project in Lua I so can embed it to a C# Plugin for NetCheat (or Nim if I can't. Either way they would significantly reduce resource usage). The least I could do for now is retheme it to get rid of those steps for Linux, at the cost of the GUI looking a little ugly in my opinion.

# WARNING
THIS PROGRAM IS AN UNFINISHED WORK (IN PROGRESS) AND ONLY WORKS ON LBP2 US LATEST VERSION! DO NOT ATTEMPT ON OTHER GAMES OR VERSIONS!

Doing so may result in the loss of progress in your levels, profile, or even the whole game!

Please back them up before testing/using this software.

# Using the Program
If you use Windows, you can try a Package in the [Releases Page](https://github.com/dermi1002/lbp_popit-color-generator/releases).

## Building From Source
The LittleBigPlanet Popit Color Generator was tested on Windows 10 Python 3.8.0 with CustomTkinter, PyYAML, and Pyperclip. 

In order to install these libraries, create a virtual environment, and install them through this command:
```
pip install -r requirements.txt
```
Then, you can open the GUI program:
```
python main.py
```
If done correctly, you'll end up with this:

![First look of the LBP Popit Color Generator GUI](./docs/resources/main_firstlook.png)

# Documents
[How To Use](./docs/how_to_use.md)
[How NetCheat Codes Work](./docs/netcheat_pointer_codes.md)

# To-do List
### High Priority:
- [ ] Retheme the GUI to Tkinter's TTK widget to remove CustomTkinter dependency and support most Linux devices out-of-the-box
- [ ] Add a toolbar to the program

### Next:
- [ ] ~~Add functionality to change colors via hex color entry~~

### Future Considerations:
- [ ] ~~Complete and~~ polish README file
- [ ] ~~Create mock-up gameplay previews~~
- [ ] Add Terminal logs

### Completed:
- [x] ~~Rework the code into classes and functions for easier functionality with other games and versions (see the class-test branch)~~
- [x] ~~Edit code functions, values, etc., for extra readability among project contributors~~
