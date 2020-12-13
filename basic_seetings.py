import time,win32api,win32con,pyautogui 
from positions import Positions
from key_press import press,Keys,more_than_one_press

def basic_settings():
    modify_age()

    #navigate to basic settings
    more_than_one_press(Keys.DOWN,3)
    growth_type()
    save_basic_settings()

def modify_age():
    press(Keys.ENTER)
    more_than_one_press(Keys.LEFT,4)
    press(Keys.ENTER)

def growth_type():
    press(Keys.ENTER)
    more_than_one_press(Keys.UP,2)
    press(Keys.ENTER)

def save_basic_settings():
    press(Keys.DOWN)
    press(Keys.ENTER)
