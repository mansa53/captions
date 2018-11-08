#!/usr/bin/env python3
#print "hello"
import os
from gtts import gTTS

f=open('out1.txt')
lines=f.readlines()
language='en'
print("The captions are:") 
voice1=lines[7]
print(voice1)
voice2=lines[8]
print(voice2)

#os.system("espeak '{}'".format(voice2))
#os.system("espeak  -v mb+f1 -p99 -s200' {}'".format(voice2))
myobj = gTTS(text=voice1, lang=language, slow=False) 
myobj1 = gTTS(text=voice2, lang=language, slow=False) 
#myobj2 = gTTS(text=voice3, lang=language, slow=False) 
#myobj.save("welcome2.mp3") 
myobj1.save("welcome1.mp3")
#myobj2.save("welcome.mp3")
  
# Playing the converted file 
#os.system("mpg321 welcome2.mp3")
os.system("mpg321 welcome1.mp3")
#os.system("mpg321 welcome2.mp3")


