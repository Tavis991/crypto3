# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:13:11 2019

@author: Dani
"""
import math
import random
from os import urandom

iterations = 10


def modular_power(a,b,n):
    """ computes a**b (mod n) using iterated squaring 
        assumes b is a nonnegative integer """
    binary_str=bin(b)[2:]
    result = 1
    for x in binary_str:
        result=(result**2)%n
        if x=='1':
            result=result*a%n            
    return result


def is_nonwitness(a,n,t,s):
    ''' one iteration of Miller-Rabin '''
    d = pow(a,t,n)
    if d==1 or d==n-1:
        return True
    for i in range(1,s):
        d=(d*d)%n
        if d == n-1:
            return True
    return False

def is_MR_prime(n):  
    ''' checks if n is prime by Miller-Rabin '''
    t = (n-1)//2
    s=1
    while t%2 == 0:
        t//=2
        s+=1
    for i in range(iterations):
        a = random.randint(2,n-1)
        if is_nonwitness(a,n,t,s) == False:
            return False
    return True

def random_odd(num_bytes):
    ''' generates a random odd number '''
    n = int.from_bytes(urandom(num_bytes),'little')
    if n%2==0:
        n+=1
    return n

def get_prime(size):
    ''' generates a prime number with size bytes'''
    n = random_odd(size)
    while is_MR_prime(n) == False:
        n = random_odd(size)
    return n




def main():
    print(get_prime(int(input("Enter size of prime: "))))

    
if __name__=='__main__':
    main()