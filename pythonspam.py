import pyautogui
import time
import webbrowser as wb

wb.open("https://web.whatsapp.com/")
time.sleep(45)

for i in range(70):
    pyautogui.write("spam")
    pyautogui.press("enter")
