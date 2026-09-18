import keyboard
import pyautogui
import webbrowser
from time import sleep

def Open(Query):
    Query = str(Query).lower()

    if "visit" in Query:
        Nameofweb = Query.replace("visit ","")
        Link = f"https://www.{Nameofweb}.com"# will open website 
        webbrowser.open(Link)
        return True

    elif "launch" in Query:
        Nameofweb = Query.replace("launch ","")
        Link = f"https://www.{Nameofweb}.com"# will open website 
        webbrowser.open(Link)
        return True

    elif "open" in Query:
        Nameofapp = Query.replace("open ","")
        pyautogui.keyDown('command')
        pyautogui.press('space')
        pyautogui.keyUp('command')
        sleep(1)
        keyboard.write(Nameofapp)
        sleep(1)
        pyautogui.press('enter')
        sleep(0.5)
        return True
    
    elif "start" in Query:
        Nameofapp = Query.replace("open ","")
        pyautogui.keyDown('command')
        pyautogui.press('space')
        pyautogui.keyUp('command')
        sleep(1)
        keyboard.write(Nameofapp)
        sleep(1)
        pyautogui.press('enter')
        sleep(0.5)
        return True
    