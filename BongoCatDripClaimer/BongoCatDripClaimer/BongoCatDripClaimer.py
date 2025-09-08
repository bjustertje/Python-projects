import pyautogui
import time
from datetime import datetime
from PIL import ImageGrab
from tkinter import *
import threading

# Create root window
root = Tk()
root.title("Bongo Cat Auto Drip Claimer")
root.geometry('750x400')

# Add content
label1 = Label(root, text="Not drippy yet.")
label1.grid()

programStarted = False
checker_thread = None  # Keep track of the thread

# Pixel info
treasureColor = (147, 100, 89)
x, y = 3145, 55

def pixel_checker():
    print("Checking for loot...")
    global programStarted
    while programStarted:  # Only run while programStarted is True
        pixel_color = ImageGrab.grab(bbox=(x, y, x+1, y+1)).getpixel((0, 0))
        if pixel_color == treasureColor:
            pyautogui.click(x, y)
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Drip auto claimed on: ", current_time)
        time.sleep(0.5)

def btnClicked():
    global programStarted, checker_thread
    programStarted = not programStarted
    if programStarted:
        label1.configure(text="Drip claimer is currently running. Very drippy.")
        btn.configure(text="Stop Drip Claimer")
        # Start a new thread only if none is running
        if checker_thread is None or not checker_thread.is_alive():
            checker_thread = threading.Thread(target=pixel_checker, daemon=True)
            checker_thread.start()
    else:
        label1.configure(text="Not drippy yet.")
        btn.configure(text="Start Drip Claimer")

btn = Button(root, text="Start Drip Claimer", fg="red", command=btnClicked)
btn.grid(column=1, row=0)

root.mainloop()