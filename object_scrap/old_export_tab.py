# Export Tab UI
export_tab = ctk.CTkFrame(self.tab('Export'))
export_text_preview = ctk.CTkLabel(
export_tab, 
text = f'If you are finished with your Popit color theme,\ngive it a Code Name and export a cheat file!', 
width = 525
)

code_caption = ctk.CTkEntry(export_tab, placeholder_text = 'Code Name')

save_yaml_button = ctk.CTkButton(
export_tab, 
text = 'Save YAML', 
command = lambda: external_objects.new_export_yaml(
    code_caption.get(),
    self.primary_colortab.color_preview.cget('background')[1:],
    self.secondary_colortab.color_preview.cget('background')[1:],
    self.tertiary_colortab.color_preview.cget('background')[1:],
    self.emphasis_colortab.color_preview.cget('background')[1:]
    )
)

save_ncl_button = ctk.CTkButton(
export_tab, 
text = 'Save NCL', 
command = lambda: external_objects.new_export_ncl(
    code_caption.get(),
    self.primary_colortab.color_preview.cget('background')[1:],
    self.secondary_colortab.color_preview.cget('background')[1:],
    self.tertiary_colortab.color_preview.cget('background')[1:],
    self.emphasis_colortab.color_preview.cget('background')[1:]
    )
)

export_text_preview.grid(row = 0, pady = 5)
code_caption.grid(row = 1, pady = 10)
save_yaml_button.grid(row = 2, pady = 10)
save_ncl_button.grid(row = 3, pady = 10)


export_tab.grid(row = 0, column = 0)