import numpy as np
def size_of_array():
    num = int(input("Number of elements in the array: "))
    arr = np.array(list(map(int, input("Elements of the array: ").strip().split())))
    return arr, arr.size, arr.size*arr.itemsize

print(size_of_array())
