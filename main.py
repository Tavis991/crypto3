# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import timeit

import numpy as np
import matplotlib.pyplot as plt
import itertools
from miller_rabin import *
import sys
import time

def print_hi(name):
    t1 = timeit.default_timer()
    size = int(input("enter size in bytes:"))
    a, p, p_num = creation(size)
    t2 = timeit.default_timer()
    print (f'p={p}')
    print ('a=', a)
    print('2 ', p_num)
    # bis = set()
    # for i in range (1,p):#test
    #     n = pow(a,i,p)
    #     bis.add(n)
    # print(f'len of nums: {len(bis)} should be = {p-1}')
    print(f' time consumed : {t2-t1}')


def byte_length(i):
    return (i.bit_length() + 7) // 8

def creation(size):
    alph = 1
    b_num = get_prime(size - alph)
    num = b_num  # generating p num for mod p, while we know p-1 divisors
    while (byte_length(num) < size):# afsghyusafjisakhfnsajiokd
        num *= 2
    num += 1
    while not is_MR_prime(num) :
        b_num = get_prime(size)
        num = b_num  # generating p num for mod p, while we know p-1 divisors
        while (byte_length(num) < size):
            num *= 2
        num += 1
    for i in range (2,num):
        if remainder_phi(i, num-1, [2, b_num]) :
            return i,num, b_num


def remainder_phi(a, phi, p_is): #finding if num is generator of p = phi + 1 mod group
    num = phi + 1
    for p in p_is :
        if pow(a, (phi) // p, num) == 1:
            return False
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
