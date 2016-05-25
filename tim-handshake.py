# oscOut.py

from osc import *

oscOut = OscOut("169.231.139.109", 8001) 

oscOut.sendMessage("/handshake")
