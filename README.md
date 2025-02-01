# LittleBigPlanet Popit Color Generator
A CustomTkinter GUI program that generates NetCheat List files to modify LittleBigPlanet Popit Color Themes

# THIS PROGRAM IS A WORK IN PROGRESS AND ONLY WORKS ON LBP2 US LATEST VERSION! DO NOT ATTEMPT ON OTHER GAMES OR VERSIONS!
## Doing so may result to loss of progress in your levels, profile, or even the whole game!

## How To Use
The LittleBigPlanet Popit Color Generator was tested on WIndows 10 Python 3.8.0 with CustomTkinter, PyYAML, and Pyperclip. 

In order to install these libraries, create a virtual environment, and install them through this command:
```
pip install -r requirements.txt
```
Then, you can open the GUI program:
```
python main.py
```
If done correctly, you'll end up with this:

![First look of the LBP Popit Color Generator GUI](./.readme_pictures/main_firstlook.png)

In this window, there are five tabs, four of which are for changing color values. 

The Popit uses the first three of the values; Primary, Secondary, and Tertiary; and the fourth one, Emphasis, is used as "highlighted" text in level descriptions (and dialog bubbles (check)).

These four tabs appear in a layout like this:
- On the right are three sliders; those of which "represent" values for red, green, and blue;
- Below them is a hex color entry with a button to copy and paste outside the program; and
- On the left is a square that previews the color changed by the three sliders.

![Editing the Primary Color in the LBP Popit Color Generator GUI](./.readme_pictures/main_changecolor.png)

The sliders can be dragged left to right to change the square's color and the hex color entry. 

As of now, editing the hex entry won't change the color and slider values unfortunately. Functionality for this is planned in the future.

The current color value can be copied by pressing the "Copy" Button next to the entry.

Once your done editing the color values, you can move onto the fifth tab, Export:

![Export Tab in the LBP Popit Color Generator GUI](./.readme_pictures/main_export.png)

To be continued...

### To-do List
High Priority:
- [ ] Complete README file
- [ ] Change License to prohibit commercial usage

Next:
- [ ] Rework the code into classes and functions for easier functionality with other games and versions
- [ ] Add functionality to change colors via hex color entry

Future Considerations:
- [ ] Rework functionality to export color codes to support various LBP titles and regions
- More to add...
