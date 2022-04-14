from math import sqrt
import math
import random
from urllib import response
import requests
from requests.exceptions import Timeout
import statistics
import json


class AssignmentTwo():
    #Question 1
    def is_power_of_four(num):
        if(num == 0):
            return False
        while (num != 1):
            if (num % 4 != 0):
                return False
            num = num // 4
        return True

    #Question 2
    def is_perfect_square(num):
        sq_root = int(sqrt(num))
        return (sq_root*sq_root) == num

    # #Question 3
    def guess_number():
        lower = int(input("Enter Lower Bound:- "))
        upper = int(input("Enter Upper Bound:- "))

        x = random.randint(lower, upper)
        print("\n\t You have only ", round(math.log(upper - lower + 1, 2)), "chances to guess!\n")

        #initializing the guess
        count = 0
        while count < math.log(upper - lower + 1, 2):
            count += 1
            guess = int(input("Guess a number: ")) #taking guess
            
            if x == guess:
                print("Congratulations!!! You guessed it right in ", count, "try")
                #once guessed loop breaks
                break
            elif x > guess:
                print("You guessed lower")
            elif x < guess:
                print("You guessed higher")

        if count >= math.log(upper - lower + 1, 2):
            print("\nThe number is %d" % x)
            print("\tBetter luck next time")

    #Question 4
    url = 'https://api.github.com/events'
    def web_request(url):
        try:
            res = requests.get(url)
            return res
        except requests.exceptions.RequestException as err:
                return err


    #Question 5
  
    def timeout_request(url, timeout=1):
        try:
            response = requests.get(url, timeout=timeout)
            return response
        except Timeout as err:
                raise(err)


    #Question 6
    def basic_stat(num):
        num_mean = statistics.mean(num)
        num_mode = statistics.mode(num)
        num_variance = statistics.variance(num)
        num_median = statistics.median(num)

        dict_stats = {
            'mean':num_mean,
            'mode':num_mode,
            'variance':num_variance,
            'median':num_median
        }

        return dict_stats

    #Question 7
    def get_dict_data(url):
        response = requests.get(url)
        data = response.json()
        return data