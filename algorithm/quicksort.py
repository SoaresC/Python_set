"""
快速排序
"""


def quicksort(array):
    if len(array) <= 1:
        return array

    left_sort = []
    right_sort = []

    num = array.pop()

    for i in array:
        if i <= num:
            left_sort.append(i)
        else:
            right_sort.append(i)

    return quicksort(left_sort) + [num] + right_sort


if __name__ == '__main__':
    array = [8, 2, 0, 1, 5, 6, 4, 1]
    print(quicksort(array))
