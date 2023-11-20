
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


### TO SAVE DATA ###
training_folder_path = '/Users/pelinozsezer/Desktop/EXP1_MP/experiment'
training_file_name = 'training_data.csv'

training_block_no = []
training_trial_no = []
training_motion_type = []
training_key_response = []
training_rt = []


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






# ### TRAINING PHASE ###
# # 20 trials - z=horizontal & m=vertical
# import random
# training_phase = ['vertical'] * int(n_trials_training/2) + ['horizontal'] * int(n_trials_training/2)
# random.shuffle(training_phase)
# print(training_phase)


# # prepare stimuli
# width=20
# height=20

# upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), stimulus_size+(height/2)),fillColor=color_quartets,lineColor=color_quartets)
# upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), stimulus_size+(height/2)),fillColor=color_quartets,lineColor=color_quartets)
# lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), -stimulus_size-(height/2)),fillColor=color_quartets,lineColor=color_quartets)
# lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), -stimulus_size-(height/2)),fillColor=color_quartets,lineColor=color_quartets)
# stimuli = [upper_left, upper_right, lower_left, lower_right]


# while True:
#     message = visual.TextStim(win, text='Press "z" for horizontal;\n"m" for vertical;\n"space" for continue').draw()
#     #message.autoDraw = True  # Automatically draw every frame
#     win.flip()
#     keyPressed = kb.waitKeys()
#     if keyPressed == ["space"]:
#         break


# #message.autoDraw = False
# # fixation cross
# fixation = visual.ShapeStim(win,
#     vertices=((0, -0.05), (0, 0.05), (0,0), (-0.05,0), (0.05, 0)),
#     lineWidth=75,
#     closeShape=False,
#     lineColor="white"
# )

# fixation.draw()
# win.flip()
# core.wait(2)


# training_block=0
# while accuracy_training < 0.9:


#     if not training_block==0:
#         while True:
#             message = visual.TextStim(win, text='Accuracy is lower than 90%. \n It must be more than 90%. \n "space" to continue for more training').draw()
#             #message.autoDraw = True  # Automatically draw every frame
#             win.flip()
#             keyPressed = kb.waitKeys()
#             if keyPressed == ["space"]:
#                 break


#     for trial_no in range(n_trials_training):

#         if training_phase[trial_no]=="vertical":

#             fixation.draw()
#             win.flip()
#             core.wait(1)

#             duration = 2 # seconds

#             kb.getKeys()
#             kb.clock.reset()

#             for i in list(range(0,duration)):

#                 # 1 second
#                 for i in list(range(0,freq)):


#                     for i in list(range(0,2)):
#                         stimuli[i].draw()

#                     win.flip()
#                     core.wait((1/freq)/2)


#                     for i in list(range(2,4)):
#                         stimuli[i].draw()
#                     win.flip()
#                     core.wait((1/freq)/2)


#             keyPressed = kb.getKeys()

#             if keyPressed == []:
#                 print('no response')
#                 message = visual.TextStim(win, text='NO RESPONSE').draw()
#                 win.flip()

#                 training_block_no=training_block_no+[training_block+1]
#                 training_trial_no=training_trial_no+[trial_no+1]
#                 training_motion_type=training_motion_type+["vertical"]
#                 training_key_response=training_key_response+["no response"]
#                 training_rt= training_rt+ ["N/A"]

#                 core.wait(1)

#             elif keyPressed[0].name == "z":
#                 print(keyPressed[0].name)
#                 #print(keyPressed[1].name)
#                 message = visual.TextStim(win, text='INCORRECT').draw()
#                 win.flip()

#                 training_block_no=training_block_no+[training_block+1]
#                 training_trial_no=training_trial_no+[trial_no+1]
#                 training_motion_type=training_motion_type+["vertical"]
#                 training_key_response=training_key_response+["z"]
#                 training_rt= training_rt+ [keyPressed[0].rt]

#                 core.wait(1)

#             elif keyPressed[0].name == "m":
#                 print(keyPressed[0].name)
#                 message = visual.TextStim(win, text='CORRECT').draw()
#                 corr_resp_training=corr_resp_training+1
#                 win.flip()

#                 training_block_no=training_block_no+[training_block+1]
#                 training_trial_no=training_trial_no+[trial_no+1]
#                 training_motion_type=training_motion_type+["vertical"]
#                 training_key_response=training_key_response+["m"]
#                 training_rt= training_rt+ [keyPressed[0].rt]

#                 core.wait(1)

#             else:
#                 print(keyPressed[0].name)
#                 message = visual.TextStim(win, text='INCORRECT - except z & m').draw()
#                 win.flip()

#                 training_block_no=training_block_no+[training_block+1]
#                 training_trial_no=training_trial_no+[trial_no+1]
#                 training_motion_type=training_motion_type+["vertical"]
#                 training_key_response=training_key_response+["other"]
#                 training_rt= training_rt+ [keyPressed[0].rt]

#                 core.wait(1)


#         if training_phase[trial_no]=="horizontal":

#             fixation.draw()
#             win.flip()
#             core.wait(1)

#             duration = 2 # seconds

#             kb.getKeys()
#             kb.clock.reset()

#             for i in list(range(0,duration)):


#                 # 1 second
#                 for i in list(range(0,freq)):

#                     for i in list(range(1,4,2)):
#                         stimuli[i].draw()
#                     win.flip()
#                     core.wait((1/freq)/2)


#                     for i in list(range(0,3,2)):

#                         stimuli[i].draw()
#                     win.flip()
#                     core.wait((1/freq)/2)

#             keyPressed = kb.getKeys()

#             if keyPressed == []:
#                 print('no response')
#                 message = visual.TextStim(win, text='NO RESPONSE').draw()
#                 win.flip()

#                 training_block_no=training_block_no+[training_block+1]
#                 training_trial_no=training_trial_no+[trial_no+1]
#                 training_motion_type=training_motion_type+["horizontal"]
#                 training_key_response=training_key_response+["no response"]
#                 training_rt= training_rt+ ["N/A"]

#                 core.wait(1)
#             elif keyPressed[0].name == "z":
#                 print(keyPressed[0].name)
#                 message = visual.TextStim(win, text='CORRECT').draw()
#                 corr_resp_training=corr_resp_training+1
#                 win.flip()

#                 training_block_no=training_block_no+[training_block+1]
#                 training_trial_no=training_trial_no+[trial_no+1]
#                 training_motion_type=training_motion_type+["horizontal"]
#                 training_key_response=training_key_response+["z"]
#                 training_rt= training_rt+ [keyPressed[0].rt]

#                 core.wait(1)

#             elif keyPressed[0].name == "m":
#                 print(keyPressed[0].name)
#                 message = visual.TextStim(win, text='INCORRECT').draw()
#                 win.flip()

#                 training_block_no=training_block_no+[training_block+1]
#                 training_trial_no=training_trial_no+[trial_no+1]
#                 training_motion_type=training_motion_type+["horizontal"]
#                 training_key_response=training_key_response+["m"]
#                 training_rt= training_rt+ [keyPressed[0].rt]

#                 core.wait(1)

#             else:
#                 print(keyPressed[0].name)
#                 message = visual.TextStim(win, text='INCORRECT - except z & m').draw()
#                 win.flip()

#                 training_block_no=training_block_no+[training_block+1]
#                 training_trial_no=training_trial_no+[trial_no+1]
#                 training_motion_type=training_motion_type+["horizontal"]
#                 training_key_response=training_key_response+["other"]
#                 training_rt= training_rt+ [keyPressed[0].rt]

#                 core.wait(1)

#     accuracy_training = corr_resp_training/n_trials_training
#     training_block=training_block+1
#     corr_resp_training=0


# # save data from training phase
# df = pd.DataFrame({'block': training_block_no, 'trial': training_trial_no, 'motion_type': training_motion_type, 'key_response': training_key_response, 'RT': training_rt})
# training_full_file_path = training_folder_path + '/' + training_file_name
# df.to_csv(training_full_file_path, index=False)
# print(f"Data saved to '{training_full_file_path}'")

# while True:
#     message = visual.TextStim(win, text='Training phase has been succesfully completed. \n "space" to continue').draw()
#     #message.autoDraw = True  # Automatically draw every frame
#     win.flip()
#     keyPressed = kb.waitKeys()
#     if keyPressed == ["space"]:
#         break

# win.close()
# core.quit()





## DEMONSTRATION PHASE OF EXPERIMENTAL PARADIGM ##
while True:
    message = visual.TextStim(win, text='DEMONSTRATION PHASE OF EXPERIMENTAL PARADIGM. \n "space" for continue').draw()
    #message.autoDraw = True  # Automatically draw every frame
    win.flip()
    keyPressed = kb.waitKeys()
    if keyPressed == ["space"]:
        break
    

# ADD scaler 
scaler=1
# MQ parameters
stimulus_size = 10*scaler
freq = 2 # 1 cycle/freq is when all the quartets have been shown.
# height=100
# width=200



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
# Now, 'values' contains the desired array
print(width_val)

max_idx_width = width_val.index(max(width_val))



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

# Now, 'values' contains the desired array
print(height_val)

max_idx_height = height_val.index(max(height_val))



#def draw_motquarts(stimulus_size, freq, height, width):



message = visual.TextStim(win, text='Stimuli during the experimental phase - 2 trials')
message.autoDraw = True  # Automatically draw every frame
win.flip()
core.wait(3.0)
message.autoDraw = False

color_quartets=[0.9, 0.9, 0.9]


flag_demonstration = True
while flag_demonstration:
    
    for iteration in [1]:
        
        idx_counter=0
        for width in width_val:
            print(width)
            height=(360/width)*scaler
            
            idx_counter += 1
            
            # prepare stimuli
            upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), stimulus_size+(height/2)),fillColor=color_quartets,lineColor=color_quartets)
            upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), stimulus_size+(height/2)),fillColor=color_quartets,lineColor=color_quartets)
            lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), -stimulus_size-(height/2)),fillColor=color_quartets,lineColor=color_quartets)
            lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), -stimulus_size-(height/2)),fillColor=color_quartets,lineColor=color_quartets)
            stimuli = [upper_left, upper_right, lower_right, lower_left]
                
            if idx_counter <= max_idx_width:
                message = visual.TextStim(win, text='extending horizontally', pos=[0, -60])
                message.autoDraw = True  # Automatically draw every frame
                
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
                 
                message.autoDraw = False   
                    
            elif idx_counter> max_idx_width:
                message = visual.TextStim(win, text='shrinking horizontally', pos=[0, -60])
                message.autoDraw = True  # Automatically draw every frame
                
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
                        
                message.autoDraw = False   
                 
            # if len(kb.getKeys()) > 0: # if a key is pressed
            #     print('KEYYYYYYYY')
            #     # thisKey = kb.getKeys()
            #     # print(thisKey)
            #     break
        event.clearEvents()
        
        
        idx_counter=0
        for height in height_val:
            print(height)
            width=(360/height)*scaler
            
            idx_counter += 1
            
            # prepare stimuli
            upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), stimulus_size+(height/2)),fillColor=[1, 1, 1],lineColor=[11, 1, 1])
            upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), stimulus_size+(height/2)),fillColor=[1, 1, 1],lineColor=[1, 1, 1])
            lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(width/2), -stimulus_size-(height/2)),fillColor=[1, 1, 1],lineColor=[1, 1, 1])
            lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(stimulus_size+(width/2), -stimulus_size-(height/2)),fillColor=[1, 1, 1],lineColor=[1, 1, 1])
            stimuli = [upper_left, upper_right, lower_right, lower_left]
            
            
            if idx_counter <= max_idx_height:
                message = visual.TextStim(win, text='extending vertically', pos=[0, -120])
                message.autoDraw = True  # Automatically draw every frame
                
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
               
                        
                message.autoDraw = False   
        
        
            elif idx_counter > max_idx_height:
                message = visual.TextStim(win, text='shrinking vertically', pos=[0, -120])
                message.autoDraw = True  # Automatically draw every frame
                
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
                        
                        
                        
                message.autoDraw = False   
                 
            # if len(kb.getKeys()) > 0: # if a key is pressed
            #     print('KEYYYYYYYY')
            #     # thisKey = kb.getKeys()
            #     # print(thisKey)
            #     break
        event.clearEvents()
        
        
        
    message = visual.TextStim(win, text='End of demonstration')
    message.autoDraw = True  # Automatically draw every frame
    win.flip()
    core.wait(2.0)
    message.autoDraw = False  # Automatically draw every frame


    

    # ask participants if they want more
    while True:
        message = visual.TextStim(win, text='Would you like more demonstration? \n press y for yes \n press n for no').draw()
        #message.autoDraw = True  # Automatically draw every frame
        win.flip()
        keyPressed = kb.waitKeys()
        if keyPressed == ["y"]:
            flag_demonstration = True
            break
        elif keyPressed == ["n"]:
            message = visual.TextStim(win, text='continueing to the experimental phase')#.draw()
            message.autoDraw = True  # Automatically draw every frame
            win.flip()
            core.wait(5.0)
            message.autoDraw = False  # Automatically draw every frame
            
            flag_demonstration = False
            break













# ## EXPERIMENT PHASE ###

# # fixation cross
# fixation = visual.ShapeStim(win,
#                             vertices=((0, -0.05), (0, 0.05), (0, 0),
#                                       (-0.05, 0), (0.05, 0)),
#                             lineWidth=75,
#                             closeShape=False,
#                             lineColor="white"
#                             )


# ##
# # 1 cycle - trial: extending-shrinking square first horizontally, then vertically
# for block in range(1, block_number_experiment+1):

#     for trial in range(1, trial_number_experiment+1):
#         scaler = 1

#         width_val = []
#         result = math.sqrt(360)
#         current_value = (result)*scaler
#         start_value = current_value

#         # Add values in the increasing phase
#         while current_value <= 90*scaler:
#             width_val.append(current_value)
#             current_value += 3*scaler

#         # Subtract values in the decreasing phase
#         while current_value >= result*scaler:
#             width_val.append(current_value)
#             current_value -= 3*scaler
#         # Now, 'values' contains the desired array
#         print(width_val)

#         #
#         totalx = start_value ** 2

#         # height_val = []
#         # result=math.sqrt(360)
#         # current_value = (result)*scaler
#         # start_value=current_value

#         # # Add values in the increasing phase
#         # while current_value <= 90*scaler:
#         #     height_val.append(current_value)
#         #     current_value += 3*scaler

#         # # Subtract values in the decreasing phase
#         # while current_value >= 17.5*scaler:
#         #     height_val.append(current_value)
#         #     current_value -= 3*scaler

#         # # Now, 'values' contains the desired array
#         # print(height_val)

#         # height_val = []
#         # result=math.sqrt(360)
#         # current_value = (result)*scaler
#         # start_value=current_value

#         # # Add values in the increasing phase
#         # while current_value <= 90*scaler:
#         #     height_val.append(current_value)
#         #     current_value += 3*scaler

#         # # Subtract values in the decreasing phase
#         # while current_value >= result*scaler:
#         #     height_val.append(current_value)
#         #     current_value -= 3*scaler
#         # # Now, 'values' contains the desired array
#         # print(height_val)


#         color_quartets = [0.9, 0.9, 0.9]

#         fixation.draw()
#         win.flip()
#         core.wait(2)

#         kb.clock.reset()
#         kb.getKeys()

#         ## extending horizontally
#         for width in width_val:

#             height = (totalx/width)  # *scaler

#             # prepare stimuli
#             upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(
#                 width/2), stimulus_size+(height/2)), fillColor=color_quartets, lineColor=color_quartets)
#             upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(
#                 stimulus_size+(width/2), stimulus_size+(height/2)), fillColor=color_quartets, lineColor=color_quartets)
#             lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(
#                 width/2), -stimulus_size-(height/2)), fillColor=color_quartets, lineColor=color_quartets)
#             lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(
#                 stimulus_size+(width/2), -stimulus_size-(height/2)), fillColor=color_quartets, lineColor=color_quartets)
#             stimuli = [upper_left, upper_right, lower_right, lower_left]

#             duration = 1  # seconds
#             for i in list(range(0, duration)):

#                 # 1 second
#                 for i in list(range(0, freq)):

#                     for i in list(range(0, 3, 2)):
#                         stimuli[i].draw()
#                     win.flip()
#                     core.wait((1/freq)/2)

#                     for i in list(range(1, 4, 2)):
#                         stimuli[i].draw()
#                     win.flip()
#                     core.wait((1/freq)/2)

#             # if a key is pressed
#             if len(kb.getKeys()) > 0:
#                 print('key pressed - change of percept')
#                 idx_width_keyPress = width_val.index(width)
#                 idx_width_extend = idx_width_keyPress+1
#                 width = width_val[idx_width_extend]
#                 height = (totalx/width)  # *scaler

#                 # prepare stimuli
#                 upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(
#                     width/2), stimulus_size+(height/2)), fillColor=color_quartets, lineColor=color_quartets)
#                 upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(
#                     stimulus_size+(width/2), stimulus_size+(height/2)), fillColor=color_quartets, lineColor=color_quartets)
#                 lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(
#                     width/2), -stimulus_size-(height/2)), fillColor=color_quartets, lineColor=color_quartets)
#                 lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(
#                     stimulus_size+(width/2), -stimulus_size-(height/2)), fillColor=color_quartets, lineColor=color_quartets)
#                 stimuli = [upper_left, upper_right, lower_right, lower_left]

#                 duration = 1  # seconds
#                 for i in list(range(0, duration)):

#                     # 1 second
#                     for i in list(range(0, freq)):

#                         for i in list(range(0, 3, 2)):
#                             stimuli[i].draw()
#                         win.flip()
#                         core.wait((1/freq)/2)

#                         for i in list(range(1, 4, 2)):
#                             stimuli[i].draw()
#                         win.flip()
#                         core.wait((1/freq)/2)

#                 break

#         ## shrinking horizontally

#         width_val_shrinking = width_val[:idx_width_keyPress]
#         width_val_shrinking.reverse()

#         kb.getKeys()
#         for width in width_val_shrinking:
#             height = (totalx/width)  # *scaler

#             # prepare stimuli
#             upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(
#                 width/2), stimulus_size+(height/2)), fillColor=color_quartets, lineColor=color_quartets)
#             upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(
#                 stimulus_size+(width/2), stimulus_size+(height/2)), fillColor=color_quartets, lineColor=color_quartets)
#             lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(
#                 width/2), -stimulus_size-(height/2)), fillColor=color_quartets, lineColor=color_quartets)
#             lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(
#                 stimulus_size+(width/2), -stimulus_size-(height/2)), fillColor=color_quartets, lineColor=color_quartets)
#             stimuli = [upper_left, upper_right, lower_right, lower_left]

#             duration = 1  # seconds
#             for i in list(range(0, duration)):

#                 # 1 second
#                 for i in list(range(0, freq)):

#                     for i in list(range(0, 3, 2)):
#                         stimuli[i].draw()
#                     win.flip()
#                     core.wait((1/freq)/2)

#                     for i in list(range(1, 4, 2)):
#                         stimuli[i].draw()
#                     win.flip()
#                     core.wait((1/freq)/2)

#             # if a key is pressed
#             if len(kb.getKeys()) > 0:
#                 print('key pressed - change of percept')

#                 #needs to continue for more 1 cycle
#                 idx_width_keyPress = width_val.index(width)
#                 idx_width_shrink = idx_width_keyPress-1
#                 width = width_val_shrinking[idx_width_shrink]
#                 height = (totalx/width)  # *scaler

#                 # prepare stimuli
#                 upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(
#                     width/2), stimulus_size+(height/2)), fillColor=color_quartets, lineColor=color_quartets)
#                 upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(
#                     stimulus_size+(width/2), stimulus_size+(height/2)), fillColor=color_quartets, lineColor=color_quartets)
#                 lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(
#                     width/2), -stimulus_size-(height/2)), fillColor=color_quartets, lineColor=color_quartets)
#                 lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(
#                     stimulus_size+(width/2), -stimulus_size-(height/2)), fillColor=color_quartets, lineColor=color_quartets)
#                 stimuli = [upper_left, upper_right, lower_right, lower_left]

#                 duration = 1  # seconds
#                 for i in list(range(0, duration)):

#                     # 1 second
#                     for i in list(range(0, freq)):

#                         for i in list(range(0, 3, 2)):
#                             stimuli[i].draw()
#                         win.flip()
#                         core.wait((1/freq)/2)

#                         for i in list(range(1, 4, 2)):
#                             stimuli[i].draw()
#                         win.flip()
#                         core.wait((1/freq)/2)

#                 break

#         # calculate heights for extending vertically
#         height_val = []
#         # result=math.sqrt(360)
#         current_value = height  # (result)*scaler
#         start_value = current_value

#         # Add values in the increasing phase
#         while current_value <= 90*scaler:
#             height_val.append(current_value)
#             current_value += 3*scaler

#         # Subtract values in the decreasing phase
#         while current_value >= result*scaler:
#             height_val.append(current_value)
#             current_value -= 3*scaler
#         # Now, 'values' contains the desired array
#         print(height_val)

#         ## extending vertically
#         for height in height_val:
#             width = (totalx/height)  # *scaler

#             # prepare stimuli
#             upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(
#                 width/2), stimulus_size+(height/2)), fillColor=[1, 1, 1], lineColor=[11, 1, 1])
#             upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(
#                 stimulus_size+(width/2), stimulus_size+(height/2)), fillColor=[1, 1, 1], lineColor=[1, 1, 1])
#             lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(
#                 width/2), -stimulus_size-(height/2)), fillColor=[1, 1, 1], lineColor=[1, 1, 1])
#             lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(
#                 stimulus_size+(width/2), -stimulus_size-(height/2)), fillColor=[1, 1, 1], lineColor=[1, 1, 1])
#             stimuli = [upper_left, upper_right, lower_right, lower_left]

#             duration = 1  # seconds
#             for i in list(range(0, duration)):

#                 # 1 second
#                 for i in list(range(0, freq)):

#                     for i in list(range(0, 3, 2)):
#                         stimuli[i].draw()
#                     win.flip()
#                     core.wait((1/freq)/2)

#                     for i in list(range(1, 4, 2)):
#                         stimuli[i].draw()
#                     win.flip()
#                     core.wait((1/freq)/2)

#             # if a key is pressed
#             if len(kb.getKeys()) > 0:
#                 print('key pressed - change of percept')
#                 idx_height_keyPress = height_val.index(height)
#                 idx_height_extend = idx_height_keyPress+1
#                 height = height_val[idx_height_extend]
#                 width = (totalx/height)  # *scaler

#                 # prepare stimuli
#                 upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(
#                     width/2), stimulus_size+(height/2)), fillColor=color_quartets, lineColor=color_quartets)
#                 upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(
#                     stimulus_size+(width/2), stimulus_size+(height/2)), fillColor=color_quartets, lineColor=color_quartets)
#                 lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(
#                     width/2), -stimulus_size-(height/2)), fillColor=color_quartets, lineColor=color_quartets)
#                 lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(
#                     stimulus_size+(width/2), -stimulus_size-(height/2)), fillColor=color_quartets, lineColor=color_quartets)
#                 stimuli = [upper_left, upper_right, lower_right, lower_left]

#                 duration = 1  # seconds
#                 for i in list(range(0, duration)):

#                     # 1 second
#                     for i in list(range(0, freq)):

#                         for i in list(range(0, 3, 2)):
#                             stimuli[i].draw()
#                         win.flip()
#                         core.wait((1/freq)/2)

#                         for i in list(range(1, 4, 2)):
#                             stimuli[i].draw()
#                         win.flip()
#                         core.wait((1/freq)/2)

#                 break

#         ## shrinking vertically
#         height_val_shrinking = height_val[:idx_height_keyPress]
#         height_val_shrinking.reverse()

#         kb.getKeys()
#         for height in height_val_shrinking:
#             width = (totalx/height)  # *scaler

#             # prepare stimuli
#             upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(
#                 width/2), stimulus_size+(height/2)), fillColor=color_quartets, lineColor=color_quartets)
#             upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(
#                 stimulus_size+(width/2), stimulus_size+(height/2)), fillColor=color_quartets, lineColor=color_quartets)
#             lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(
#                 width/2), -stimulus_size-(height/2)), fillColor=color_quartets, lineColor=color_quartets)
#             lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(
#                 stimulus_size+(width/2), -stimulus_size-(height/2)), fillColor=color_quartets, lineColor=color_quartets)
#             stimuli = [upper_left, upper_right, lower_right, lower_left]

#             duration = 1  # seconds
#             for i in list(range(0, duration)):

#                 # 1 second
#                 for i in list(range(0, freq)):

#                     for i in list(range(0, 3, 2)):
#                         stimuli[i].draw()
#                     win.flip()
#                     core.wait((1/freq)/2)

#                     for i in list(range(1, 4, 2)):
#                         stimuli[i].draw()
#                     win.flip()
#                     core.wait((1/freq)/2)

#             # if a key is pressed
#             if len(kb.getKeys()) > 0:
#                 print('key pressed - change of percept')


# message = visual.TextStim(win, text='END')
# message.autoDraw = True  # Automatically draw every frame
# win.flip()
# core.wait(2.0)
# message.text = 'Did it work?'
# win.flip()
# core.wait(2.0)

# win.close()
# core.quit()
