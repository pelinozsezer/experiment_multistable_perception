
# Pelin Ozsezer - Experiment 1


import os
import time
import numpy as np
import pandas as pd

from psychopy import core, visual, event, parallel

from psychopy.gui import DlgFromDict
from psychopy.visual import Window
#from psychopy.core import Clock, quit, wait
from psychopy.event import Mouse
from psychopy.hardware.keyboard import Keyboard


import matplotlib.pyplot as plt
#import time

from psychopy import visual, event
from pathlib import Path

win = visual.Window(size = [1920, 1080], units="pix", screen = 0, fullscr=False, allowGUI = False)

# Get refresh rate
refresh_r = round(win.getActualFrameRate())q
print(f"refresh rate: {refresh_r} Hz")

stimulus_size = 200
stimulus_speed = 5

upper_left = visual.Rect(win, width=stimulus_size, height=stimulus_size, pos=(-stimulus_size, stimulus_size))
upper_right = visual.Rect(win, width=stimulus_size, height=stimulus_size, pos=(stimulus_size, stimulus_size))
lower_left = visual.Rect(win, width=stimulus_size, height=stimulus_size, pos=(-stimulus_size, -stimulus_size))
lower_right = visual.Rect(win, width=stimulus_size, height=stimulus_size, pos=(stimulus_size, -stimulus_size))

stimuli = [upper_left, upper_right, lower_left, lower_right]

while not event.getKeys():
    for stim in stimuli:
        stim.setPos((stim.pos[0] + stimulus_speed, stim.pos[1]))
        stim.draw()

    win.flip()

win.close()
core.quit()