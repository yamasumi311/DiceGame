from unittest import TestCase

from functions import check_inputs


class Test_dice_gama(TestCase):
    def test_check_wrong_inputs(self):
        self.assertFalse(check_inputs('r=-'))

    def test_first_character_wrong(self):
        self.assertFalse(check_inputs('=r=-'))

    def test_short_inputs(self):
        self.assertTrue(check_inputs('r-'))

    def test_check_correct_inputs(self):
        self.assertTrue(check_inputs('r--'))
