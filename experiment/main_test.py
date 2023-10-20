# responselar icin pythonda matrixe yaz ve sonra disa aktar.


# Pelin Ozsezer 

#!pip install psychopy

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
from psychopy.hardware import keyboard


kb = keyboard.Keyboard()
#keys = kb.getKeys()
keys = kb.getKeys(['right', 'left', 'quit'], waitRelease=True)


#win = visual.Window(size=[1792, 1120]) #units="pix", screen = 0, fullscr=False, allowGUI=True) #allowGUI! - personal laptop
win = visual.Window(size=[1512, 982]) #units="pix", screen = 0, fullscr=False, allowGUI=True) #allowGUI! - work laptop

# # get refresh rate
# refresh_r = round(win.getActualFrameRate())
# print(f"refresh rate: {refresh_r} Hz")


###############################################################################

# MQ parameters
stimulus_size = 25
freq = 2 # 1 cycle/freq is when all the quartets have been shown.
height=100
width=200

#def draw_motquarts(stimulus_size, freq, height, width):

# prepare stimuli
upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), stimulus_size+(height/2)),fillColor=[1, -1, -1],lineColor=[-1, -1, 1])
upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), stimulus_size+(height/2)),fillColor=[1, -1, -1],lineColor=[-1, -1, 1])
lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), -stimulus_size-(height/2)),fillColor=[1, -1, -1],lineColor=[-1, -1, 1])
lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), -stimulus_size-(height/2)),fillColor=[1, -1, -1],lineColor=[-1, -1, 1])
stimuli = [upper_left, upper_right, lower_right, lower_left]

message = visual.TextStim(win, text='Wait')
message.autoDraw = True  # Automatically draw every frame
win.flip()
core.wait(3.0)
message.autoDraw = False

while True:
    
    duration = 5 # seconds
    for i in list(range(0,duration)):
    
        # 1 second
        for i in list(range(0,freq)):
        
            for i in list(range(0,3,2)):
                stimuli[i].draw()
            win.flip()
            core.wait((1/freq)/2)    
            
            for i in list(range(1,4,2)):
                stimuli[i].draw()
            win.flip()
            core.wait((1/freq)/2)  
            
    keyPressed = event.getKeys()

    #if len(kb.getKeys() > 0: # if a key is pressed
    if len(keyPressed > 0): # if a key is pressed
        print('KEYYYYYYYY')
        print(keyPressed)
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





##################################
###### Hysteresis Part ###########
##################################


# 1 cycle = trial genisleyen sonra uzayan sonra kare. 
# Pelin Ozsezer 

#!pip install psychopy

# import libraries
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


kb = keyboard.Keyboard()
keys = kb.getKeys()

#win = visual.Window(size=[1792, 1120]) #units="pix", screen = 0, fullscr=False, allowGUI=True) #allowGUI! - personal laptop
win = visual.Window(size=[1512, 982]) #units="pix", screen = 0, fullscr=False, allowGUI=True) #allowGUI! - work laptop

# # get refresh rate
# refresh_r = round(win.getActualFrameRate())
# print(f"refresh rate: {refresh_r} Hz")


###############################################################################



# key response change (key release & other key press)- AR - time 
# label - timing: her bir tip icin ayri kod.
# set background color yourself.
# ADD color parameter: brighter than background - close to white

 # ADD MULTIPLIER 
multiplier=1.5
# MQ parameters
stimulus_size = 10*multiplier
freq = 2 # 1 cycle/freq is when all the quartets have been shown.
# height=100
# width=200



width_val = []
current_value = 17.5*multiplier

# Add values in the increasing phase
while current_value <= 90*multiplier:
    width_val.append(current_value)
    current_value += 3*multiplier

# Subtract values in the decreasing phase
while current_value >= 17.5*multiplier:
    width_val.append(current_value)
    current_value -= 3*multiplier
# Now, 'values' contains the desired array
print(width_val)




height_val = []
current_value = 17.5*multiplier

# Add values in the increasing phase
while current_value <= 90*multiplier:
    height_val.append(current_value)
    current_value += 3*multiplier

# Subtract values in the decreasing phase
while current_value >= 17.5*multiplier:
    height_val.append(current_value)
    current_value -= 3*multiplier

# Now, 'values' contains the desired array
print(height_val)



#def draw_motquarts(stimulus_size, freq, height, width):



message = visual.TextStim(win, text='Wait')
message.autoDraw = True  # Automatically draw every frame
win.flip()
core.wait(3.0)
message.autoDraw = False

color_quartets=[0.9, 0.9, 0.9]


for width in width_val:
    height=(360/width)*multiplier
    
    # prepare stimuli
    upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), stimulus_size+(height/2)),fillColor=color_quartets,lineColor=color_quartets)
    upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), stimulus_size+(height/2)),fillColor=color_quartets,lineColor=color_quartets)
    lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), -stimulus_size-(height/2)),fillColor=color_quartets,lineColor=color_quartets)
    lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), -stimulus_size-(height/2)),fillColor=color_quartets,lineColor=color_quartets)
    stimuli = [upper_left, upper_right, lower_right, lower_left]
    
    duration = 1 # seconds
    for i in list(range(0,duration)):
    
        # 1 second
        for i in list(range(0,freq)):
        
            for i in list(range(0,3,2)):
                stimuli[i].draw()
            win.flip()
            core.wait((1/freq)/2)    
            
            for i in list(range(1,4,2)):
                stimuli[i].draw()
            win.flip()
            core.wait((1/freq)/2)  
            
    # if len(kb.getKeys()) > 0: # if a key is pressed
    #     print('KEYYYYYYYY')
    #     # thisKey = kb.getKeys()
    #     # print(thisKey)
    #     break
event.clearEvents()



# key response accruta timign in psychopy? 


for height in height_val:
    width=(360/height)*multiplier
    
    
    # prepare stimuli
    upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), stimulus_size+(height/2)),fillColor=[1, 1, 1],lineColor=[11, 1, 1])
    upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), stimulus_size+(height/2)),fillColor=[1, 1, 1],lineColor=[1, 1, 1])
    lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), -stimulus_size-(height/2)),fillColor=[1, 1, 1],lineColor=[1, 1, 1])
    lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), -stimulus_size-(height/2)),fillColor=[1, 1, 1],lineColor=[1, 1, 1])
    stimuli = [upper_left, upper_right, lower_right, lower_left]
    
    duration =  1 # seconds
    for i in list(range(0,duration)):
    
        # 1 second
        for i in list(range(0,freq)):
        
            for i in list(range(0,3,2)):
                stimuli[i].draw()
            win.flip()
            core.wait((1/freq)/2)    
            
            for i in list(range(1,4,2)):
                stimuli[i].draw()
            win.flip()
            core.wait((1/freq)/2)  
            
    # if len(kb.getKeys()) > 0: # if a key is pressed
    #     print('KEYYYYYYYY')
    #     # thisKey = kb.getKeys()
    #     # print(thisKey)
    #     break
event.clearEvents()






def find_dimensions(lst):
    if not isinstance(lst, list):
        return 0  # This is not a list, so it has 0 dimensions.
    # Recursively find the dimensions of the nested list and add 1 for the current level.
    return 1 + find_dimensions(lst[1])











message = visual.TextStim(win, text='LOL')
message.autoDraw = True  # Automatically draw every frame
win.flip()
core.wait(2.0)
message.text = 'Did it work?' 
win.flip() 
core.wait(2.0)

win.close()
core.quit()






## FIXATION CROSS




















    
















