from unittest import TestCase
import qs_check


class TestJoke(TestCase):
    def test_is_string(self):
        s = qs_check.joke()
        self.assertTrue(isinstance(s, basestring))

