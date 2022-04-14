import numpy as np
def size_of_array():
    num = int(input("Number of elements in the array: "))
    arr = np.array(list(map(int, input("Elements of the array: ").strip().split())))
    #return arr, arr.size, arr.size*arr.itemsize
    print("The array is: ", arr)
    print("Array size is: ", arr.size)
    print("Memory occupied by array: ", arr.size*arr.itemsize)

size_of_array()




    #return ("Array is: " + arr + "\nSize of memory occupied by array: " + arr.size*arr.itemsize)
    # return (arr, 
    #         arr.size, 
    #         arr.size*arr.itemsize)


