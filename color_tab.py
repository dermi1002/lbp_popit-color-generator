import customtkinter as ctk
import pyperclip


class ColorTabList(ctk.CTkTabview):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs) #super(ColorTabList, self)

        self.place_configure(width=530, height=254)

        self.add('Primary')
        self.add('Export')

        self.set('Primary')

        class ColorTab(ctk.CTkFrame):
            def __init__(self, master, *args, **kwargs):
                super().__init__(master, *args, **kwargs)
                
                def change_color(value):
                    self.R = int(self.red_slider.get())
                    self.G = int(self.green_slider.get())
                    self.B = int(self.blue_slider.get())

                    _hexprint = '%02X%02X%02X' % (self.R, self.G, self.B)

                    self.color_preview.configure(bg_color=f'#{self._hexprint}')

                    self._hexentry.delete(0, ctk.END)
                    self._hexentry.insert(0, _hexprint)

                def copy_hexentry():
                    pyperclip.copy(self._hexentry.get())


                self.color_preview = ctk.CTkLabel(master, text='', bg_color='#000', width=200, height=200).place(y=4)


                self.letter_r = ctk.CTkLabel(master, text='R').place(x=225, y=10)
                self.red_slider = ctk.CTkSlider(master, from_=0, to=255, width=256, command=change_color).place(x=260, y=16)

                self.letter_g = ctk.CTkLabel(master, text='G').place(x=225, y=60)
                self.green_slider = ctk.CTkSlider(master, from_=0, to=255, width=256, command=change_color).place(x=260, y=66)

                self.letter_b = ctk.CTkLabel(master, text='B').place(x=225, y=110)
                self.blue_slider = ctk.CTkSlider(master, from_=0, to=255, width=256, command=change_color).place(x=260, y=116)


                self._hexdisplay = ctk.CTkLabel(master, text='HEX Color:').place(x=225, y=170)
                self._hexentry = ctk.CTkEntry(master)
                self._hexcopy = ctk.CTkButton(master, text='Copy', width=50, command=copy_hexentry).place(x=450, y=170)

                self._hexentry.place(x=297, y=170)
                self._hexentry.insert(ctk.END, '000000')

        self.prim_colortab = ColorTab(self.tab('Primary'))

        self.place(x=5)

    
class WindowLBP2USNormal(ctk.CTk):
    def __init__(self):
        super().__init__()

        # window setup
        self.title("LBP2 Color Generator")
        self.geometry('540x260')
        self.resizable(False, False)

        # program
        ColorTabList(self)

        

        self.mainloop()


def main():
    WindowLBP2USNormal()

if __name__ == '__main__':
    main()
