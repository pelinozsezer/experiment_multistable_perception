
# Pelin Ozsezer - 5th Oct 2023

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

        #
        totalx = start_value ** 2

        # height_val = []
        # result=math.sqrt(360)
        # current_value = (result)*scaler
        # start_value=current_value

        # # Add values in the increasing phase
        # while current_value <= 90*scaler:
        #     height_val.append(current_value)
        #     current_value += 3*scaler

        # # Subtract values in the decreasing phase
        # while current_value >= 17.5*scaler:
        #     height_val.append(current_value)
        #     current_value -= 3*scaler

        # # Now, 'values' contains the desired array
        # print(height_val)

        # height_val = []
        # result=math.sqrt(360)
        # current_value = (result)*scaler
        # start_value=current_value

        # # Add values in the increasing phase
        # while current_value <= 90*scaler:
        #     height_val.append(current_value)
        #     current_value += 3*scaler

        # # Subtract values in the decreasing phase
        # while current_value >= result*scaler:
        #     height_val.append(current_value)
        #     current_value -= 3*scaler
        # # Now, 'values' contains the desired array
        # print(height_val)


        color_quartets = [0.9, 0.9, 0.9]

        fixation.draw()
        win.flip()
        core.wait(2)

        kb.clock.reset()
        kb.getKeys()

        ## extending horizontally
        for width in width_val:

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

            # if a key is pressed
            if len(kb.getKeys()) > 0:
                print('key pressed - change of percept')
                idx_width_keyPress = width_val.index(width)
                idx_width_extend = idx_width_keyPress+1
                width = width_val[idx_width_extend]
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

                break

        ## shrinking horizontally

        width_val_shrinking = width_val[:idx_width_keyPress]
        width_val_shrinking.reverse()

        kb.getKeys()
        for width in width_val_shrinking:
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

            # if a key is pressed
            if len(kb.getKeys()) > 0:
                print('key pressed - change of percept')

                #needs to continue for more 1 cycle
                idx_width_keyPress = width_val.index(width)
                idx_width_shrink = idx_width_keyPress-1
                width = width_val_shrinking[idx_width_shrink]
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

                break

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

        ## extending vertically
        for height in height_val:
            width = (totalx/height)  # *scaler

            # prepare stimuli
            upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(
                width/2), stimulus_size+(height/2)), fillColor=[1, 1, 1], lineColor=[11, 1, 1])
            upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(
                stimulus_size+(width/2), stimulus_size+(height/2)), fillColor=[1, 1, 1], lineColor=[1, 1, 1])
            lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(
                width/2), -stimulus_size-(height/2)), fillColor=[1, 1, 1], lineColor=[1, 1, 1])
            lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(
                stimulus_size+(width/2), -stimulus_size-(height/2)), fillColor=[1, 1, 1], lineColor=[1, 1, 1])
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

            # if a key is pressed
            if len(kb.getKeys()) > 0:
                print('key pressed - change of percept')
                idx_height_keyPress = height_val.index(height)
                idx_height_extend = idx_height_keyPress+1
                height = height_val[idx_height_extend]
                width = (totalx/height)  # *scaler

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

                break

        ## shrinking vertically
        height_val_shrinking = height_val[:idx_height_keyPress]
        height_val_shrinking.reverse()

        kb.getKeys()
        for height in height_val_shrinking:
            width = (totalx/height)  # *scaler

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

            # if a key is pressed
            if len(kb.getKeys()) > 0:
                print('key pressed - change of percept')


message = visual.TextStim(win, text='END')
message.autoDraw = True  # Automatically draw every frame
win.flip()
core.wait(2.0)
message.text = 'Did it work?'
win.flip()
core.wait(2.0)

win.close()
core.quit()




