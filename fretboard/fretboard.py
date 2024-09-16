#!/usr/bin/env python3

class Fretboard:
    def __init__(self, tuning, notes, fretCount = 25):
        self.tuning = tuning 
        self.fretCount = fretCount 
        self.notes = notes

    def getTuning(self):
        return self.tuning

    def getStringMap(self):
        stringMap = {} 
        for string in self.tuning:
            index = self.notes.index(string)
            stringMap[string] = []
            for fret in range(0, self.fretCount) :
                while index > 11:
                    index = index - len(self.notes)
                stringMap[string].insert(len(stringMap[string]),self.notes[index])
                index = index + 1
        return stringMap
