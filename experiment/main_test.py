#!pip install psychopy
## MAINNNNNN

# import libraries
import os
import sys
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from psychopy import gui, core, visual, event

from psychopy.gui import DlgFromDict
from psychopy.visual import Window
from psychopy.core import Clock, quit, wait
#from psychopy.event import Mouse
from psychopy.hardware import keyboard

kb = keyboard.Keyboard()
keys = kb.getKeys()
#win = visual.Window(size=[1792, 1120]) #units="pix", screen = 0, fullscr=False, allowGUI=True) #allowGUI!
win = visual.Window(size=[1512, 982]) #units="pix", screen = 0, fullscr=False, allowGUI=True) #allowGUI! # work laptop

# # get refresh rate
# refresh_r = round(win.getActualFrameRate())
# print(f"refresh rate: {refresh_r} Hz")

# circ_stim=visual.Circle(win, radius=100,units='pix', fillColor=[1, -1, -1],lineColor=[-1, -1, 1], edges=128)
# circ_stim.draw()
# win.flip()
# core.wait(3.0)


##############################################################################
# motion quartets
stimulus_size = 25
freq = 7 # ON and OFF is 1 cycle.
height=10
width=100

upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), stimulus_size+(height/2)),fillColor=[1, -1, -1],lineColor=[-1, -1, 1])
upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), stimulus_size+(height/2)),fillColor=[1, -1, -1],lineColor=[-1, -1, 1])
lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), -stimulus_size-(height/2)),fillColor=[1, -1, -1],lineColor=[-1, -1, 1])
lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), -stimulus_size-(height/2)),fillColor=[1, -1, -1],lineColor=[-1, -1, 1])
stimulix = [upper_left, upper_right, lower_right, lower_left]



message = visual.TextStim(win, text='waiting')
message.autoDraw = True  # Automatically draw every frame
win.flip()
core.wait(3.0)
message.autoDraw = False  # Automatically draw every frame


while True:

    duration = 5 # seconds
    for i in list(range(0,duration)):
    
        # 1 second
        for i in list(range(0,freq)):
        
            for i in list(range(0,3,2)):
                stimulix[i].draw()
            # stimulix[0].draw(); stimulix[1].draw(); stimulix[2].draw(); stimulix[3].draw()
            win.flip()
            core.wait((1/freq)/2)    
            
            for i in list(range(1,4,2)):
                stimulix[i].draw()
            # stimulix[0].draw(); stimulix[1].draw(); stimulix[2].draw(); stimulix[3].draw()
            win.flip()
            core.wait((1/freq)/2)  
    if len(kb.getKeys()) > 0:
        print('YESSSSSS')
        # thisKey = kb.getKeys()
        # print(thisKey)
        break
    event.clearEvents()


message = visual.TextStim(win, text='LOL')
message.autoDraw = True  # Automatically draw every frame
win.flip()
core.wait(2.0)
message.text = 'Did it work?' 
win.flip() 
core.wait(2.0)

win.close()
core.quit()



#def draw_motquarts(stimulus_size, height, width):
    
















