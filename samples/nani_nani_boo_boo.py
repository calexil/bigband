#!/usr/bin/python
import pyautogui
import os
# Set a counter to count the # of exceptions occur
counter = 0

# Start the while loop
while counter < 1:
    try:
# Sleep so there is time for the script to execute after MP or satchmo
        pyautogui.time.sleep(2)
# Press and delay release of MP to start a song (This section can be removed if using for lvl 5 only
        pyautogui.keyDown('i')
        pyautogui.time.sleep(1)
        pyautogui.keyUp('i')
# Start the song, this plays lp-mp-hp-lk-mk-hk on each available scale continuously.
        pyautogui.keyDown('i')
        pyautogui.keyUp('i')
        pyautogui.keyDown('i')
        pyautogui.keyUp('i')
        pyautogui.press(['i', 'o'])
        pyautogui.press(['k', 'l'])
        pyautogui.keyDown('i')
        pyautogui.keyUp('i')
        pyautogui.press(['i', 'o'])
        pyautogui.time.sleep(1)
        counter += 1
# Exception handle 
# this section needs work and sometimes fails to function properly
    except Exception:
        print ("Oops you broke it")
        counter += 1
        print ("counter =" + str(counter))
        if counter >= 2: exit
