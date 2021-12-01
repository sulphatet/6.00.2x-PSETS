# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 17:53:11 2021

@author: affan
"""


""" input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    
def greedySum(L, s):
    multipliers = []
    remainder = s
    for num in L:
        if num <= remainder:
            multi = remainder // num
            multipliers.append(multi)
            remainder = remainder - (num*multi)
        else:
            multipliers.append(0)
    if remainder == 0:
        return sum(multipliers)
    else:
        return 'no solution'
  
        
"""  
 Consider a list of positive (there is at least one positive) and negative 
 numbers. You are asked to find the maximum sum of a contiguous subsequence. For example,

    in the list [3, 4, -1, 5, -4], the maximum sum is 3+4-1+5 = 11
    in the list [3, 4, -8, 15, -1, 2], the maximum sum is 15-1+2 = 16

Write a function that meets the specification below.     

"""
def max_contig_sum(L):   
    lists = [[]]
    result = 0
    for i in range(len(L) + 1):
        for j in range(i):
            lists.append(L[j: i])
    for list in lists:
        if sum(list) > result:
            result = sum(list)
    return result

max_contig_sum([1,2,3])

def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    n = 0
    while True:
        if test(n) == True:
            return n
        elif test(-n) == True:
            return -n
        n += 1

#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

#### This test case prints 0 ####
def f(x):
    return x == 0
print(solveit(f))





















  