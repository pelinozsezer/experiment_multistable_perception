
### timing ###
kb.clock.reset()  

### key response ###
event.getKeys()
event.waitKeys()
waitKeys(maxWait=inf, keyList=None, waitRelease=True, clear=True)

# key release
import psychopy.iohub as io
from psychopy.hardware import keyboard
from psychopy.iohub import *
from psychopy.iohub.constants import EventConstants,KeyboardConstants
from psychopy.iohub.client import launchHubServer,ioHubConnection
from psychopy.data import getDateStr
from psychopy.core import getTime
#Create an ioHubConnection instance, which starts the ioHubProcess, and informs it of the requested devices and their configurations.
try:
# io=launchHubServer()
    io=ioHubConnection()
except:
# New connection fails when case there’s already an ioHubConnection, get active connection
    io = ioHubConnection.getActiveConnection()

iokeyboard=io.devices.keyboard



#in the begin routine section of the response routine
#Need to reset these events in case the participant already pressed and released one of the keys
io.clearEvents()
iokeyboard.clearEvents()

#remember the current time so that we can get RTs relative to the trial start
stime = getTime()

z_released = False
z_response_event = None

m_released = False
m_response_event = None



#In the each frame section of the response routine
z_key_releases=iokeyboard.getReleases(keys=['z'])
if z_key_releases:
    # Get first Z key release
    z_response_event=z_key_releases[0]
    z_released=True
    
m_key_releases=iokeyboard.getReleases(keys=['m'])
if m_key_releases:
    # Get first M key release
    m_response_event=m_key_releases[0]
    m_released=True