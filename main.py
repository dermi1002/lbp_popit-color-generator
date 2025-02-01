import os
import yaml
import customtkinter as ctk
import pyperclip # other than copying hex values, i don't know what else to use this for. i might as well get rid of the function.

def main():
    app = ctk.CTk()
    app.title("LBP2 Color Generator")
    app.geometry('535x265')
    app.resizable(False, False)

    color_tabs = ctk.CTkTabview(app)
    color_tabs.grid(row=0, column=0, padx=5)

    color_tabs.add('Primary')
    color_tabs.add('Secondary')
    color_tabs.add('Tertiary')
    color_tabs.add('Emphasis')
    color_tabs.add('Export')
    color_tabs.set('Primary')

    #Primary Color
    def change_primcolor(value):
        # get RGB values from sliders
        primR = int(primred_slider.get())
        primG = int(primgreen_slider.get())
        primB = int(primblue_slider.get())

        # convert to hex value
        prim_hexprint = '%02X%02X%02X' % (primR, primG, primB)

        # display hex value on color square
        primcolor_preview.configure(bg_color=f'#{prim_hexprint}')

        # change text in the hex color entry
        prim_hexentry.delete(0, ctk.END)
        prim_hexentry.insert(0, prim_hexprint)

    def primhex_copy(): # the only use of pyperclip ever
        pyperclip.copy(prim_hexentry.get())

    # tab layout
    primframe = ctk.CTkFrame(color_tabs.tab('Primary'))
    primframe.grid(row=0, column=0)

    primcolor_tab = ctk.CTkFrame(primframe)
    primcolor_tab.grid(row=0)

    primcolor_info = ctk.CTkFrame(primframe)
    primcolor_info.grid(row=0, column=1, padx=10)

    primcolor_sliders = ctk.CTkFrame(primcolor_info, width=500)
    primcolor_sliders.grid(row=0, column=0, pady=10)

    primcolor_entries = ctk.CTkFrame(primcolor_info)
    primcolor_entries.grid(row=1, column=0)


    primcolor_preview = ctk.CTkLabel(primcolor_tab, text='', bg_color='#000', width=200, height=200)
    primcolor_preview.grid(padx=5, pady=5)


    primletter_r = ctk.CTkLabel(primcolor_sliders, text='R')
    primred_slider = ctk.CTkSlider(primcolor_sliders, from_=0, to=255, width=256, command=change_primcolor)

    primletter_g = ctk.CTkLabel(primcolor_sliders, text='G')
    primgreen_slider = ctk.CTkSlider(primcolor_sliders, from_=0, to=255, width=256, command=change_primcolor)

    primletter_b = ctk.CTkLabel(primcolor_sliders, text='B')
    primblue_slider = ctk.CTkSlider(primcolor_sliders, from_=0, to=255, width=256, command=change_primcolor)

    primletter_r.grid(row=0, padx=10, pady=10)
    primred_slider.grid(row=0, column=1, padx=5, pady=10)
    primletter_g.grid(row=1, padx=10, pady=10)
    primgreen_slider.grid(row=1, column=1, padx=5, pady=10)
    primletter_b.grid(row=2, padx=10, pady=10)
    primblue_slider.grid(row=2, column=1, padx=5, pady=10)


    prim_hexdisplay = ctk.CTkLabel(primcolor_entries, text='HEX Color: ')
    prim_hexentry = ctk.CTkEntry(primcolor_entries)
    prim_hexcopy = ctk.CTkButton(primcolor_entries, text='Copy', width=50, command=primhex_copy)

    prim_hexdisplay.grid(row=0, column=0, padx=5)
    prim_hexentry.grid(row=0, column=1)
    prim_hexentry.insert(ctk.END, '000000')
    prim_hexcopy.grid(row=0, column=2, padx=5)


    # duplicated code 3 times and changed names of variables, functions, and widgets for different color values.
    # i'm wondering if that was necessary. i'm strongly considering converting everything into a class or function.
    # Secondary Color
    def change_seccolor(value):
        secR = int(secred_slider.get())
        secG = int(secgreen_slider.get())
        secB = int(secblue_slider.get())

        sec_hexprint = '%02X%02X%02X' % (secR, secG, secB)

        seccolor_preview.configure(bg_color=f'#{sec_hexprint}')

        sec_hexentry.delete(0, ctk.END)
        sec_hexentry.insert(0, sec_hexprint)

    def sechex_copy():
        pyperclip.copy(sec_hexentry.get())
        
    secframe = ctk.CTkFrame(color_tabs.tab('Secondary'))
    secframe.grid(row=0, column=0)

    seccolor_tab = ctk.CTkFrame(secframe)
    seccolor_tab.grid(row=0)

    seccolor_info = ctk.CTkFrame(secframe)
    seccolor_info.grid(row=0, column=1, padx=10)

    seccolor_sliders = ctk.CTkFrame(seccolor_info, width=500)
    seccolor_sliders.grid(row=0, column=0, pady=10)

    seccolor_entries = ctk.CTkFrame(seccolor_info)
    seccolor_entries.grid(row=1, column=0)


    seccolor_preview = ctk.CTkLabel(seccolor_tab, text='', bg_color='#000', width=200, height=200)
    seccolor_preview.grid(padx=5, pady=5)


    secletter_r = ctk.CTkLabel(seccolor_sliders, text='R')
    secred_slider = ctk.CTkSlider(seccolor_sliders, from_=0, to=255, width=256, command=change_seccolor)

    secletter_g = ctk.CTkLabel(seccolor_sliders, text='G')
    secgreen_slider = ctk.CTkSlider(seccolor_sliders, from_=0, to=255, width=256, command=change_seccolor)

    secletter_b = ctk.CTkLabel(seccolor_sliders, text='B')
    secblue_slider = ctk.CTkSlider(seccolor_sliders, from_=0, to=255, width=256, command=change_seccolor)

    secletter_r.grid(row=0, padx=10, pady=10)
    secred_slider.grid(row=0, column=1, padx=5, pady=10)
    secletter_g.grid(row=1, padx=10, pady=10)
    secgreen_slider.grid(row=1, column=1, padx=5, pady=10)
    secletter_b.grid(row=2, padx=10, pady=10)
    secblue_slider.grid(row=2, column=1, padx=5, pady=10)


    sec_hexdisplay = ctk.CTkLabel(seccolor_entries, text='HEX Color: ')
    sec_hexentry = ctk.CTkEntry(seccolor_entries)
    sec_hexcopy = ctk.CTkButton(seccolor_entries, text='Copy', width=50, command=sechex_copy)

    sec_hexdisplay.grid(row=0, column=0, padx=5)
    sec_hexentry.grid(row=0, column=1)
    sec_hexentry.insert(ctk.END, '000000')
    sec_hexcopy.grid(row=0, column=2, padx=5)


    #Tertiary Color
    def change_tertcolor(value):
        tertR = int(tertred_slider.get())
        tertG = int(tertgreen_slider.get())
        tertB = int(tertblue_slider.get())

        tert_hexprint = '%02X%02X%02X' % (tertR, tertG, tertB)

        tertcolor_preview.configure(bg_color=f'#{tert_hexprint}')

        tert_hexentry.delete(0, ctk.END)
        tert_hexentry.insert(0, tert_hexprint)

    def terthex_copy():
        pyperclip.copy(tert_hexentry.get())
        
    tertframe = ctk.CTkFrame(color_tabs.tab('Tertiary'))
    tertframe.grid(row=0, column=0)

    tertcolor_tab = ctk.CTkFrame(tertframe)
    tertcolor_tab.grid(row=0)

    tertcolor_info = ctk.CTkFrame(tertframe)
    tertcolor_info.grid(row=0, column=1, padx=10)

    tertcolor_sliders = ctk.CTkFrame(tertcolor_info, width=500)
    tertcolor_sliders.grid(row=0, column=0, pady=10)

    tertcolor_entries = ctk.CTkFrame(tertcolor_info)
    tertcolor_entries.grid(row=1, column=0)


    tertcolor_preview = ctk.CTkLabel(tertcolor_tab, text='', bg_color='#000', width=200, height=200)
    tertcolor_preview.grid(padx=5, pady=5)


    tertletter_r = ctk.CTkLabel(tertcolor_sliders, text='R')
    tertred_slider = ctk.CTkSlider(tertcolor_sliders, from_=0, to=255, width=256, command=change_tertcolor)

    tertletter_g = ctk.CTkLabel(tertcolor_sliders, text='G')
    tertgreen_slider = ctk.CTkSlider(tertcolor_sliders, from_=0, to=255, width=256, command=change_tertcolor)

    tertletter_b = ctk.CTkLabel(tertcolor_sliders, text='B')
    tertblue_slider = ctk.CTkSlider(tertcolor_sliders, from_=0, to=255, width=256, command=change_tertcolor)

    tertletter_r.grid(row=0, padx=10, pady=10)
    tertred_slider.grid(row=0, column=1, padx=5, pady=10)
    tertletter_g.grid(row=1, padx=10, pady=10)
    tertgreen_slider.grid(row=1, column=1, padx=5, pady=10)
    tertletter_b.grid(row=2, padx=10, pady=10)
    tertblue_slider.grid(row=2, column=1, padx=5, pady=10)


    tert_hexdisplay = ctk.CTkLabel(tertcolor_entries, text='HEX Color: ')
    tert_hexentry = ctk.CTkEntry(tertcolor_entries)
    tert_hexcopy = ctk.CTkButton(tertcolor_entries, text='Copy', width=50, command=terthex_copy)

    tert_hexdisplay.grid(row=0, column=0, padx=5)
    tert_hexentry.grid(row=0, column=1)
    tert_hexentry.insert(ctk.END, '000000')
    tert_hexcopy.grid(row=0, column=2, padx=5)


    #Emphasis Color
    def change_emphcolor(value):
        emphR = int(emphred_slider.get())
        emphG = int(emphgreen_slider.get())
        emphB = int(emphblue_slider.get())

        emph_hexprint = '%02X%02X%02X' % (emphR, emphG, emphB)

        emphcolor_preview.configure(bg_color=f'#{emph_hexprint}')

        emph_hexentry.delete(0, ctk.END)
        emph_hexentry.insert(0, emph_hexprint)

    def emphhex_copy():
        pyperclip.copy(emph_hexentry.get())
        
    emphframe = ctk.CTkFrame(color_tabs.tab('Emphasis'))
    emphframe.grid(row=0, column=0)

    emphcolor_tab = ctk.CTkFrame(emphframe)
    emphcolor_tab.grid(row=0)

    emphcolor_info = ctk.CTkFrame(emphframe)
    emphcolor_info.grid(row=0, column=1, padx=10)

    emphcolor_sliders = ctk.CTkFrame(emphcolor_info, width=500)
    emphcolor_sliders.grid(row=0, column=0, pady=10)

    emphcolor_entries = ctk.CTkFrame(emphcolor_info)
    emphcolor_entries.grid(row=1, column=0)


    emphcolor_preview = ctk.CTkLabel(emphcolor_tab, text='', bg_color='#000', width=200, height=200)
    emphcolor_preview.grid(padx=5, pady=5)


    emphletter_r = ctk.CTkLabel(emphcolor_sliders, text='R')
    emphred_slider = ctk.CTkSlider(emphcolor_sliders, from_=0, to=255, width=256, command=change_emphcolor)

    emphletter_g = ctk.CTkLabel(emphcolor_sliders, text='G')
    emphgreen_slider = ctk.CTkSlider(emphcolor_sliders, from_=0, to=255, width=256, command=change_emphcolor)

    emphletter_b = ctk.CTkLabel(emphcolor_sliders, text='B')
    emphblue_slider = ctk.CTkSlider(emphcolor_sliders, from_=0, to=255, width=256, command=change_emphcolor)

    emphletter_r.grid(row=0, padx=10, pady=10)
    emphred_slider.grid(row=0, column=1, padx=5, pady=10)
    emphletter_g.grid(row=1, padx=10, pady=10)
    emphgreen_slider.grid(row=1, column=1, padx=5, pady=10)
    emphletter_b.grid(row=2, padx=10, pady=10)
    emphblue_slider.grid(row=2, column=1, padx=5, pady=10)


    emph_hexdisplay = ctk.CTkLabel(emphcolor_entries, text='HEX Color: ')
    emph_hexentry = ctk.CTkEntry(emphcolor_entries)
    emph_hexcopy = ctk.CTkButton(emphcolor_entries, text='Copy', width=50, command=emphhex_copy)

    emph_hexdisplay.grid(row=0, column=0, padx=5)
    emph_hexentry.grid(row=0, column=1)
    emph_hexentry.insert(ctk.END, '000000')
    emph_hexcopy.grid(row=0, column=2, padx=5)

    # YAML/NCL Export
    #functions
    def color_export():
        config_export = ctk.filedialog.asksaveasfile(initialdir="./save", filetypes=(("YAML Configuration", "*.yaml"), ("All Files", "*.*")), defaultextension='.yaml')
        if config_export is None:
            return
        color_config = str(f'color-code:\n  caption: \"{code_caption.get()}\"\n  primcolor: \"{prim_hexentry.get()}\"\n  primopacity: \"FF\"\n  seccolor: \"{sec_hexentry.get()}\"\n  secopacity: \"FF\"\n  tertcolor: \"{tert_hexentry.get()}\"\n  tertopacity: \"FF\"\n  emphcolor: \"{emph_hexentry.get()}\"\n  emphopacity: \"FF\"\n  save: \"export\\\\\"')
        config_export.write(color_config)
        config_export.close()


    def color_convert():
        yaml_set = ctk.filedialog.askopenfilename(initialdir="./save")
        if yaml_set is None:
            return
        fo = open("color_path.yaml", "w")
        fo.truncate(0)
        fo.write(
            "color-path:\n" + 
            "  set-yaml: " + "\"" + str(yaml_set) + "\"" # path to recently saved color yaml file
        )
        fo.close()

    def service_test():
        color_convert()
        
        with open ("color_path.yaml", 'r') as path_set:
            current_yaml = yaml.safe_load(path_set)

        current_color = current_yaml['color-path']

        with open (current_color['set-yaml'], 'r') as file:
            config = yaml.safe_load(file)

        db_config = config['color-code']


        # this should really be called game region but i'm not changing this variable for now
        player_id = "00DC5E8C"

        profile_id_1 = ["00000000", "00000004", "00000008", "0000000C"]

        _zeroes = "0 00000000 "

        ncl_save = ctk.filedialog.asksaveasfile(initialdir="export", filetypes=[("NetCheat List File", "*.ncl"), ("All Files", "*.*")], defaultextension=".ncl")
        if ncl_save is None:
            return
        color_code = str(
            db_config['caption'] + '\n' + '0\n' + 
            '6 ' + player_id + ' ' + profile_id_1[0] + '\n' + 
            _zeroes + db_config['primopacity'] + db_config['primcolor'] + '\n' + 
            '6 ' + player_id + ' ' + profile_id_1[1] + '\n' + 
            _zeroes + db_config['secopacity'] + db_config['seccolor'] + '\n' + 
            '6 ' + player_id + ' ' + profile_id_1[2] + '\n' + 
            _zeroes + db_config['tertopacity'] + db_config['tertcolor'] + '\n' + 
            '6 ' + player_id + ' ' + profile_id_1[3] + '\n' + 
            _zeroes + db_config['emphopacity'] + db_config['emphcolor'] + '\n' + '#\n'
            )
        ncl_save.write(color_code)
        ncl_save.close()

    #tab here
    expframe = ctk.CTkFrame(color_tabs.tab('Export'))
    expframe.grid(row=0, column=0)

    exp_text_preview = ctk.CTkLabel(expframe, text=f'If you are finished with your Popit color theme,\ngive it a Code Name and export a cheat file!', width=525)

    exp_text_preview.grid(row=0, pady=5)

    code_caption = ctk.CTkEntry(expframe, placeholder_text='Code Name')

    _savebutton = ctk.CTkButton(expframe, text='Save YAML Config', command=color_export)

    _exportbutton = ctk.CTkButton(expframe, text="Convert to NCL", command=service_test)

    code_caption.grid(row=1, pady=10)
    _savebutton.grid(row=2, pady=10)
    _exportbutton.grid(row=3, pady=10)
    app.mainloop()

if __name__ == '__main__':
    main()