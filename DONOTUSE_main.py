# THIS SCRIPT IS A WIP DO NOT USE IT YET!

import customtkinter as ctk
import window_lbp2


def close_test():
    on_closing = ctk.CTkInputDialog(title='Close Program', text='is this even the right one?') #anything here

def lbp2_open():
    # call a script from here
    window_lbp2.main()
    # something to make the main script uncloseable until the lbp2 window closes


def main():
    # window config
    app = ctk.CTk()
    app.title('LittleBigPlanet Popit Color Generator')

    # program
    welcome_wip = ctk.CTkLabel(app, text='Welcome to the LittleBigPlanet Popit Color Generator, home of the pure customization of Sackboy\'s ultimate tool.\n\nUnfortunately, this is only a Work In Progress as functionality for LBP2 US Normal Edition only works in this program.\n\nBut if you want to help, you can go to the GitHub repository, scroll to the bottom of the README.md document\nin a section briefly talking about how cheat codes work, follow it with caution, and tell us in the repository\'s issues!').grid(padx=20, pady=20)

    goto_lbp2 = ctk.CTkButton(app, text='Open LBP2 Window', command=lbp2_open).grid(row=1, pady=10)

    dialog_test = ctk.CTkButton(app, command=close_test).grid(row=2)

    app.mainloop()

if __name__ == '__main__':
    main()
