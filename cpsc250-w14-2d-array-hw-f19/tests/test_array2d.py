import unittest
from src import array2d_hw
import numpy as np


class Array2dHWTests(unittest.TestCase):

    def setUp(self):
        self.test_array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.test_array_modified = np.array([[0, 0, 0], [0, 1, 2], [0, 2, 4]])
        self.test_array2 = np.array([[10, 10, 10], [10, 10, 10], [10, 10, 10]])
        self.test_array3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        self.test_array_modified3x4 = np.array([[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]])
        self.test_array3_clipped = np.array([[1, 2, 3, 4], [5, 6, 6, 6], [6, 6, 6, 6]])
        self.test_array2_clipped = np.array([[5, 5, 5], [5, 5, 5], [5, 5, 5]])
        self.identity3 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.identity4 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        self.identity6 = np.array(
            [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 1]])

    def test_sum_threshold_1(self):
        self.assertEqual(array2d_hw.sum_threshold_2d_array(self.test_array1, 9), 0,
                         msg="Only sum values that are greater than the threshold.")

    def test_sum_threshold_2(self):
        self.assertEqual(array2d_hw.sum_threshold_2d_array(self.test_array1, 8), 9,
                         msg="Only sum values that are greater than the threshold.")

    def test_sum_threshold_3(self):
        self.assertEqual(array2d_hw.sum_threshold_2d_array(self.test_array1, 0), 45,
                         msg="Sum of test_array1 should be 45.")

    def test_sum_threshold_4(self):
        self.assertEqual(array2d_hw.sum_threshold_2d_array(self.test_array2, 10), 0,
                         msg="Only sum values that are greater than the threshold.")

    def test_sum_threshold_5(self):
        self.assertEqual(array2d_hw.sum_threshold_2d_array(self.test_array2, 9), 90,
                         msg="Only sum values that are greater than the threshold.")

    def test_sum_threshold_6(self):
        self.assertEqual(array2d_hw.sum_threshold_2d_array(self.test_array2, 0), 90,
                         msg="Sum of test_array2 should be 90.")

    def test_sum_threshold_1(self):
        self.assertEqual(array2d_hw.sum_threshold_2d_array(self.test_array1, 9), 0,
                         msg="Only sum values that are greater than the threshold.")

    def test_modified_array(self):
        self.test_array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        array2d_hw.modify_2d_array(self.test_array1)
        np.testing.assert_equal(self.test_array1, self.test_array_modified, err_msg="Arrays not equal")
        self.test_array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_modified_array2(self):
        self.test_array3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        array2d_hw.modify_2d_array(self.test_array3)
        np.testing.assert_equal(self.test_array3, self.test_array_modified3x4, err_msg="Arrays not equal")
        self.test_array3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

    def test_clipped_array1(self):
        self.test_array3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        array2d_hw.clipping_2d_array(self.test_array3, 6)
        np.testing.assert_equal(self.test_array3, self.test_array3_clipped, err_msg="Arrays not equal")
        self.test_array3 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

    def test_clipped_array2(self):
        self.test_array2 = np.array([[10, 10, 10], [10, 10, 10], [10, 10, 10]])
        array2d_hw.clipping_2d_array(self.test_array2, 5)
        np.testing.assert_equal(self.test_array2, self.test_array2_clipped, err_msg="Arrays not equal")
        self.test_array2 = np.array([[10, 10, 10], [10, 10, 10], [10, 10, 10]])

    def test_identity_3x3(self):
        test = np.array(array2d_hw.create_identity_matrix(3))
        np.testing.assert_equal(test, self.identity3, err_msg="Arrays not equal")

    def test_identity_4x4(self):
        test = np.array(array2d_hw.create_identity_matrix(4))
        np.testing.assert_equal(test, self.identity4, err_msg="Arrays not equal")

    def test_identity_6x6(self):
        test = np.array(array2d_hw.create_identity_matrix(6))
        np.testing.assert_equal(test, self.identity6, err_msg="Arrays not equal")


if __name__ == '__main__':
    unittest.main()
