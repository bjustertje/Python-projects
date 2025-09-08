import pyautogui

def checkSizePos(): 
    wh = pyautogui.size()
    print(wh)

    pos = pyautogui.position()
    print(pos)

    # Get pixel color
    pixel_color = pyautogui.pixel(x=3145, y=55)
    print(pixel_color)

checkSizePos()