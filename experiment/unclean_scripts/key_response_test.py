

#

from psychopy import DlgFromDict

exp_info = {'participant_nr': ''}  # no default!
dlg = DlgFromDict(exp_info)


#

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

    print(kb.rt) # yields an empty list; i'd like it to print all the RT's

win.close()
core.quit()

