from unittest import TestCase

import main


class Test(TestCase):
    def test_add_two_numbers(self):
        v = main.add_two_numbers(1, 10)
        self.assertEqual(v, 11)
