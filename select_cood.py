import cv2.cv2 as cv
import tkinter as tk
from PIL import ImageFont
confirmation = '0'
coord = (0,0)

def setField(value,win):
    global confirmation
    confirmation = value
    win.quit()


def popMessage():
    win = tk.Tk()
    win.title("confirmation")
    label = tk.Label(win, text="Please confirm this coordinates")
    label.pack(side="top", fill="x",pady=10)
    b1 = tk.Button(win, text="Agree", command=lambda: setField("1",win))
    b1.pack()
    b2 = tk.Button(win, text="Disagree", command=lambda: setField("-1",win))
    b2.pack()
    print("pop message", confirmation)
    win.mainloop()
    win.destroy()


def getCod(path):
    def draw_circle(event,x,y,flags,param):
        if event == cv.EVENT_LBUTTONDBLCLK:
            cv.putText(img,"MANASH DAS", (x, y),cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 0), 2)   #SELECT LOCATION OF TEXT(TRIAL & ERROR)
            cv.imshow('Double click where you want to place the text', img)
            popMessage()
            global coord
            coord = x, y

    img = cv.imread(path)
    cv.imshow('Double click where you want to place the text', img)
    cv.setMouseCallback('Double click where you want to place the text',draw_circle)
    while True:
        print(confirmation)
        if (cv.waitKey(10) and 0xFF == 27) or confirmation == '1':   #Press Escape Key to terminate window
            break
    cv.destroyAllWindows()
    return coord

