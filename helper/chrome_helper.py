import time
import pyautogui
import os


def open_youtube_on_google_chrome():
    os.system('open -na "Google Chrome" --args -incognito "www.youtube.com"')
    # webbrowser.open("https://www.youtube.com/")
    time.sleep(2)
    pyautogui.moveTo(1060, 690, 1)
    pyautogui.click()
    pyautogui.hotkey('Command', 'ctrl', 'f')
    time.sleep(2)

def reload_page():
    pyautogui.hotkey('Command', 'r')
    pyautogui.click()


def click_submit():
    pyautogui.moveTo(1620, 275, 0.001)
    pyautogui.click()
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.press("enter")



def open_channel_name_and_search(channel_name):
    pyautogui.moveTo(1020, 150, 1)
    pyautogui.click()
    pyautogui.write(channel_name)
    pyautogui.press("enter")


def subscribe_channel():
    pyautogui.moveTo(1570, 300, 1)
    pyautogui.click()


def unsubscribe_channel():
    pyautogui.moveTo(1060, 690, 1)
    # pyautogui.moveTo(1090, 690, 1)
    pyautogui.click()


def close_youtube_tab():
    time.sleep(2)
    pyautogui.hotkey('command', 'w')


def logout_youtube():
    pyautogui.moveTo(1860, 150, 1)
    pyautogui.click()
    pyautogui.moveTo(1860, 450, 1)
    pyautogui.click()


def signup_youtube():
    pyautogui.moveTo(1860, 140, 1)
    pyautogui.click()
    pyautogui.moveTo(960, 600, 1)
    pyautogui.click()


def login_youtube():
    pyautogui.moveTo(1860, 140, 1)
    pyautogui.click()
    pyautogui.moveTo(960, 600, 1)
    pyautogui.click()


def enter_login_credential(username, password):
    pyautogui.moveTo(960, 600, 1)
    pyautogui.click()
    pyautogui.write(username)
    pyautogui.press("enter")
    pyautogui.moveTo(960, 600, 1)
    pyautogui.write(password)
    pyautogui.press("enter")
    time.sleep(2)
