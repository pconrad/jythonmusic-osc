# oscOut.py

from osc import *

def head(message):      
  print "Got /1/vel/head"
  args = message.getArguments()  # get OSC message's arguments
  print "args=",str(args)

def handshakeWithTim():
  oscOut = OscOut("169.231.139.109", 8001) 
  oscOut.sendMessage("/handshake")

if __name__=="__main__":
    handshakeWithTim()
    oscIn = OscIn( 8000 ) 
    oscIn.onInput("/1/vel/head", simple)
  
