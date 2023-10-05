
# Pelin Ozsezer - 5th Oct 2023

## Experiment for Single Motion Quartet ##

# import libraries
#!pip install psychopy
import os
import sys
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from psychopy import gui, core, visual, event
from psychopy.gui import DlgFromDict
from psychopy.core import Clock, quit, wait
from psychopy.visual import Window
from psychopy.hardware import keyboard

# TO-ADD
# 1) key response change (key release & other key press)- AR - time 
# 2) add def like 'draw_motion_quartet(stimulus_size, freq, height, width)'

# COLORS
color_gray=[0,0,0]
color_quartets=[0.9, 0.9, 0.9] # close to white

# window settings
#win = visual.Window(size=[1792, 1120], color=color_gray) #units="pix", screen = 0, fullscr=False, allowGUI=True # personal laptop
win = visual.Window(size=[1512, 982], color=color_gray) #units="pix", screen = 0, fullscr=False, allowGUI=True # work laptop

# # get refresh rate
# refresh_r = round(win.getActualFrameRate())
# print(f"refresh rate: {refresh_r} Hz")

# keyboard settings
kb = keyboard.Keyboard()
keys = kb.getKeys(['z', 'm', 'space'], waitRelease=True)

# PARAMETERS
scaler=4

# MQ parameters
stimulus_size = 10*scaler
freq = 2 # 1 cycle or freq is when all the quartets have been shown.
# height
# width

# Values for extending horizontally
width_val = []
current_value = 17.5*scaler

# Add values in the increasing phase
while current_value <= 90*scaler:
    width_val.append(current_value)
    current_value += 3*scaler

# Subtract values in the decreasing phase
while current_value >= 17.5*scaler:
    width_val.append(current_value)
    current_value -= 3*scaler
print(width_val)

# Values for extending vertically
height_val = []
current_value = 17.5*scaler

# Add values in the increasing phase
while current_value <= 90*scaler:
    height_val.append(current_value)
    current_value += 3*scaler

# Subtract values in the decreasing phase
while current_value >= 17.5*scaler:
    height_val.append(current_value)
    current_value -= 3*scaler
print(height_val)

# show experiment info
message = visual.TextStim(win, text='Experiment Info')
message.autoDraw = True  # Automatically draw every frame
win.flip()
core.wait(3.0)
message.autoDraw = False

# TRAINING PHASE
# 50 trials - z=horizontal & m=vertical
import random
training_phase = ['vertical'] * 25 + ['horizontal'] * 25
random.shuffle(training_phase)
print(training_phase)


# prepare stimuli
width=20
height=20

upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), stimulus_size+(height/2)),fillColor=color_quartets,lineColor=color_quartets)
upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), stimulus_size+(height/2)),fillColor=color_quartets,lineColor=color_quartets)
lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), -stimulus_size-(height/2)),fillColor=color_quartets,lineColor=color_quartets)
lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), -stimulus_size-(height/2)),fillColor=color_quartets,lineColor=color_quartets)
stimuli = [upper_left, upper_right, lower_left, lower_right]

while True:
    message = visual.TextStim(win, text='Press "z" for horizontal & "m" for vertical; "space" for continue').draw()
    #message.autoDraw = True  # Automatically draw every frame
    win.flip()
    keyPressed = event.getKeys()
    if keyPressed == ["space"]:
        break 
#message.autoDraw = False

for i in range(1,51):
    if training_phase[i]=="vertical":
        
        duration = 1 # seconds
        for i in list(range(0,duration)):
        
            # 1 second
            for i in list(range(0,freq)):
            
                for i in list(range(0,2)):
                    stimuli[i].draw()
                win.flip()
                core.wait((1/freq)/2)    
                
                for i in list(range(2,4)):
                    stimuli[i].draw()
                win.flip()
                core.wait((1/freq)/2)  
    
    if training_phase[i]=="horizontal":
        
        duration = 1 # seconds
        for i in list(range(0,duration)):
        
            # 1 second
            for i in list(range(0,freq)):
            
                for i in list(range(1,4,2)):
                    stimuli[i].draw()
                win.flip()
                core.wait((1/freq)/2)    
                
                for i in list(range(0,3,2)):
                    stimuli[i].draw()
                win.flip()
                core.wait((1/freq)/2)  
    
win.close()
core.quit()












