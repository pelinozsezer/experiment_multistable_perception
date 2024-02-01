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

import time
start_time = time.perf_counter()


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


# DATA SAVING
experiment_folder_path = '/Users/pelinozsezer/Desktop/EXP1_MP/experiment'
experiment_file_name = 'experiment_data.csv'


## PARAMETERS ##
scaler = 1

block_number_experiment = 1
cycle_number_experiment = 10  # redefine based on participants' responses

# MQ parameters
stimulus_size = 10*scaler
freq = 2  # 1 cycle or freq is when all the quartets have been shown per second
duration = 1  # for how many seconds the quartets of the same AR will be shown
# height
# width


### EXPERIMENTAL PHASE ###

# fixation cross
fixation = visual.ShapeStim(win,
                            vertices=((0, -10), (0, 10), (0, 0),
                                      (-10, 0), (10, 0)),
                            lineWidth=65,
                            closeShape=False,
                            lineColor="white"
                            )


experimental_values = list(np.arange(2.4, 8, 0.1)) + list(range(8, 65, 1))
square_values_index = experimental_values.index(8)

max_index = np.argmax(experimental_values)
min_index = np.argmin(experimental_values)
hxw = float(experimental_values[-1])

width_val = experimental_values
height_val = [hxw / x for x in width_val]

# result = [a / b for a, b in zip(height_val, width_val)]
# print(result) # see aspect ratios


flag_continue1more = False

for block in range(1, block_number_experiment+1):
    print('block:', block)

    experiment_block_no = []
    experiment_cycle_no = []
    experiment_AR = []
    direction = []
    key_response = []

    keyPressed_last = []
    keyPressed_1back = []

    fixation.draw()
    win.flip()
    core.wait(2)

    cycle = 0

    index = square_values_index
    forward = []
    cycle_start = True
    flag_forward = []

    while cycle < cycle_number_experiment:  # trial is based on each participant's cycle==key response count=2

          cycle += 1  # placement should it be at the end within flag_change loop
          print('CYCLE increase')
          print('cycle number:', cycle)

          # EXPANDING & SHRINKING
          key_couple_1 = []
          key_couple_2 = []
          # to exit 1 cycle: 2 key responses and they must be different, if not reached to the extremes (min & max)?
          flag_change = 0
          while flag_change == 0:  # should be 1 when there are two different key responses
              print('index:', index)

              # the very start: square and participant has to respond. 10 (width) x 10 (height) = 100 (hxw)
              if cycle_start == True:
                  index = square_values_index
                  cycle_start = False

                  width = width_val[index]
                  height = height_val[index]
                  AR = height/width

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

                  event.getKeys(keyList=['z', 'm'])  # memory resets here!
                  #event.clock.reset()

                  while 1:  # first_cycle==True:

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

                      response = event.getKeys(keyList=['z', 'm'])

                      if len(response) > 0:
                          check_key_response = True
                          print('key press at first trial')
                          print("Response:", response)
                          #first_cycle=False

                          if response[-1] == 'z':  # horizontal - LR
                              forward = True
                              flag_direction = 3  # for data saving
                              keyPressed_last = response[-1]
                              key_couple_1 = response[-1]
                              print('z at first trial')

                              break

                          elif response[-1] == 'm':  # vertical - UD
                              forward = False
                              flag_direction = 2  # for data saving
                              keyPressed_last = response[-1]
                              key_couple_1 = response[-1]
                              print('m at first trial')

                              break

              ## CHECK FOR EXTREME BOUNDARIES
              elif index == max_index:  # if max boundary is reached, wait for key response - m: vertical
                  print('max index')

                  while 1:

                      width = width_val[index]
                      height = height_val[index]
                      AR = height/width

                      # prepare stimuli
                      upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(
                          width/2), stimulus_size+(height/2)), fillColor=color_quartets, lineColor=color_quartets)
                      upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(
                          stimulus_size+(width/2), stimulus_size+(height/2)), fillColor=color_quartets, lineColor=color_quartets)
                      lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(
                          width/2), -stimulus_size-(height/2)), fillColor=color_quartets, lineColor=color_quartets)
                      lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(
                          stimulus_size+(width/2), -stimulus_size-(height/2)), fillColor=color_quartets, lineColor=color_quartets)
                      stimuli = [upper_left, upper_right,
                                 lower_right, lower_left]

                      event.getKeys(keyList=['z', 'm'])

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

                      response = event.getKeys(keyList=['z', 'm'])

                      flag_direction = 4  # for data saving

                      if len(response) > 0:
                          check_key_response = True
                          if response[-1] == 'm':
                              keyPressed_1back = keyPressed_last
                              keyPressed_last = response[-1]
                              forward = False
                              if key_couple_1 == [] and key_couple_2 == []:
                                  key_couple_1 = response[-1]
                              elif (key_couple_1 != [] and key_couple_2 == []) and key_couple_1 != response[-1]:
                                  key_couple_2 = response[-1]

                              break

              elif index == min_index:  # if min boundary is reached, wait for key response - z: vertical
                  print('min index')

                  while 1:

                      width = width_val[index]
                      height = height_val[index]
                      AR = height/width

                      # prepare stimuli
                      upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(
                          width/2), stimulus_size+(height/2)), fillColor=color_quartets, lineColor=color_quartets)
                      upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(
                          stimulus_size+(width/2), stimulus_size+(height/2)), fillColor=color_quartets, lineColor=color_quartets)
                      lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(
                          width/2), -stimulus_size-(height/2)), fillColor=color_quartets, lineColor=color_quartets)
                      lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(
                          stimulus_size+(width/2), -stimulus_size-(height/2)), fillColor=color_quartets, lineColor=color_quartets)
                      stimuli = [upper_left, upper_right,
                                 lower_right, lower_left]

                      event.getKeys(keyList=['z', 'm'])

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

                      response = event.getKeys(keyList=['z', 'm'])

                      flag_direction = 5  # for data saving

                      if len(response) > 0:
                          check_key_response = True
                          if response[-1] == 'z':
                              keyPressed_1back = keyPressed_last
                              keyPressed_last = response[-1]
                              forward = True
                              if key_couple_1 == [] and key_couple_2 == []:
                                  key_couple_1 = response[-1]
                              elif (key_couple_1 != [] and key_couple_2 == []) and key_couple_1 != response[-1]:
                                  key_couple_2 = response[-1]
                              #flag_change=1 #???
                              break

              else:  # other than the very start & extremes

                  width = width_val[index]
                  height = height_val[index]
                  AR = height/width

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

                  event.getKeys(keyList=['z', 'm'])  # memory resets here!
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

                  response = event.getKeys(keyList=['z', 'm'])

                  if response == []:
                      check_key_response = False
                      print('key response: NO')

                  elif len(response) > 0:  # OR response.size > 0 # check if there is a key response
                      check_key_response = True
                      print('key response')
                      keyPressed_1back = keyPressed_last
                      keyPressed_last = response[-1]

                      # for counting cycles
                      if key_couple_1 == [] and key_couple_2 == []:
                          key_couple_1 = response[-1]
                      elif (key_couple_1 != [] and key_couple_2 == []) and key_couple_1 != response[-1]:
                          key_couple_2 = response[-1]

                      # the last two key presses must be different to count as a cycle & for change of direction (forward)
                      if keyPressed_1back != keyPressed_last:
                          print('last two key responses are different')
                          if forward == True:
                              flag_direction = 2  # for data saving
                              forward = False
                              flag_continue1more = True
                              #flag_change=1 #??? record number of responses for each cycle
                          elif forward == False:
                              flag_direction = 3  # for data saving
                              forward = True
                              flag_continue1more = True
                              #flag_change=1 #???

                      else:  # if the last two key presses are the same: no change of direction
                          flag_continue1more = False
                          # 'forward' variable will stay the same

                      if flag_continue1more:  # after key response show stimuli for one more 'duration'
                          print('flag_continue1more')

                          if forward == False:  # show forward direction one more
                              index += 1

                              width = width_val[index]
                              height = height_val[index]

                              # prepare stimuli
                              upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(
                                  width/2), stimulus_size+(height/2)), fillColor=color_quartets, lineColor=color_quartets)
                              upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(
                                  stimulus_size+(width/2), stimulus_size+(height/2)), fillColor=color_quartets, lineColor=color_quartets)
                              lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(
                                  width/2), -stimulus_size-(height/2)), fillColor=color_quartets, lineColor=color_quartets)
                              lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(
                                  stimulus_size+(width/2), -stimulus_size-(height/2)), fillColor=color_quartets, lineColor=color_quartets)
                              stimuli = [upper_left, upper_right,
                                         lower_right, lower_left]

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

                          elif forward == True:  # show non-forward/reverse direction one more
                              index -= 1

                              width = width_val[index]
                              height = height_val[index]

                              # prepare stimuli
                              upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size-(
                                  width/2), stimulus_size+(height/2)), fillColor=color_quartets, lineColor=color_quartets)
                              upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(
                                  stimulus_size+(width/2), stimulus_size+(height/2)), fillColor=color_quartets, lineColor=color_quartets)
                              lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size-(
                                  width/2), -stimulus_size-(height/2)), fillColor=color_quartets, lineColor=color_quartets)
                              lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(
                                  stimulus_size+(width/2), -stimulus_size-(height/2)), fillColor=color_quartets, lineColor=color_quartets)
                              stimuli = [upper_left, upper_right,
                                         lower_right, lower_left]

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
                  index += 1  # forward
                  print('increase index')
              else:
                  index -= 1  # reverse
                  print('decrease index')

              # CHANGING CYCLE/TRIAL - if the last two key responses are different
              # if (len(keyPressed_1back)>0 and len(keyPressed_last)>0) and (keyPressed_1back != keyPressed_last) and (flag_couple_key_response_reset==True):
              if (key_couple_1 != [] and key_couple_2 != []) and (key_couple_1 != key_couple_2):
                  print('flag change to 1')
                  flag_change = 1

              # Data saving to memory for each block
              experiment_block_no = experiment_block_no + [block]
              experiment_cycle_no = experiment_cycle_no + [cycle]
              experiment_AR = experiment_AR + [AR]

              # for data saving
              if flag_direction == 1:
                  direction = direction + ['very start']
              elif flag_direction == 2:
                  direction = direction + ['increasing']
              elif flag_direction == 3:
                  direction = direction + ['decreasing']
              elif flag_direction == 4:
                  direction = direction + ['max index']
              elif flag_direction == 5:
                  direction = direction + ['min index']

              if check_key_response == False:
                  key_response = key_response + [['']]
              elif check_key_response == True:
                  key_response = key_response + [keyPressed_last]

      # SAVE DATA TO CSV FILE for each block
    if block == 1:
          df = pd.DataFrame({'block': experiment_block_no, 'cycle': experiment_cycle_no,
                            'AR': experiment_AR, 'direction': direction, 'key_response': key_response})
          experiment_full_file_path = experiment_folder_path + '/' + experiment_file_name
          df.to_csv(experiment_full_file_path, index=False)
          print(f"Data saved to '{experiment_full_file_path}'")

    else:
          new_df = pd.DataFrame({'block': experiment_block_no, 'cycle': experiment_cycle_no,
                                'AR': experiment_AR, 'direction': direction, 'key_response': key_response})
          experiment_full_file_path = experiment_folder_path + '/' + experiment_file_name
          new_df.to_csv(experiment_full_file_path,
                        mode='a', header=False, index=False)
          print(f"Data saved to '{experiment_full_file_path}'")


elapsed_time = time.perf_counter() - start_time
print(f"The experiment took {elapsed_time} seconds")
