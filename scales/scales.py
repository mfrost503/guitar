#!/usr/bin/env python3

class Scale:
    def __init__(self, util): 
        self.patterns = {
            "major": [0,2,2,1,2,2,2,1],
            "minor": [0,2,1,2,2,1,2,2],
            "ionian":[0,2,2,1,2,2,2,1],
            "dorian":[2,2,1,2,2,2,1,2],
            "phrygian": [4,1,2,2,2,1,2,2],
            "lydian":[5,2,2,2,1,2,2,1],
            "mixolydian":[7,2,2,1,2,2,1,2],
            "aeolian":[9,2,1,2,2,1,2,2],
            "locrian": [11,1,2,2,1,2,2,2],
            "major-pentatonic": [0,2,2,3,2,3],
            "minor-pentatonic": [0,3,2,2,3,2],
            "harmonic-minor": [9,2,1,2,2,1,2,2],
            "chromatic": [0,1,1,1,1,1,1,1,1,1,1,1,1],
            "minor-blues": [0,3,2,1,1,3,2],
            "major-blues": [0,2,1,1,3,2,3]
        }

        self.util = util
        self.notes = util.getNotes()
        
    def getPattern(self, pattern):
        key = pattern.lower()
        return self.patterns[key]

    def getPatterns(self):
        return self.patterns

    def getNotes(self, note, pattern):
        scalePattern = self.getPattern(pattern)
        scaleNums = self.getIntervals(note, scalePattern)
        scaleNotes = []
        for notePosition in scaleNums:
            notePosition = self.util.adjustNote(notePosition)
            scaleNotes.insert(len(scaleNotes), self.notes[notePosition])

        return scaleNotes

    def getIntervals(self, note, pattern):
        scaleNums = []
        noteIndex = self.notes.index(note)
        if type(pattern) == str:
            pattern = self.getPattern(pattern)

        for semitones in pattern:
            noteIndex = noteIndex + semitones
            scaleNums.insert(len(scaleNums), noteIndex) 
        return scaleNums
