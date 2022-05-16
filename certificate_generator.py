from PIL import ImageFont, ImageDraw, Image
import tkinter as tk
import tkinter.ttk as tkk


def writeName(certificate_path, coordinates, name_path,target_folder,font_size,font_type):
    root = tk.Tk()
    f = open(name_path, 'r')
    names_list = f.read().split("\n")
    progress = tkk.Progressbar(root, orient="horizontal", length=400, mode='determinate')
    progress['value'] = 10*1
    value = 200.00/float(len(names_list))
    progress["maximum"] = 200
    progress.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
    progress.start()
    root.update_idletasks()
    progress['value'] += 0
    for name_to_print in names_list:
        image = Image.open(certificate_path)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(font_type, font_size)
        draw.text(coordinates, name_to_print, font=font, fill='black')
        image.save(target_folder+"/"+name_to_print+".png")
        progress.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
        progress.start()
        root.update_idletasks()
        progress['value'] += value
        print(progress["value"])
    root.destroy()
