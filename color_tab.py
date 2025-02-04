import customtkinter as ctk
import pyperclip

# i want to turn an individual color tab frame into a template that could be used four times
# this would be so i would only have to change code within a color tab once and not have to repeat it across multiple instances if that makes sense
# is this callable yet?
class ColorTab(ctk.CTkFrame):
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

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.grid()

        self.color_tab = ctk.CTkFrame(self).grid(row=0)

        self.color_info = ctk.CTkFrame(self).grid(row=0, column=1, padx=10)


class ColorTabList(ctk.CTkTabview):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.add('Primary')

        self.set('Primary')

        self.grid(row=0, column=0, padx=5)


class WindowLBP2USNormal(ctk.CTk):
    def __init__(self):
        super().__init__()

        # window setup
        self.title("LBP2 Color Generator")
        self.geometry('535x265')
        self.resizable(False, False)

        # program
        self.color_tablist = ColorTabList(self)

        self.prim_colortab = ColorTab(self)
        
        self.prim_colortab(self.color_tablist.tab('Primary'))

        self.mainloop()


def main():
    WindowLBP2USNormal()

if __name__ == '__main__':
    main()