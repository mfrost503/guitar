#!/usr/bin/env python3

class String:
    def __init__(self, noteMapping):
        self.noteMapping = noteMapping

    def getFretsForNote(self, note):
        outOfRange = False
        workingIndex = 0
        frets = []
        while outOfRange is False:
            try:
                index = self.noteMapping.index(note, workingIndex)
                workingIndex = index + 1
                frets.insert(len(frets), index)
            except Exception:
                outOfRange = True 
        return frets

    def getNoteMapping(self):
        return self.noteMapping
