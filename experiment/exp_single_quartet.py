
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
# 1) key response change (key release & other key press) - AR - time 
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
scaler=1.5
n_trials_training=20

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
training_phase = ['vertical'] * int(n_trials_training/2) + ['horizontal'] * int(n_trials_training/2) 
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
    keyPressed = kb.waitKeys()
    if keyPressed == ["space"]:
        break 
    
    



#message.autoDraw = False
# fixation cross
fixation = visual.ShapeStim(win, 
    vertices=((0, -0.05), (0, 0.05), (0,0), (-0.05,0), (0.05, 0)),
    lineWidth=75,
    closeShape=False,
    lineColor="white"
)
#

fixation.draw()
win.flip()
core.wait(2)
    
for i in range(n_trials_training):
    
    if training_phase[i]=="vertical":
        
        fixation.draw()
        win.flip()
        core.wait(1)
        
        duration = 2 # seconds

        kb.clock.reset()
        for i in list(range(0,duration)):

            # 1 second
            for i in list(range(0,freq)):
                # keyPressed = kb.getKeys(keyList=['z','m'])


                for i in list(range(0,2)):
                    stimuli[i].draw()
     
                win.flip()
                core.wait((1/freq)/2)    

                
                for i in list(range(2,4)):
                    stimuli[i].draw()
                win.flip()
                core.wait((1/freq)/2)  

                
                
                
        # while kb.clock.getTime() < 2:
        #     keyPressed = kb.waitKeys(keyList=['z','m'])
        #     # for key in keys:
        #     #     # The `:.3f` part in the F-string makes sure the float is only displayed with 3 decimals!
        #     #     print(f"The '{key.name}' key was pressed within {key.rt:.3f} seconds for a total of {key.duration:.3f} seconds")
                
        # while True:
        #     keyPressed = kb.getKeys(['z','m'])

        #     if keyPressed[0] == ["m"]:
        #         message = visual.TextStim(win, text='CORRECT').draw()
        #         win.flip()
        #         core.wait(1)
        #         break
        #     elif keyPressed[0] == ["z"]:
        #         message = visual.TextStim(win, text='INCORRECT').draw()
        #         win.flip()
        #         core.wait(1)
        #         break

    # get history of event.getkeys
    
    if training_phase[i]=="horizontal":
        
        fixation.draw()
        win.flip()
        core.wait(1)
        
        duration = 2 # seconds
        kb.clock.reset()
        kb.getKeys()
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
       
                
        
        # while kb.clock.getTime() < 2:
        #     keyPressed = kb.waitKeys(keyList=['z','m'])
        #     # for key in keys:
        #     #     # The `:.3f` part in the F-string makes sure the float is only displayed with 3 decimals!
        #     #     print(f"The '{key.name}' key was pressed within {key.rt:.3f} seconds for a total of {key.duration:.3f} seconds")
        
        # while True:
        #     keyPressed = kb.getKeys(['z','m'])
        keyPressed = kb.getKeys()
        
        if keyPressed == []:
            message = visual.TextStim(win, text='NO RESPONSE').draw()
            win.flip()
            core.wait(1)
        elif keyPressed[0].name == "z":
            print(keyPressed[0].name)
            message = visual.TextStim(win, text='CORRECT').draw()
            win.flip()
            core.wait(1)
        elif keyPressed[0].name == "m":
            print(keyPressed[0].name)
            message = visual.TextStim(win, text='INCORRECT').draw()
            win.flip()
            core.wait(1)
        else:
            print(keyPressed[0].name)
            message = visual.TextStim(win, text='INCORRECT - except z & m').draw()
            win.flip()
            core.wait(1)
    
win.close()
core.quit()



# # EXPERIMENT PHASE
# # 1 cycle - trial: extending square first horizontally, then vertically

# width_val = []
# current_value = 17.5*scaler

# # Add values in the increasing phase
# while current_value <= 90*scaler:
#     width_val.append(current_value)
#     current_value += 3*scaler

# # Subtract values in the decreasing phase
# while current_value >= 17.5*scaler:
#     width_val.append(current_value)
#     current_value -= 3*scaler
# # Now, 'values' contains the desired array
# print(width_val)




# height_val = []
# current_value = 17.5*scaler

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



# #def draw_motquarts(stimulus_size, freq, height, width):



# message = visual.TextStim(win, text='Wait')
# message.autoDraw = True  # Automatically draw every frame
# win.flip()
# core.wait(3.0)
# message.autoDraw = False

# color_quartets=[0.9, 0.9, 0.9]


# for width in width_val:
#     height=(360/width)*scaler
    
#     # prepare stimuli
#     upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), stimulus_size+(height/2)),fillColor=color_quartets,lineColor=color_quartets)
#     upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), stimulus_size+(height/2)),fillColor=color_quartets,lineColor=color_quartets)
#     lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), -stimulus_size-(height/2)),fillColor=color_quartets,lineColor=color_quartets)
#     lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), -stimulus_size-(height/2)),fillColor=color_quartets,lineColor=color_quartets)
#     stimuli = [upper_left, upper_right, lower_right, lower_left]
    
#     duration = 1 # seconds
#     for i in list(range(0,duration)):
    
#         # 1 second
#         for i in list(range(0,freq)):
        
#             for i in list(range(0,3,2)):
#                 stimuli[i].draw()
#             win.flip()
#             core.wait((1/freq)/2)    
            
#             for i in list(range(1,4,2)):
#                 stimuli[i].draw()
#             win.flip()
#             core.wait((1/freq)/2)  
            
#     # if len(kb.getKeys()) > 0: # if a key is pressed
#     #     print('KEYYYYYYYY')
#     #     # thisKey = kb.getKeys()
#     #     # print(thisKey)
#     #     break
# event.clearEvents()



# # key response accruta timign in psychopy? 


# for height in height_val:
#     width=(360/height)*scaler
    
    
#     # prepare stimuli
#     upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), stimulus_size+(height/2)),fillColor=[1, 1, 1],lineColor=[11, 1, 1])
#     upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), stimulus_size+(height/2)),fillColor=[1, 1, 1],lineColor=[1, 1, 1])
#     lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), -stimulus_size-(height/2)),fillColor=[1, 1, 1],lineColor=[1, 1, 1])
#     lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), -stimulus_size-(height/2)),fillColor=[1, 1, 1],lineColor=[1, 1, 1])
#     stimuli = [upper_left, upper_right, lower_right, lower_left]
    
#     duration =  1 # seconds
#     for i in list(range(0,duration)):
    
#         # 1 second
#         for i in list(range(0,freq)):
        
#             for i in list(range(0,3,2)):
#                 stimuli[i].draw()
#             win.flip()
#             core.wait((1/freq)/2)    
            
#             for i in list(range(1,4,2)):
#                 stimuli[i].draw()
#             win.flip()
#             core.wait((1/freq)/2)  
            
#     # if len(kb.getKeys()) > 0: # if a key is pressed
#     #     print('KEYYYYYYYY')
#     #     # thisKey = kb.getKeys()
#     #     # print(thisKey)
#     #     break
# event.clearEvents()




# message = visual.TextStim(win, text='END')
# message.autoDraw = True  # Automatically draw every frame
# win.flip()
# core.wait(2.0)
# message.text = 'Did it work?' 
# win.flip() 
# core.wait(2.0)

# win.close()
# core.quit()












