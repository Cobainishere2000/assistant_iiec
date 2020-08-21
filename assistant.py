import os
import pyttsx3 as pyt
l=list()
l=['chrome','notepad','jupyter','media player', 'windows media player', 'calculator','microsoft paint','paint','file explorer','explorer','browser']
print('HELLO THERE, I am your assistant')
print("ENTER 'end' or 'no' to exit")
pyt.speak('HELLO THERE, What can I do for you')
order=input("What can I do for you: ")
while True :
    if (('end' in order) or  ('no' in order) or ('stop' in order) or ('close' in order)):
        pyt.speak("Terminating assistant")
        print("Termiating Assistant.........")
        break
    elif((("chrome" in order) or ('browser' in order  )) and (('open' in order) or ('run' in order ) or ('execute' in order))):
        pyt.speak('Opening Chrome Web Browser')
        os.system('chrome')
        pyt.speak('Anything else sir?')
        order=input('Anything else sir?')
    elif((('notepad'in order) or ('text editor' in order )) and (('open' in order) or ('run' in order ) or ('execute' in order))):
        pyt.speak("Opening Notepad")
        os.system('notepad')
        pyt.speak('Anything else sir?')
        order=input('Anything else sir?')
    elif((('atom' in order) or ("Atom" in order)) and (('open' in order) or ('run' in order ) or ('execute' in order))):
        pyt.speak("Opening Atom")
        os.system("atom")
        pyt.speak('Anything else sir?')
        order=input('Anything else sir?')
    elif((('paint'in order) or ('mspaint' in order)) and (('open' in order) or ('run' in order ) or ('execute' in order))):
        pyt.speak("Opening Microsoft Paint")
        os.system("mspaint")
        pyt.speak('Anything else sir?')
        order=input('Anything else sir?')
    elif(('calculator'in order ) and (('open' in order) or ('run' in order ) or ('execute' in order))):
        pyt.speak("Opening Calculator")
        os.system('calc')
        pyt.speak('Anything else sir?')
        order=input('Anything else sir?')
    elif((('jupyter'in order ) or ("notebook" in order) or ('jupiter' in  order)) and (('open' in order) or ('run' in order ) or ('execute' in order))):
        pyt.speak("opening Jupyter Notebook")
        os.system('jupyter notebook')
        pyt.speak('Anything else sir?')
        order=input('Anything else sir?')
    elif((('explorer'in order ) or ("File Explorer" in order) or ('files' in  order)) and (('open' in order) or ('run' in order ) or ('execute' in order))):
        pyt.speak("opening File Explorer")
        os.system('explorer')
        pyt.speak('Anything else sir?')
        order=input('Anything else sir?')
    elif((('media player'in order ) or ("windows media player" in order) or ('wmplayer' in  order)) and (('open' in order) or ('run' in order ) or ('execute' in order))):
        pyt.speak("opening Windows Media player")
        os.system('wmplayer')
        pyt.speak('Anything else sir?')
        order=input('Anything else sir?')
    else :
        print("not recognisable command try again:")
        pyt.speak("not recognisable command try again:")
        order=input()
        if (('end' in order) or  ('no' in order)):
            pyt.speak("Terminating assistant")
            print("Termiating Assistant.........")
            break
