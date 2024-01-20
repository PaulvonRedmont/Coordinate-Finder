import pyautogui
import time

#Wait for a few seconds to give you time to move the mouse
X = True

while X == True:
    time.sleep(0.001)
    current_mouse_position = pyautogui.position()
    print("Mouse Position:", current_mouse_position)
