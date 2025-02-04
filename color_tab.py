import customtkinter as ctk
import pyperclip


class ColorTabList(ctk.CTkTabview):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs) #super(ColorTabList, self)

        self.add('Primary')
        self.add('Export')

        self.set('Primary')

        def colorTab(master):
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

            # i make a frame for the two below
            tab_frame = ctk.CTkFrame(master).grid()

            # and within that frame, i make two other frames
            color_square = ctk.CTkFrame(tab_frame).grid(row=0)

            color_info = ctk.CTkFrame(tab_frame).grid(row=0, column=1, padx=10)

            # everythin within color_square
            color_preview = ctk.CTkLabel(color_square, text='', bg_color='#000', width=200, height=200).grid(padx=5, pady=5)

            # everything within color_info
            color_sliders = ctk.CTkFrame(color_info, width=500).grid(row=0, column=0, pady=10)

            red_slider = ctk.CTkSlider(color_sliders, from_=0, to=255, width=256) #, command=change_color

        self.prim_colortab = colorTab(self.tab('Primary'))

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
