# import libraries
#!pip install psychopy
import os
import sys
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

from psychopy import gui, core, visual, event
from psychopy.gui import DlgFromDict
from psychopy.core import Clock, quit, wait
from psychopy.visual import Window
from psychopy.hardware import keyboard
from psychopy.event import Mouse


# COLORS
color_gray = [0, 0, 0]
color_quartets = [0.9, 0.9, 0.9]  # close to white

# window settings
#win = visual.Window(size=[1792, 1120], color=color_gray) #units="pix", screen = 0, fullscr=False, allowGUI=True # personal laptop
# units="pix", screen = 0, fullscr=False, allowGUI=True # work laptop
win = visual.Window(size=[1512, 982], color=color_gray, units="pix")

# keyboard settings
kb = keyboard.Keyboard()
keys = kb.getKeys(['z', 'm', 'space'], waitRelease=True)


## PARAMETERS ##
scaler = 1

block_number_experiment = 1
trial_number_experiment = 10 # redefine based on participants' responses

# MQ parameters
stimulus_size =  10*scaler
freq = 2  # 1 cycle or freq is when all the quartets have been shown.
# height
# width


### EXPERIMENTAL PHASE ###

# fixation cross
fixation = visual.ShapeStim(win,
                            vertices=((0, -0.05), (0, 0.05), (0, 0),
                                      (-0.05, 0), (0.05, 0)),
                            lineWidth=75,
                            closeShape=False,
                            lineColor="white"
                            )

experimental_values = list(range(10,110,10))
max_index = experimental_values.index(max(experimental_values))
dynamical_experimental_values = experimental_values
hxw=float(experimental_values[-1])



# 1 cycle - trial: extending-shrinking square first horizontally, then vertically
for block in range(1, block_number_experiment+1):
    
    fixation.draw()
    win.flip()
    core.wait(2)
    

    for trial in range(1, trial_number_experiment+1):
        
        
        # EXTENDING HORIZONTALLY
        flag_change=0
        idx=0
        while flag_change==0:
            
            idx =+ 1
            width=dynamical_experimental_values[idx]
            height = (hxw/width)  # *scaler
            
            # prepare stimuli
            upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(
                width/2), stimulus_size+(height/2)), fillColor=color_quartets, lineColor=color_quartets)
            upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(
                stimulus_size+(width/2), stimulus_size+(height/2)), fillColor=color_quartets, lineColor=color_quartets)
            lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(
                width/2), -stimulus_size-(height/2)), fillColor=color_quartets, lineColor=color_quartets)
            lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(
                stimulus_size+(width/2), -stimulus_size-(height/2)), fillColor=color_quartets, lineColor=color_quartets)
            stimuli = [upper_left, upper_right, lower_right, lower_left]
            
            
            duration = 1  # seconds
            for i in list(range(0, duration)):

                # 1 second
                for i in list(range(0, freq)):

                    for i in list(range(0, 3, 2)):
                        stimuli[i].draw()
                    win.flip()
                    core.wait((1/freq)/2)

                    for i in list(range(1, 4, 2)):
                        stimuli[i].draw()
                    win.flip()
                    core.wait((1/freq)/2)
                
                
            # if the last two keys are thg eame # break 
            #     break
            # if max_index==9: # if max boundary is reached, wait for key response - z or m
            #     break
      
            
      
        
        dynamical_experimental_values = dynamical_experimental_values[:idx]
        dynamical_experimental_values.reverse()
        
        
      
        
        # SHRINKING HORIZONTALLY
        flag_change==0
        idx=0
        while flag_change==0:    
            
            idx =+ 1
            width=dynamical_experimental_values[idx]
            height = (hxw/width)  # *scaler
            
            # prepare stimuli
            upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(
                width/2), stimulus_size+(height/2)), fillColor=color_quartets, lineColor=color_quartets)
            upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(
                stimulus_size+(width/2), stimulus_size+(height/2)), fillColor=color_quartets, lineColor=color_quartets)
            lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(
                width/2), -stimulus_size-(height/2)), fillColor=color_quartets, lineColor=color_quartets)
            lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(
                stimulus_size+(width/2), -stimulus_size-(height/2)), fillColor=color_quartets, lineColor=color_quartets)
            stimuli = [upper_left, upper_right, lower_right, lower_left]
            
            
            duration = 1  # seconds
            for i in list(range(0, duration)):

                # 1 second
                for i in list(range(0, freq)):

                    for i in list(range(0, 3, 2)):
                        stimuli[i].draw()
                    win.flip()
                    core.wait((1/freq)/2)

                    for i in list(range(1, 4, 2)):
                        stimuli[i].draw()
                    win.flip()
                    core.wait((1/freq)/2)
                
            
            # if the last two keys are thg eame # break 
            #     break
            # if max_index==dynamical_experimental_values[-1]: # no key response expected here
            #     break
            
        
        current_val=dynamical_experimental_values[idx]
        index = experimental_values.index(current_val)
        dynamical_experimental_values = experimental_values[index:]
        
        
        # transition from width value to height value??
        # EXTENDING VERTICALLY
        flag_change==0
        idx=0
        while flag_change==0:  
                
        # SHRINKING VERTICALLY
        flag_change==0
        idx=0
        while flag_change==0:  
            
            














