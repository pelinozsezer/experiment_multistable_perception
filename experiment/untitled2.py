#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 17:34:45 2023

@author: pelinozsezer
"""

from psychopy import core, event, visual, monitors

mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(monitor=mon, size=(400,400), color=[-1,-1,-1])

nTrials=5
my_text=visual.TextStim(win)
fix=visual.TextStim(win, text='+')

for trial in range(nTrials):
    
    keys = event.getKeys(keyList=['z','m']) #put getkeys HERE
    my_text.text = "trial %i" %trial #insert integer into the string with %i
    
    fix.draw()
    win.flip()
    core.wait(2)
    
    event.clearEvents() #clear events HERE
    
    my_text.draw()
    win.flip()
    core.wait(1)
    
    print(keys) #which keys were pressed?
    
win.close()