"""Tests of worddict"""

import unittest

import settings
from dicts.worddict import split_dict, split_dicts


class SplitDictTests(unittest.TestCase):
    """Tests of split_dict."""

    def setUp(self):
        """Initialize."""
        words = {
                  1: ['word1', 'word2'],
                  2: ['word3', 'word4']
                }
        self.words = words
        self.wordDict = split_dict(settings.EXTRA_DICT_PATH) 

    def test_extremes(self):
        """Tests extreme cases."""
        pass

    def test_input_errors(self):
        """Tests input errors."""
        pass

    def test_general_cases(self):
        """Tests general cases."""
        self.assertEquals(type(self.words), type(self.wordDict))


class SplitDictsTests(unittest.TestCase):
    """Tests of split_dicts."""

    def setUp(self):
        """Initialize."""
        pass

    def test_extremes(self):
        """Tests extreme cases."""
        pass

    def test_input_errors(self):
        """Tests input errors."""
        pass

    def test_general_cases(self):
        """Tests general cases."""
        pass
