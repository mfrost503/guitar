#!/usr/bin/env python3

import unittest
from utils import utils

class util_test(unittest.TestCase):
    def setUp(self):
        self.utils = utils.Utils()

    def test_getNotes(self):
        notes = self.utils.getNotes()
        self.assertEqual("A", notes[0])
        self.assertEqual("B", notes[2])
        self.assertEqual("G", notes[10])

    def test_getStandardTuning(self):
        tuningKey = "standard"
        expectedTuning = ["E","A","D","G","B","E"]
        tuning = self.utils.getTuning(tuningKey)
        self.assertEqual(expectedTuning, tuning)

    def test_getDropDTuning(self):
        tuningKey = "drop-d"
        expectedTuning = ["D","A","D","G","B","E"]
        tuning = self.utils.getTuning(tuningKey)
        self.assertEqual(expectedTuning, tuning)

    def test_getHalfStepDownTuning(self):
        tuningKey = "half-step-down"
        expectedTuning = ["D#/Eb","G#/Ab","C#/Db","F#/Gb","A#/Bb","D#/Eb"]
        tuning = self.utils.getTuning(tuningKey)
        self.assertEqual(expectedTuning, tuning)

    def test_getWholeStepDownTuning(self):
        tuningKey = "whole-step-down"
        expectedTuning = ["D","G","C","F","A","D"]
        tuning = self.utils.getTuning(tuningKey)
        self.assertEqual(expectedTuning, tuning)

    ####
    # There are only 12 notes in Western Music, so any note position + 12
    # is an octave - however we are just looking for note names
    def test_adjustNoteOver12(self):
        notePosition = 13
        expectedNotePosition = 1
        newNotePosition = self.utils.adjustNote(notePosition)
        self.assertEqual(expectedNotePosition, newNotePosition)

    ####
    # Since there are 12 notes, if a number position is under 11 (0 - 11)
    # no adjustment needs to be made to find that note
    def test_adjustNoteUnder12(self):
        notePosition = 6
        expectedNotePosition = 6
        newNotePosition = self.utils.adjustNote(notePosition)
        self.assertEqual(expectedNotePosition, newNotePosition)
