
# Written by Pelin Ozsezer

### Experiment for Single Motion Quartet ###

## import libraries
# !pip install psychopy
import os
import sys
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# import definitions_EXP_M1 as def_exp
os.chdir('/Users/pelinozsezer/Desktop/EXP1_MP/experiment')
import definitions_EXP_M1
from definitions_EXP_M1 import training_phase, demonstration_phase, experiment_phase

from psychopy import gui, core, visual, event
from psychopy.gui import DlgFromDict
from psychopy.core import Clock, quit, wait
from psychopy.visual import Window
from psychopy.event import Mouse
from psychopy.hardware import keyboard


### PARAMETERS & VARIABLES ###

## MQ parameters
scaler = 1
stimulus_size =  10*scaler
freq = 2  # 1 cycle or freq is when all the quartets have been shown.
# height
# width

## hardware
color_gray = [0, 0, 0]
color_quartets = [0.9, 0.9, 0.9]  # close to white

## training phase
training_folder_path = '/Users/pelinozsezer/Desktop/EXP1_MP/experiment'
training_file_name = 'training_data.csv'
n_trials_training = 20

## demonstration phase
n_trials_demonstration = 2

## experiment phase
experiment_folder_path = '/Users/pelinozsezer/Desktop/EXP1_MP/experiment'
experiment_file_name = 'experiment_data.csv'
block_number_experiment = 1
trial_number_experiment = 10



## Settings

# window settings
# win = visual.Window(size=[1792, 1120], color=color_gray, units="pix") # screen = 0, fullscr=False, allowGUI=True  # personal laptop
win = visual.Window(size=[1512, 982], color=color_gray, units="pix")    # screen = 0, fullscr=False, allowGUI=True  # work laptop

# mouse - remove cursor!

# # get refresh rate
# refresh_r = round(win.getActualFrameRate())
# print(f"refresh rate: {refresh_r} Hz")

# keyboard settings
kb = keyboard.Keyboard()
keys = kb.getKeys(['z', 'm', 'space'], waitRelease=True)



## Show Information
message = visual.TextStim(win, text='Information about the Experiment')
message.autoDraw = True  # Automatically draw every frame
win.flip()
core.wait(3.0)
message.autoDraw = False

### CALL ###
training_phase(n_trials_training)
demonstration_phase(n_trials_demonstration)
# experiment_phase()



message = visual.TextStim(win, text='TERMINUS')
message.autoDraw = True  # Automatically draw every frame
win.flip()
core.wait(2.0)

win.close()
core.quit()



