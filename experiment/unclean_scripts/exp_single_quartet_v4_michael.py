
# Pelin Ozsezer - 5th Oct 2023
# Changed by Michael D. Nunez 11-Jan-2024

### Experiment for Single Motion Quartet ###

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


### TO SAVE DATA ###
# training
training_folder_path = '/Users/pelinozsezer/Desktop/EXP1_MP/experiment'
training_file_name = 'training_data.csv'

training_block_no = []
training_trial_no = []
training_motion_type = []
training_key_response = []
training_rt = []

# experiment


# COLORS
color_gray = [0, 0, 0]
color_quartets = [0.9, 0.9, 0.9]  # close to white

# window settings
#win = visual.Window(size=[1792, 1120], color=color_gray) #units="pix", screen = 0, fullscr=False, allowGUI=True # personal laptop
# units="pix", screen = 0, fullscr=False, allowGUI=True # work laptop
win = visual.Window(size=[1512, 982], color=color_gray, units="pix")

# mouse -  remove cursor
mouse = Mouse(visible=False)
mouse.setVisible(False)

# # get refresh rate
# refresh_r = round(win.getActualFrameRate())
# print(f"refresh rate: {refresh_r} Hz")

# keyboard settings
kb = keyboard.Keyboard()
keys = kb.getKeys(['z', 'm', 'space'], waitRelease=True)

## PARAMETERS ##
scaler = 1

n_trials_training = 4
corr_resp_training = 0
accuracy_training = 0

block_number_experiment = 1
trial_number_experiment = 10

# MQ parameters
stimulus_size =  10*scaler
freq = 2  # 1 cycle or freq is when all the quartets have been shown.
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






## EXPERIMENT PHASE ###

# fixation cross
fixation = visual.ShapeStim(win,
                            vertices=((0, -0.05), (0, 0.05), (0, 0),
                                      (-0.05, 0), (0.05, 0)),
                            lineWidth=75,
                            closeShape=False,
                            lineColor="white"
                            )


##
# 1 cycle - trial: extending-shrinking square first horizontally, then vertically
for block in range(1, block_number_experiment+1):

    for trial in range(1, trial_number_experiment+1):
        scaler = 1

        width_val = []
        result = math.sqrt(360)
        current_value = (result)*scaler
        start_value = current_value

        # Add values in the increasing phase
        while current_value <= 90*scaler:
            width_val.append(current_value)
            current_value += 3*scaler

        # Subtract values in the decreasing phase
        while current_value >= result*scaler:
            width_val.append(current_value)
            current_value -= 3*scaler
        # Now, 'values' contains the desired array
        print(width_val)
        width_val_1st_half = width_val

        totalx = start_value ** 2
        height = (totalx/current_value)

        # There is a better way to do this, but in the interest of time - Michael 11-Jan-2024
        # calculate heights for extending vertically
        height_val = []
        # result=math.sqrt(360)
        current_value = height  # (result)*scaler
        start_value = current_value

        # Add values in the increasing phase
        while current_value <= 90*scaler:
            height_val.append(current_value)
            current_value += 3*scaler

        # Subtract values in the decreasing phase
        while current_value >= result*scaler:
            height_val.append(current_value)
            current_value -= 3*scaler
        # Now, 'values' contains the desired array
        print(height_val)

        width_val_2nd_half = [totalx / x for x in height_val]

        width_val = width_val_1st_half + width_val_2nd_half

        color_quartets = [0.9, 0.9, 0.9]

        fixation.draw()
        win.flip()
        core.wait(2)

        kb.clock.reset()
        kb.getKeys()

        ## full loop
        width_index = 0
        forward = True
        while True: #Temporary fix for infinite loop
            width = width_val[width_index]

            height = (totalx/width)  # *scaler

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

            if width_index == 0:
            	forward = True
            elif width_index == len(width_val):
            	forward = False

            if forward:
            	width_index += 1 #forward
            else:
            	width_index -= 1 #reverse

            # if a key is pressed
            if len(kb.getKeys()) > 0:
                print('key pressed - change of percept')
                idx_width_keyPress = width_val.index(width)
                idx_width_extend = idx_width_keyPress+1
                width_val = width_val
                width = width_val[idx_width_extend]
                forward = not forward


message = visual.TextStim(win, text='END')
message.autoDraw = True  # Automatically draw every frame
win.flip()
core.wait(2.0)
message.text = 'Did it work?'
win.flip()
core.wait(2.0)

win.close()
core.quit()
