import unittest
from list import merge

class mergeListTestCase(unittest.TestCase):
    """merge_list tests"""

    def test_merge_zero_inputs(self):
         actual = list(merge())
         expected = []
         self.assertEqual(expected, actual)

def test_merge_one_empty_iterable(self):
        input1 = []
        actual = list(merge(input1))
        expected = []
        self.assertEqual(expected, actual)

def test_merge_one_nonempty_iterable(self):
        input1 = range(3)
        actual = list(merge(input1))
        expected=list(input1)
        self.assertEqual(expected, actual)

def test_merge_two_distinct_values_iterables_of_equal_size(self):
        input1 = range(3)
        input2 = range(3,6)
        actual = list(merge(input1, input2))
        expected=sorted(list(input1) + list(input2))
        self.assertEqual(expected, actual)
def test_merge_three_nondinstict_values_iterables_of_different_size(self):
        input_range1 = range(5000)
        input_range2 = range(-100, 80000)
        input_range3 = range(2, 200000)
        actual = list(merge(input_range1, input_range2, input_range3))

        expected=sorted(list(input1) + list(input2) + list(input3))
        self.assertEqual(expected, actual)
def test_from_task_description(self):

        input1 = [1, 5, 9]
        input2 = [2, 5]
        input3 = [1, 6, 10, 11]


        actual = list(merge(input1, input2, input3))

        expected = [1, 1, 2, 5, 5, 6, 9, 10, 11]
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()