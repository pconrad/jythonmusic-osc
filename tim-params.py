# oscOut.py

from osc import *
from music import *        # import music library
from random import *    

def msg_1_pos_lhand(message): 
  args = message.getArguments()  # get OSC message's arguments
  print "args=",str(args)
  
  lowestExpectedValue = -0.7
  highestExpectedValue = 1.2
  
  myArg = args[0]
  myArg = max(lowestExpectedValue,min(highestExpectedValue,myArg))
  pitch = mapValue(myArg, lowestExpectedValue,highestExpectedValue, 0, 128)
  print "pitch = ", pitch
  Play.note(pitch, 0, 1000, 100)

def handshakeWithTim():
  oscOut = OscOut("169.231.139.109", 8001) 
  oscOut.sendMessage("/handshake")

if __name__=="__main__":
    handshakeWithTim()
    oscIn = OscIn( 9000 ) 
    oscIn.onInput("/1/pos/l_hand", msg_1_pos_lhand)

