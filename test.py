import unittest
import main
class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort_1(self):
        expected = [1,2,3,4,5]
        actual = main.Array([2,3,5,4,1]).bubble_sort()
        self.assertEqual(expected, actual)
    def test_bubble_sort_2(self):
        expected = [1,2,3,4,5,10,11]
        actual = main.Array([2,3,5,4,1,11,10]).bubble_sort()
        self.assertEqual(expected, actual)
    def test_bubble_sort_3(self):
        expected = [1,2,3,4,5,8,9]
        actual = main.Array([2,3,8,9,5,4,1]).bubble_sort()
        self.assertEqual(expected, actual)
    def test_bubble_sort_4(self):
        expected = [1,2,3,4,5,6,7]
        actual = main.Array([2,6,3,5,4,1,7]).bubble_sort()
        self.assertEqual(expected, actual)