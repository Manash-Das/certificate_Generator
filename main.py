import os
import sys
import tkinter as tk
from tkinter import filedialog as fd

import cv2.cv2 as cp
import numpy as np
from PIL import ImageFont, ImageDraw, Image

from certificate_generator import writeName
from select_cood import getCod

target_path = ''
name_path = ''
cer_path = ''
text_path = "C:\\Windows\\Fonts"
text = []
font_type = ''
font_size = 30
cord = (0, 0)
if os.path.exists:
    for file in os.listdir(text_path):
        if file.endswith(".ttf"):
            text.append(file)
else:
    sys.exit(1)


def getCorrected(x):
    global font_type, font_size
    font_size = text_size_scale.get()
    font_type = text_path + "\\" + menu.get()
    image = cp.imread(cer_path)
    image = cp.cvtColor(image, cp.COLOR_BGR2RGB)
    pilImage = Image.fromarray(image)
    draw = ImageDraw.Draw(pilImage)
    font = ImageFont.truetype(font_type, font_size)
    draw.text((cord[0] + x_scale.get(), cord[1] + y_scale.get()), "Manash Das", font=font, fill='black')
    opencvImage = cp.cvtColor(np.array(pilImage), cp.COLOR_RGB2BGR)
    cp.imshow("Display", opencvImage)


def chooseFile(file_type):
    global cord, cer_path, name_path, target_path
    if file_type == 'Certificate':
        cer_path = fd.askopenfilename()
        v1.set(cer_path)
    elif file_type == 'Name':
        name_path = fd.askopenfilename()
        v2.set(name_path)
    elif file_type == 'Save':
        target_path = fd.askdirectory()
        v3.set(target_path)
    else:
        if v1.get() =='' or v2.get()=='' or v3.get()=='':
            return
        cord = getCod(cer_path)
        root.quit()


def onchange():
    coordinate = (cord[0] + x_scale.get(), cord[1] + y_scale.get())
    root.destroy()
    cp.destroyWindow("Display")
    writeName(cer_path, coordinate, name_path, target_path, font_size, font_type)


root = tk.Tk()
root.title("Certificate Generator")
v1 = tk.StringVar()
v2 = tk.StringVar()
v3 = tk.StringVar()
cer_btn = tk.Button(root, text="Upload certificate", command=lambda: chooseFile("Certificate")).grid(row=0, column=0)
cer_label = tk.Entry(root, text="", width=50, textvariable=v1).grid(row=0, column=1)

name_btn = tk.Button(root, text="Upload names", command=lambda: chooseFile("Name")).grid(row=1, column=0)
name_label = tk.Entry(root, text="", width=50, textvariable=v2).grid(row=1, column=1)

Output_btn = tk.Button(root, text="Save", command=lambda: chooseFile("Save")).grid(row=2, column=0)
Output_label = tk.Entry(root, text="", width=50, textvariable=v3).grid(row=2, column=1)

tk.Button(root, text="Get coordinate", command=lambda: chooseFile("Done")).grid(row=3, column=0)

root.mainloop()
root.destroy()

################# For second Process ################
root = tk.Tk()
root.geometry('500x300')

################ Select text Size ###################
text_size_scale = tk.Scale(root, from_=1, to_=100, command=getCorrected, orient=tk.HORIZONTAL, label="Text Size",length=600)
text_size_scale.set(font_size)
text_size_scale.pack(anchor=tk.CENTER)

############### Moving text x_axis ################
x_scale = tk.Scale(root, from_=-100, to_=100, command=getCorrected, orient=tk.HORIZONTAL, label="x_axis", length=600)
x_scale.set(0)
x_scale.pack(anchor=tk.CENTER)

############### Moving text y_axis ################
y_scale = tk.Scale(root, from_=-100, to_=100, command=getCorrected, orient=tk.HORIZONTAL, label="y_axis", length=600)
y_scale.set(-font_size)
y_scale.pack(anchor=tk.CENTER)

############## Select Text ##################
menu = tk.StringVar()
menu.set(text[10])
drop = tk.OptionMenu(root, menu, *text, command=getCorrected)
drop.pack()

############# Button for completition #############
done_btn = tk.Button(root, text="Done", command=onchange)
done_btn.pack()

############## Reading the  image ##################
getCorrected(10)
root.mainloop()
