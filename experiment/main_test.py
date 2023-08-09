

## MAINNNNNN
##############################################################################
# import libraries
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from psychopy import core, visual, event

from psychopy.gui import DlgFromDict
from psychopy.visual import Window
from psychopy.core import Clock, quit, wait
#from psychopy.event import Mouse
#from psychopy.hardware.keyboard import Keyboard


win = visual.Window(size=[1792, 1120]) #units="pix", screen = 0, fullscr=False, allowGUI=True) #allowGUI!

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
#speed = 5 # frames per second
height=10
width=30

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





for i in list(range(0,3,2)):
    stimulix[i].draw()
# stimulix[0].draw(); stimulix[1].draw(); stimulix[2].draw(); stimulix[3].draw()
win.flip()
core.wait(0.5)    

for i in list(range(1,4,2)):
    stimulix[i].draw()
# stimulix[0].draw(); stimulix[1].draw(); stimulix[2].draw(); stimulix[3].draw()
win.flip()
core.wait(0.5)  



message = visual.TextStim(win, text='LOL')
message.autoDraw = True  # Automatically draw every frame
win.flip()
core.wait(2.0)
message.text = 'Did it work?' 
win.flip() 
core.wait(2.0)

win.close()
core.quit()


















