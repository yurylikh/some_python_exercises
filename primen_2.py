"""Print the n-th prime number"""

from sys import argv
from math import sqrt

import itertools as it


def is_prime(number):
    """Check if a number is prime or not."""
    if number in [0, 1]:
        return False
    elif number == 2:
        return True
    else: 
        odd_divisors = it.takewhile(lambda x: x < int(sqrt(number)+1),\
                                    it.count(3,2))
        for i in it.chain([2], odd_divisors):
            if number%i == 0:
                return False
        else: 
            return True 

if __name__ == '__main__':
    if len(argv)<2:
        print("*** Provide a number to find n-th prime. ***")
        raise Exception("Missing argument")
    
    n = int(argv[1])
    for num in it.count(2):
        if is_prime(num):
#            print("{} {}".format(n, num))
            n-=1
            if n == 0:
                print(num)
                break
