import unittest
from unittest import TestCase

from bot_for_practice.bot_for_practice import planet_answer


class TestPlanet_anwser(TestCase):
    def test_planet_answer(self):
        result = planet_answer("/planet Mars 2020/10/10")
        self.assertEqual("Pisces", result)


if __name__ == '__main__':
    unittest.main()
