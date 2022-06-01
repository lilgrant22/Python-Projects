import numpy as np


def modify_2d_array(array):
    """
    Given a 2d numpy array iterate through the values and set the value equal to the row*column number

    :param array: 2d numpy array
    """

    rows = array.shape[0]
    cols = array.shape[1]
    for i in range(0, rows):
        for j in range(0, cols):
            array[i, j] = (i + 1) * (j + 1)
    return

def sum_threshold_2d_array(array, threshold):
    """
    Iterate through each element of the 2d array using nested loops.
    Sum up the values that are greater than a threshold value given as an input parameter.

    :param array: a 2d array
    :param threshold: a threshold value (valid int or float)
    :return: sum total of values above the threshold
    """
    rows = array.shape[0]
    cols = array.shape[1]
    sum = 0
    for x in range(0, rows):
        for y in range(0, cols):
            if (array[x, y] > threshold):
                sum += array[x, y]
    return sum


def clipping_2d_array(array, threshold):
    """
    Iterate through each element of the 2d array using nested loops.
    Set the values greater than a threshold value equal to the threshold value given as an input parameter.

    (E.g. if the threshold is 1 and there is a value 1.5, set the value to 1 in the array)

    :param array: a 2d array
    :param threshold: a threshold value (valid int or float)
    """

    row = len(array)
    column = len(array[0])  # no. of elements in the first row
    for i in range(row):
        for j in range(column):
            if array[i][j] > threshold:
                array[i][j] = threshold

def create_identity_matrix(n):
    """
    Create a nxn sized identity matrix. The return type should be a list or numpy ndarray

    For more info: https://en.wikipedia.org/wiki/Identity_matrix

    For this exercise you can use nested loops to construct your 2d array or find an applicable function in the numpy library.

    :param n:
    :return: nxn ndarray where the diagonal elements are 1 and nondiagonal elements are 0
    """

    return np.identity(n)


if __name__ == "__main__":
    my_example_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(sum_threshold_2d_array(my_example_array, 5))
    print(clipping_2d_array(my_example_array, 5))
    print(create_identity_matrix(5))

    # Modifies existing array
    modify_2d_array(my_example_array)
    print(my_example_array)
