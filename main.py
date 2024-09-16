#!/usr/bin/env python3
    
from scales import scales
from chord import chord
from utils import utils
from fretboard import fretboard
from string import string

# getting our instances 
util = utils.Utils()
notes = util.getNotes()
s = scales.Scales(notes, util)
tuning = util.getTuning("standard")
fretboard = fretboard.Fretboard(tuning, notes)
noteMapping = fretboard.getStringMap()
    
        
exitStatus = False

# getting user input
note = input("Enter a note: ")


while exitStatus is False:
    ## What would you like to do?
    ## Available actions:
    ##  - show scale notes
    ##  - show notes of a particular chord
    ##  - show tabs of a scale
    action = input("What would you like to do?: ")
    if action.lower() == 'help':
        print("  * scale-notes - show all the notes of the scale\n  * chord-notes - show all notes of a provided chord\n")

    if action.lower() == 'exit':
        exitStatus = True

    if action.lower() == 'scale-notes':
        scale = input("What scale would you like? (Key of " + note + "): ")
        scaleNotes = s.getScaleNotes(note, scale)
        print(scaleNotes)

    if action.lower() == 'change-note':
        note = input("Enter a note: ")

    if action.lower() == 'fret-position':
        strings = []
        for strg in tuning:
            strings.insert(len(strings), string.String(noteMapping[strg]))

        for st in strings[::-1]:
            frets = st.getFretsForNote(note)
            tabOutput = "----"
            for fret in frets:
                tabOutput += str(fret) + '----'

            print(tabOutput)
