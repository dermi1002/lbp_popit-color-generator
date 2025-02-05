import customtkinter as ctk
import pyperclip


class ColorTabList(ctk.CTkTabview):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs) #super(ColorTabList, self)

        self.add('Primary')
        self.add('Export')

        self.set('Primary')

        class ColorTab(ctk.CTkFrame):
            def __init__(self, master, *args, **kwargs):
                super().__init__(master, *args, **kwargs)
                # don't mind the functions yet
                #def change_color(value):
                #    R = int(red_slider.get())
                #    G = int(green_slider.get())
                #    B = int(blue_slider.get())

                #    _hexprint = '%02X%02X%02X' % (R, G, B)

                #    color_preview.configure(bg_color=f'#{_hexprint}')

                #    _hexentry.delete(0, ctk.END)
                #    _hexentry.insert(0, _hexprint)

                #def hex_copy():
                #    pyperclip.copy(_hexentry.get())


                # ok so it turns out that the grid system in within a function is much different than normal
                # everything still appears outside the tabview
                color_square = ctk.CTkFrame(master).grid(row=0, column=0)

                self.color_preview = ctk.CTkLabel(color_square, text='', bg_color='#000', width=200, height=200).grid(row=0, column=0, padx=5, pady=5)


                color_info = ctk.CTkFrame(master).grid(row=3, column=1, padx=10)


                color_sliders = ctk.CTkFrame(color_info).grid(row=3, column=1, pady=10)

                self.letter_r = ctk.CTkLabel(color_sliders, text='R').grid(row=0, column=1, padx=10, pady=10)
                self.red_slider = ctk.CTkSlider(color_sliders, from_=0, to=255, width=256).grid(row=0, column=2, padx=5, pady=10)

                self.letter_g = ctk.CTkLabel(color_sliders, text='G').grid(row=1, column=1, padx=10, pady=10)
                self.green_slider = ctk.CTkSlider(color_sliders, from_=0, to=255, width=256).grid(row=1, column=2, padx=5, pady=10)

                self.letter_b = ctk.CTkLabel(color_sliders, text='B').grid(row=2, column=1, padx=10, pady=10)
                self.blue_slider = ctk.CTkSlider(color_sliders, from_=0, to=255, width=256).grid(row=2, column=2, padx=5, pady=10)


                color_entries = ctk.CTkFrame(color_info).grid(row=3, column=1)

                self._hexdisplay = ctk.CTkLabel(color_entries, text='HEX Color: ').grid(row=3, column=0, padx=5)
                self._hexentry = ctk.CTkEntry(color_entries)
                self._hexcopy = ctk.CTkButton(color_entries, text='Copy', width=50).grid(row=3, column=2, padx=5)

                self._hexentry.grid(row=3, column=1)
                self._hexentry.insert(ctk.END, '000000')

        self.prim_colortab = ColorTab(self.tab('Primary'))

        self.grid(row=0, column=0, padx=5)

    
class WindowLBP2USNormal(ctk.CTk): # inherrits everything from main window right?
    def __init__(self):
        super().__init__()

        # window setup
        self.title("LBP2 Color Generator")
        self.geometry('535x265')
        #self.resizable(False, False)

        # program
        ColorTabList(self)

        

        self.mainloop()


def main():
    WindowLBP2USNormal()

if __name__ == '__main__':
    main()
