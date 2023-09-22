
#### MAIN

from psychopy.hardware import keyboard
from psychopy import core

kb = keyboard.Keyboard()

# during your trial
kb.clock.reset()  # when you want to start the timer from
keys = kb.getKeys(['right', 'left', 'quit'], waitRelease=True)
if 'quit' in keys:
    core.quit()
for key in keys:
    print(key.name, key.rt, key.duration)




##





keyPressed = event.getKeys()


if keyPressed =


##########3

from psychopy.hardware import keyboard
from psychopy import core, clock, visual

win = visual.window(fullscr = False)

kb = keyboard.Keyboard()
trialClock = core.Clock()

for i in range (4):
    # trial begins
    kb.clock.reset()  # timer (re)starts
    trialClock.reset()

    while trialClock.getTime() <  5:
        kb.getKeys(['right', 'left'])
        win.flip()

    print (kb.rt) # yields an empty list; i'd like it to print all the RT's

win.close()
core.quit()



########

from psychopy.hardware import keyboard
from psychopy import core, clock, visual

win = visual.window(fullscr = False)

kb = keyboard.Keyboard()
trialClock = core.Clock()

for i in range (4):
    # trial begins
    kb.clock.reset()  # timer (re)starts
    trialClock.reset()

    while trialClock.getTime() <  5:
        if (len(kb.getKeys(['right', 'left'])) > 0):
            t = kb.clock.getTime()
        win.flip()

    print (t) #would print the most recent RT, which is fine in my case, but that would be rounded to the frame rate

win.close()
core.quit()