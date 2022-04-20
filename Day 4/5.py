#generate an infinitecycle of elements from an iterable

list = [3, 5, 7, 9]
def infinite_funct(list):
    for i in list:
        return infinite_funct(list)

print(infinite_funct(list))