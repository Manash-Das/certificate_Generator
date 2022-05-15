import tkinter as tk
from tkinter import filedialog as fd
import cv2.cv2 as cp
from select_cood import getCod
from certificate_generator import writeName
def getCorrected(x):
    try:
        x = cp.getTrackbarPos("Scale", "Scaling")/10
    except cp.error:
        x = 1
    try:
        y = cp.getTrackbarPos("Thickness", "Scaling")
    except cp.error:
        y = 2
    try:
        z = cp.getTrackbarPos("Text", "Scaling")
    except cp.error:
        z = 0
    image = cp.imread(cer_path)
    cp.putText(image, "MANASH DAS", cord, text[z], x, (0, 0, 0), y)
    print(text[z])
    cp.imshow("certificate", image)


def chooseFile(type):
    global cord, cer_path,name_path,target_path
    if type == 'Certificate':
        cer_path = fd.askopenfilename()
    elif type == 'Name':
        name_path = fd.askopenfilename()
    elif type =='Save':
        target_path = fd.askdirectory()
    else:
        cord = getCod(cer_path)
        root.destroy()


def onchange(x):
    if x==1:
        writeName(cer_path,cord,name_path,target_path)


target_path = ''
font_path = ''
name_path = ''
cer_path = ''
cord = (0, 0)
root = tk.Tk()
root.title("Certificate Generator")
cer_btn = tk.Button(root, text="Upload certificate", command=lambda: chooseFile("Certificate"))
cer_btn.grid(row=0, column=0)
name_btn = tk.Button(root, text="Upload names", command=lambda: chooseFile("Name"))
name_btn.grid(row=1, column=0)
name_btn = tk.Button(root, text="Save", command=lambda: chooseFile("Save"))
name_btn.grid(row=2, column=0)
name_btn = tk.Button(root, text="Get coordinate", command=lambda: chooseFile("Done"))
name_btn.grid(row=3, column=0)
root.mainloop()
cp.destroyAllWindows()

text = [cp.FONT_HERSHEY_SIMPLEX,cp.FONT_HERSHEY_PLAIN,cp.FONT_HERSHEY_DUPLEX,cp.FONT_HERSHEY_COMPLEX,
        cp.FONT_HERSHEY_TRIPLEX,cp.FONT_HERSHEY_COMPLEX_SMALL,cp.FONT_HERSHEY_SCRIPT_SIMPLEX,
        cp.FONT_HERSHEY_SCRIPT_COMPLEX]

cp.namedWindow("Scaling")
cp.resizeWindow("Scaling",300,200)
image = cp.imread(cer_path)
cp.putText(image, "MANASH DAS", cord, cp.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0), 1)
cp.imshow("certificate", image)

cp.createTrackbar("Scale", "Scaling", 2, 20, getCorrected)
cp.createTrackbar("Thickness", "Scaling", 2, 20, getCorrected)
cp.createTrackbar("Text", "Scaling", 3, 7, getCorrected)
cp.createTrackbar("Completed", "Scaling", 0, 1, onchange)



cp.waitKey(0)
cp.destroyAllWindows()