#Check if its a perfect square
from math import sqrt

def is_perfect_square(num):
    sq_root = int(sqrt(num))
    return (sq_root*sq_root) == num

print(is_perfect_square(50))
print(is_perfect_square(81))