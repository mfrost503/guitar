#!/usr/bin/env python3

class Chord:
    def __init__(self, scaleNotes, scaleType, notes):
        self.notes = notes
        self.scaleNotes = scaleNotes
        self.scaleType = scaleType.lower()
        self.patterns = {
            "major": [1, 3, 5],
            "minor": [1, 3, 5],
            "sus4": [1, 4, 5],
            "sus2": [1, 2, 5],
        
        }

    def getChord(self):
        pattern = self.patterns[self.scaleType]
        chordNotes = []
        for note in pattern:
            index = note - 1
            chordNotes.insert(len(chordNotes), self.scaleNotes[index])
        return chordNotes
