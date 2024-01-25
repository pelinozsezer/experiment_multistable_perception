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
# screen = 0, fullscr=False, allowGUI=True # work laptop
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

experimental_values = list(range(1,101,1))
max_index = np.argmax(experimental_values)
min_index = np.argmin(experimental_values)
hxw=float(experimental_values[-1])

keyPressed_last=[]
keyPressed_1back=[]



for block in range(1, block_number_experiment+1):
    
    fixation.draw()
    win.flip()
    core.wait(2)
    
    trial = 0
    while  trial < trial_number_experiment: # trial is based on each participant's cycle. key response count?
            
        
        
        # HORIZONTALLY EXPANDING & SHRINKING
        width_val = experimental_values
        height_val = [hxw / x for x in width_val]
        flag_change=0 # to exit from horizontal
        index=9
        forward = True
        while flag_change==0: # should be 1 when there are two different key responses
        
            
            if index==9: # the very start: square and participant has to respond.
            
                width= width_val(idx)
                height= height_val(idx)
                 
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
                
                response = kb.getKeys(keyList = ['z', 'm'])
                
                while 1:
                    
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
           
                    if len(response)>0:
                        keyPressed_last = response[-1].name
                        forward = True
                        break
                

       
        
        
            else: # other trials

               width= width_val(idx)
               height= height_val(idx)
                
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
                
               response = kb.getKeys(keyList = ['z', 'm'])
                
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
                
                
            if len(response)>0: # keyPressed_last == response[-1].name
                    keyPressed_1back = keyPressed_last
                    keyPressed_last = response[-1].name
                 
                    # continue for one more index
                    if forward:
                        index =+ 1 
                        forward = False 
                    elif index == min_index:  # it can be at the mininmum already.
                        forward = False
                    else:
                        index =- 1 
                        flag_change==1
                        
                        
                    
                    width= width_val(idx)
                    height= height_val(idx)
                     
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
                             
                         
                             
                             
                             
                             
                 
              if max_index # if max boundary is reached, wait for key response - m: vertical
                
                    while idx==max_index:
                        
                        width= width_val(idx)
                        height= height_val(idx)
                         
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
                         
                         response = kb.getKeys(keyList = ['z', 'm'])
                         
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
                                 
                                 
                         if response[-1].name == ['m']: 
                             keyPressed_1back = keyPressed_last
                             keyPressed_last = response[-1].name

                            #if they are diff 
                             forward = False 

                         
                            
                if idx==min_index: # if min boundary is reached, wait for key response - z: vertical
                    width= width_val(idx)
                    height= height_val(idx)
                     
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
                             
                    response = kb.getKeys(keyList = ['z', 'm'])
                     
                    if response[-1].name == ['z']: 
                        keyPressed_1back = keyPressed_last
                        keyPressed_last = response[-1].name
                    
                        flag_change==1 
               
                
        if forward:
            index =+ 1 # forward
        else:
            index =- 1 # reverse                   
           
       
           
       
            
        # # VERTICALLY EXPANDING & SHRINKING
        # height_val = experimental_values
        # width_val = [hxw / x for x in height_val]
        # flag_change=0 # to exit from horizontal
        # idx=9
        # while flag_change==0: # should be 1 when there are two different key responses
      
      



      

################
      
        
        dynamical_experimental_values = dynamical_experimental_values[:idx]
        dynamical_experimental_values.reverse()
        
        
      
        

            
            














