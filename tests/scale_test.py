#!/usr/bin/env python3

import unittest
from utils import utils
from scales import scales

class TestScales(unittest.TestCase):

    def setUp(self):
        self.util = utils.Utils()
        self.scale = scales.Scale(self.util)

    def test_getSinglePattern(self):
        patterns = self.scale.getPatterns()
        patternKey = "major"
        expectedPattern = patterns[patternKey]
        fetchedPattern = self.scale.getPattern(patternKey)
        self.assertEqual(expectedPattern, fetchedPattern)

    def test_getCMajorScale(self):
        expectedScale = ["C", "D", "E", "F", "G", "A", "B", "C"]
        retrievedScale = self.scale.getNotes("C", "major")
        self.assertEqual(expectedScale, retrievedScale)

    def test_getMajorScaleIntervals(self):
        expectedInterval = [3, 5, 7, 8, 10, 12, 14, 15]
        retrievedInterval = self.scale.getIntervals("C", "major")
        self.assertEqual(expectedInterval, retrievedInterval)
