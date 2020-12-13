import time,win32api,win32con,pyautogui 
from positions import Positions
from key_press import press,Keys,likeLongPress,more_than_one_press

def ability_settings():
    # navigate to stamina
    more_than_one_press(Keys.DOWN,3)
    press(Keys.ENTER)
    # stamina
    likeLongPress(Keys.RIGHT,50)
    press(Keys.ENTER)
    # navigate to team work
    press(Keys.RIGHT)
    more_than_one_press(Keys.DOWN,6)
    press(Keys.ENTER)
    # team work
    likeLongPress(Keys.RIGHT,30)
    press(Keys.ENTER)
    # save
    more_than_one_press(Keys.DOWN,4)
    press(Keys.ENTER)
    


