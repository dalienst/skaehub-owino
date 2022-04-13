from cmath import pi
from operator import length_hint

from cv2 import circle


def sum(num1, num2):
    return num1 + num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot be divided by zero")
    return num1 / num2

def sub(num1, num2):
    return num1 - num2

def check_leap_year(year):

    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:
        return True
    else:
        return False

def area_circle(radius):
    return (radius * radius) * pi 

def cube_volume(length):
    return(length * length * length)

def upper_case(word):
    return word

def split_name(word):
    return word

def concanc_names(first_name, last_name):
    full_name = '{} {}'.format(first_name, last_name)

    return full_name
