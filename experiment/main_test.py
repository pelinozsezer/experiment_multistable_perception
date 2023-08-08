
# Pelin Ozsezer - Experiment 1

#pip install psychopy

# import libraries
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from psychopy import core, visual, event

from psychopy.gui import DlgFromDict
from psychopy.visual import Window
from psychopy.core import Clock, quit, wait
#from psychopy.event import Mouse
#from psychopy.hardware.keyboard import Keyboard


# # Monitor - saved some settings in monitor center
# widthPix = 1792 # screen width in px
# heightPix = 1120 # screen height in px
# monitorwidth = 35.4 # monitor width in cm
# viewdist = 60. # viewing distance in cm
# monitorname = 'personal'
# scrn = 0 # 0 to use main screen, 1 to use external screen
# mon = monitor.Monitor(monitorname)

# # Initialize window
# win = visual.Window(
#     monitor=mon, 
#     size=(widthPix,heightPix),
#     color='Gray',
#     colorSpace='rgb',
#     units='deg',
#     screen=scrn,
#     allowGUI=False,
#     fullscr=True)

win = visual.Window(size=[1792, 1120]) #units="pix", screen = 0, fullscr=False, allowGUI=True) #allowGUI!

# get refresh rate
refresh_r = round(win.getActualFrameRate())
print(f"refresh rate: {refresh_r} Hz")


rect = visual.Rect(
    win=win,
    units="pix",
    width=200,
    height=100,
    fillColor=[1, -1, -1],
    lineColor=[-1, -1, 1]
)

rect.draw()

win.flip()
core.wait(3.0)


##############################################################################
# # motion quartets
# stimulus_size = 200
# stimulus_speed = 5

# upper_left = visual.Rect(win, width=stimulus_size, height=stimulus_size, pos=(-stimulus_size, stimulus_size))
# upper_right = visual.Rect(win, width=stimulus_size, height=stimulus_size, pos=(stimulus_size, stimulus_size))
# lower_left = visual.Rect(win, width=stimulus_size, height=stimulus_size, pos=(-stimulus_size, -stimulus_size))
# lower_right = visual.Rect(win, width=stimulus_size, height=stimulus_size, pos=(stimulus_size, -stimulus_size))
# stimuli = [upper_left, upper_right, lower_left, lower_right]


# for stim in stimuli:
#     stim.setPos((stim.pos[0] + stimulus_speed, stim.pos[1]))
#     stim.draw()

# win.flip()
# core.wait(5.0)
    

message = visual.TextStim(win, text='LOL')
message.autoDraw = True  # Automatically draw every frame
win.flip()
core.wait(2.0)
message.text = 'Did it work?' 
win.flip() 
core.wait(2.0)

win.close()
core.quit()






















########################


# import libraries
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from psychopy import core, visual, event

from psychopy.gui import DlgFromDict
from psychopy.visual import Window
from psychopy.core import Clock, quit, wait
#from psychopy.event import Mouse
#from psychopy.hardware.keyboard import Keyboard


# # Monitor - saved some settings in monitor center
# widthPix = 1792 # screen width in px
# heightPix = 1120 # screen height in px
# monitorwidth = 35.4 # monitor width in cm
# viewdist = 60. # viewing distance in cm
# monitorname = 'personal'
# scrn = 0 # 0 to use main screen, 1 to use external screen
# mon = monitor.Monitor(monitorname)

# # Initialize window
# win = visual.Window(
#     monitor=mon, 
#     size=(widthPix,heightPix),
#     color='Gray',
#     colorSpace='rgb',
#     units='deg',
#     screen=scrn,
#     allowGUI=False,
#     fullscr=True)

win = visual.Window(size=[1792, 1120]) #units="pix", screen = 0, fullscr=False, allowGUI=True) #allowGUI!

# get refresh rate
refresh_r = round(win.getActualFrameRate())
print(f"refresh rate: {refresh_r} Hz")

circ_stim=visual.Circle(win, radius=100,units='pix', fillColor=[1, -1, -1],lineColor=[-1, -1, 1], edges=128)
circ_stim.draw()
win.flip()
core.wait(3.0)



##############################################################################
# # motion quartets
# stimulus_size = 200
# stimulus_speed = 5

# upper_left = visual.Rect(win, width=stimulus_size, height=stimulus_size, pos=(-stimulus_size, stimulus_size))
# upper_right = visual.Rect(win, width=stimulus_size, height=stimulus_size, pos=(stimulus_size, stimulus_size))
# lower_left = visual.Rect(win, width=stimulus_size, height=stimulus_size, pos=(-stimulus_size, -stimulus_size))
# lower_right = visual.Rect(win, width=stimulus_size, height=stimulus_size, pos=(stimulus_size, -stimulus_size))
# stimuli = [upper_left, upper_right, lower_left, lower_right]


# for stim in stimuli:
#     stim.setPos((stim.pos[0] + stimulus_speed, stim.pos[1]))
#     stim.draw()

# win.flip()
# core.wait(5.0)
    

message = visual.TextStim(win, text='LOL')
message.autoDraw = True  # Automatically draw every frame
win.flip()
core.wait(2.0)
message.text = 'Did it work?' 
win.flip() 
core.wait(2.0)

win.close()
core.quit()













##############################################################################
# import libraries
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from psychopy import core, visual, event

from psychopy.gui import DlgFromDict
from psychopy.visual import Window
from psychopy.core import Clock, quit, wait
#from psychopy.event import Mouse
#from psychopy.hardware.keyboard import Keyboard


win = visual.Window(size=[1792, 1120]) #units="pix", screen = 0, fullscr=False, allowGUI=True) #allowGUI!

# get refresh rate
refresh_r = round(win.getActualFrameRate())
print(f"refresh rate: {refresh_r} Hz")

# circ_stim=visual.Circle(win, radius=100,units='pix', fillColor=[1, -1, -1],lineColor=[-1, -1, 1], edges=128)
# circ_stim.draw()
# win.flip()
# core.wait(3.0)



##############################################################################
# motion quartets
stimulus_size = 100
#stimulus_speed = 5
#distance

upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size, stimulus_size),fillColor=[1, -1, -1],lineColor=[-1, -1, 1])
upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(stimulus_size, stimulus_size),fillColor=[1, -1, -1],lineColor=[-1, -1, 1])
lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size, -stimulus_size),fillColor=[1, -1, -1],lineColor=[-1, -1, 1])
lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(stimulus_size, -stimulus_size),fillColor=[1, -1, -1],lineColor=[-1, -1, 1])
stimulix = [upper_left, upper_right, lower_left, lower_right]





#for i in stimulix
#    stimuli.draw(stimulix[i])
stimulix[0].draw(); stimulix[1].draw(); stimulix[2].draw(); stimulix[3].draw()
win.flip()
core.wait(3.0)    

message = visual.TextStim(win, text='LOL')
message.autoDraw = True  # Automatically draw every frame
win.flip()
core.wait(2.0)
message.text = 'Did it work?' 
win.flip() 
core.wait(2.0)

win.close()
core.quit()









##############################################################################
# import libraries
import os
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from psychopy import core, visual, event

from psychopy.gui import DlgFromDict
from psychopy.visual import Window
from psychopy.core import Clock, quit, wait
#from psychopy.event import Mouse
#from psychopy.hardware.keyboard import Keyboard


win = visual.Window(size=[1792, 1120]) #units="pix", screen = 0, fullscr=False, allowGUI=True) #allowGUI!

# get refresh rate
refresh_r = round(win.getActualFrameRate())
print(f"refresh rate: {refresh_r} Hz")

# circ_stim=visual.Circle(win, radius=100,units='pix', fillColor=[1, -1, -1],lineColor=[-1, -1, 1], edges=128)
# circ_stim.draw()
# win.flip()
# core.wait(3.0)



##############################################################################
# motion quartets
stimulus_size = 100
#stimulus_speed = 5
#distance

upper_left = visual.Circle(win, radius=stimulus_size, units='pix', pos=(-stimulus_size, stimulus_size),fillColor=[1, -1, -1],lineColor=[-1, -1, 1])
upper_right = visual.Circle(win,  radius=stimulus_size, units='pix', pos=(stimulus_size, stimulus_size),fillColor=[1, -1, -1],lineColor=[-1, -1, 1])
lower_left = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(-stimulus_size, -stimulus_size),fillColor=[1, -1, -1],lineColor=[-1, -1, 1])
lower_right = visual.Circle(win,   radius=stimulus_size, units='pix', pos=(stimulus_size, -stimulus_size),fillColor=[1, -1, -1],lineColor=[-1, -1, 1])
stimulix = [upper_left, upper_right, lower_left, lower_right]





#for i in stimulix
#    stimuli.draw(stimulix[i])
stimulix[0].draw(); stimulix[1].draw(); stimulix[2].draw(); stimulix[3].draw()
win.flip()
core.wait(3.0)    

message = visual.TextStim(win, text='LOL')
message.autoDraw = True  # Automatically draw every frame
win.flip()
core.wait(2.0)
message.text = 'Did it work?' 
win.flip() 
core.wait(2.0)

win.close()
core.quit()

