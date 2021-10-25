import unittest

from homework_2.custom_list import CustomList


class CustomListTest(unittest.TestCase):

    def test_add(self):
        c_l_1 = CustomList([1])
        c_l_2 = CustomList([1, 2])
        self.assertEqual([2, 2], c_l_1 + c_l_2)
        self.assertEqual([2, 2], c_l_2 + c_l_1)
        self.assertIsInstance(c_l_1 + c_l_2, CustomList)
        self.assertEqual([2], c_l_1 + c_l_1)
        self.assertEqual([2, 2], c_l_1 + [1, 2])
        self.assertIsInstance(c_l_1 + [1, 2], CustomList)
        self.assertEqual([2, 2], [1, 2] + c_l_1)
        self.assertIsInstance([1, 2] + c_l_1, CustomList)
        self.assertEqual([4, 4], [3, 2] + c_l_2)
        self.assertIsInstance([3, 2] + c_l_2, CustomList)
        self.assertEqual([4, 4], c_l_2 + [3, 2])
        self.assertIsInstance(c_l_2 + [3, 2], CustomList)
        self.assertEqual([2, 2], c_l_2 + [1])
        self.assertIsInstance(c_l_2 + [1], CustomList)
        self.assertEqual([2, 2], [1] + c_l_2)
        self.assertIsInstance([1] + c_l_2, CustomList)

    def test_sub(self):
        c_l_1 = CustomList([1])
        c_l_2 = CustomList([1, 2])
        self.assertEqual([0, -2], c_l_1 - c_l_2)
        self.assertEqual([0, 2], c_l_2 - c_l_1)
        self.assertIsInstance(c_l_1 - c_l_2, CustomList)
        self.assertEqual([0], c_l_1 - c_l_1)
        self.assertEqual([0, -2], c_l_1 - [1, 2])
        self.assertIsInstance(c_l_1 - [1, 2], CustomList)
        self.assertEqual([0, 2], [1, 2] - c_l_1)
        self.assertIsInstance([1, 2] - c_l_1, CustomList)
        self.assertEqual([2, 0], [3, 2] - c_l_2)
        self.assertIsInstance([3, 2] - c_l_2, CustomList)
        self.assertEqual([-2, 0], c_l_2 - [3, 2])
        self.assertIsInstance(c_l_2 - [3, 2], CustomList)
        self.assertEqual([0, 2], c_l_2 - [1])
        self.assertIsInstance(c_l_2 - [1], CustomList)
        self.assertEqual([0, -2], [1] - c_l_2)
        self.assertIsInstance([1] - c_l_2, CustomList)

    def test_eq(self):
        c_l_1 = CustomList([1])
        c_l_2 = CustomList([1, 2])
        self.assertEqual(False, c_l_1 == c_l_2)
        self.assertEqual(True, [1, 2] == c_l_2)
        self.assertEqual(True, [3] == c_l_2)
        self.assertEqual(True, CustomList([3]) == c_l_2)
        self.assertEqual(True, CustomList([1, 2]) == c_l_2)
        self.assertEqual(True, c_l_1 != c_l_2)
        self.assertEqual(False, c_l_2 != c_l_2)
