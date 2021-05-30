import pyautogui
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

# You have to change the path for screenshot folder.
class capture():

    def captureScreen():
        screenshot1 = pyautogui.screenshot()
        screenshot1.save(r"/Users/ray.rajnish/PycharmProjects/RightMoveStorage/POM/TakeScreenshot/Capturedscreenshots/Screenshot"+"  "+"{}".format(current_time) +".png")
        print("Current Time =", current_time)
