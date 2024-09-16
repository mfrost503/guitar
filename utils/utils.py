#!/usr/bin/env python3

class Utils:
    def __init__(self):
        self.notes = ["A", "A#/Bb", "B", "C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab"]
        self.tunings = {
            "standard": ["E", "A", "D", "G", "B", "E"],
            "drop-d": ["D", "A", "D", "G", "B", "E"],
            "half-step-down": ["D#/Eb", "G#/Ab", "C#/Db", "F#/Gb", "A#/Bb", "D#/Eb"],
	    "whole-step-down": ["D", "G", "C", "F", "A", "D"]
        } 

    def adjustNote(self, notePosition):
        if notePosition < 12:
            return notePosition
        while notePosition > 11:
            notePosition = notePosition - len(self.notes)
        return notePosition

    def getNotes(self):
        return self.notes

    def getTuning(self, key):
        return self.tunings[key]
