import unittest
from unittest import TestCase

from for_dict_challenges import maxClass


class TestMost_name(TestCase):

    def test_max_class(self):
        is_male = {
            'Маша': False,
            'Оля': False,
            'Олег': True,
            'Миша': True,
        }

        m1, f1 = maxClass([
            {'class': '2a',
             'students':
                 [{'first_name': 'Маша'},
                  {'first_name': 'Оля'},
                  {'first_name': 'Оля'}]
             }],
            is_male)

        self.assertEqual("2a", m1)


if __name__ == '__main__':
    unittest.main()
