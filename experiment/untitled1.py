#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 16:05:29 2023

@author: pelinozsezer
"""

from psychopy.core import Clock, quit, wait
from psychopy.hardware.keyboard import Keyboard

kb=Keyboard()


wait(2)
t_init=kb.clock.getTime()
print(t_init)


keys = kb.getKeys()
# Checks if "space" in the list of keypresses and returns
# a boolean (True / False)
spacebar_pressed = "space" in keys

while True:
    keys = kb.getKeys()
    key_pressed="space" 
    if key_pressed in keys:
        break
    
print(keys.name, keys.tDown, keys.rt)


# We need to reset the clock!
kb.clock.reset()
while kb.clock.getTime() < 2:
    keys = kb.getKeys()
    for key in keys:
        # The `:.3f` part in the F-string makes sure the float is only displayed with 3 decimals!
        print(f"The '{key.name}' key was pressed within {key.rt:.3f} seconds for a total of {key.duration:.3f} seconds")
        
        
        
keyPressed = kb.waitKeys()
if keyPressed == ["space"]:
    break 
