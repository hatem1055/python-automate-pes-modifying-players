import time,win32api,win32con,pyautogui 
from positions import Positions
from key_press import press,Keys,more_than_one_press
from basic_seetings import basic_settings
from ability_settings import ability_settings

def open_pes():
    pyautogui.click(Positions.pes[0],Positions.pes[1])

def save_player_and_go_to_the_next_one():
    more_than_one_press(Keys.DOWN,6)
    press(Keys.ENTER)
    press(Keys.DOWN)
#main
def main(number_of_playres):
    '''
    cant done automatic : injury,
    needs cheeking : age
    '''
    open_pes()
    for _ in range(0,number_of_playres):
        #navigate to basic settings
        press(Keys.ENTER)
        press(Keys.DOWN)
        press(Keys.ENTER)
        #basic settings
        basic_settings()
        #navigate to abillity settings
        more_than_one_press(Keys.DOWN,2)
        press(Keys.ENTER)
        # ability settings
        ability_settings()
        #save
        save_player_and_go_to_the_next_one()

    
if __name__ == "__main__":
    main(23)

