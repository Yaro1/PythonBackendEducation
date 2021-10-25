import unittest

from homework_2.custom_list import CustomList


class CustomListTest(unittest.TestCase):

    def test_add(self):
        c_l_1 = CustomList([1])
        c_l_2 = CustomList([1, 2])
        # self.assertEqual([2, 2], c_l_1 + c_l_2)
        # self.assertEqual([2, 2], c_l_2 + c_l_1)
        # self.assertEqual([2], c_l_1 + c_l_1)
        # self.assertEqual([2, 2], c_l_1 + [1, 2])
        self.assertEqual([2, 2], [1, 2] + c_l_1)
        self.assertEqual([4, 4], [3, 2] + c_l_2)
        self.assertEqual([4, 4], c_l_2 + [3, 2])
        self.assertEqual([2, 2], c_l_2 + [1])
        self.assertEqual([2, 2], [1] + c_l_2)
