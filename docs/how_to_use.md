# How To Use 
When you open the program, there will be five tabs, four of which are for changing color values. 

The Popit uses the first three of the values; Primary, Secondary, and Tertiary; and the fourth one, Emphasis, is used as "highlighted" text in level descriptions.

These four tabs appear in a layout like this:
- On the right are three sliders; those of which "represent" values for red, green, and blue;
- Below them is a hex color entry with a button to copy and paste outside the program; and
- On the left is a square that previews the color changed by the three sliders.

![Editing the Primary Color in the LBP Popit Color Generator GUI](./resources/main_changecolor.png)

The sliders can be dragged left to right to change the square's color and the hex color entry. 

As of now, editing the hex entry won't change the color and slider values unfortunately. Functionality for this is planned in the future.

The current color value can be copied by pressing the "Copy" Button next to the entry.

Once your done editing the color values, you can move onto the fifth tab, Export:

![Export Tab in the LBP Popit Color Generator GUI](./resources/main_export.png)

In this tab is a label that reads:

*"If you are finished with your Popit color theme, give it a Code Name and export a cheat file!"*

Below is an entry that reads Code Name. As the label said, you can click on it and type anything into it as shown below:

![Entering a Code Name in the Export Tab of the LittleBigPlanet Color Generator GUI](./resources/main_exportcodename.png)

After that, you can click on the "Save YAML Config" button to store your Popit color values in a YAML dictionary file.

Then, you can click on the "Concert to NCL" button to convert a YAML file to a .ncl NetCheat List file, which is a set of values to manipulate in a PS3 memory editor, such as NetCheat and Artemis.

First, the program will prompt you to open a YAML file. Then, it will prompt you to choose a directory to save the .ncl file. 

As of now, keeping the default directories is essential for the programs functionality.

Once you saved your .ncl file, you can import it to the PS3 memory editor of your choice and apply it in-game.
