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
cycle_number_experiment = 25 # redefine based on participants' responses

# MQ parameters
stimulus_size =  10*scaler
freq = 2  # 1 cycle or freq is when all the quartets have been shown per second
duration = 1 # for how many seconds the quartets of the same AR will be shown
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

width_val = experimental_values
height_val = [hxw / x for x in width_val]

keyPressed_last=[]
keyPressed_1back=[]

number_keyPressed=[]

flag_continue1more=False

for block in range(1, block_number_experiment+1):
    
     fixation.draw()
     win.flip()
     core.wait(2)
    
     cycle = 0
     number_keyPressed=0
     
     flag_change=0 # to exit 1 cycle: 2 key responses and they must be different, if not reached to the extremes (min & max)?
     index=9
     forward = []

     while  cycle < cycle_number_experiment: # trial is based on each participant's cycle==key response count=2

         # EXPANDING & SHRINKING 
         while flag_change==0: # should be 1 when there are two different key responses

             if index==9: # the very start: square and participant has to respond. 10 (width) x 10 (height) = 100 (hxw)

                 width= width_val[index]
                 height= height_val[index]
                 
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
                
                 event.getKeys(keyList = ['z', 'm']) # memory resets here!
                 #event.clock.reset()

                 while 1:
                    
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
           
                     response = event.getKeys(keyList = ['z', 'm'])
                     
                     if len(response)>0:
                         print('keyyyyy')
                         print(response)

                         if response[-1] == ['z']: # horizontal - LR
                             forward = True
                             keyPressed_last = response[-1]   
                             print('z')
                             flag_change=1 #???
                             break

                         elif response[-1] == ['m']: # vertical - UD
                             forward = False
                             keyPressed_last = response[-1]  
                             print('m')
                             flag_change=1 #???
                             break







             ## CHECK FOR EXTREME BOUNDARIES
             elif index == max_index: # if max boundary is reached, wait for key response - m: vertical
                 
                 while 1:

                     width= width_val[index]
                     height= height_val[index]
                         
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
                     
                     kb.getKeys(keyList = ['z', 'm'])
                     
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
                             
                     if response[-1].name == ['m']: 
                         keyPressed_1back = keyPressed_last
                         keyPressed_last = response[-1].name
                         forward = False 
                         flag_change=1 #???
                         break



             elif index==min_index: # if min boundary is reached, wait for key response - z: vertical
                 while 1:

                     width= width_val[index]
                     height= height_val[index]
                     
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
                     
                     kb.getKeys(keyList = ['z', 'm'])
                     
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
                         forward = True 
                         flag_change=1 #???
                         break








             else: # other than the very start & extremes

                 width= width_val[index]
                 height= height_val[index]
                 
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

                 kb.getKeys(keyList = ['z', 'm']) # memory resets here!
                 kb.clock.reset()

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

                 if len(response)>0: # OR response.size > 0 # check if there is a key response
                     keyPressed_1back = keyPressed_last
                     keyPressed_last = response[-1].name

                     if keyPressed_1back != keyPressed_last: # the last two key presses must be different to count as a cycle & for change of direction (forward)
                         if forward==True:
                             forward=False
                             flag_continue1more=True
                             flag_change=1 #??? record number of responses for each cycle
                         elif forward==False:
                             forward=True
                             flag_continue1more=True
                             flag_change=1 #???

                     else: # if the last two key presses are the same: no change of direction
                         continue # 'forward' variable will stay the same




                     if flag_continue1more: # after key response show stimuli for one more 'duration'

                         if forward==False: # show forward direction one more
                             index =+ 1

                             width= width_val[index]
                             height= height_val[index]
            
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



                         elif forward==True: # show non-forward/reverse direction one more
                             index =- 1

                             width= width_val[index]
                             height= height_val[index]
           
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
















                 # CHECK WHETHER WIDTH SHOULD INCREASE OR DECREASE
                 if forward:
                     index =+ 1 # forward
                 else:
                     index =- 1 # reverse  



        

















