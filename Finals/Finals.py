# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 20:07:36 2021

@author: affan
"""

import random, pylab

# xVals = []
# yVals = []
# wVals = []
# for i in range(1000):
#     xVals.append(random.random())
#     yVals.append(random.random())
#     wVals.append(random.random())
# xVals = pylab.array(xVals)
# yVals = pylab.array(yVals)
# wVals = pylab.array(wVals)
# xVals = xVals + xVals
# zVals = xVals + yVals

# tVals = xVals + yVals + wVals
# pylab.plot(yVals,tVals)
# pylab.plot(xVals, zVals)
# pylab.plot(xVals, yVals)
# pylab.plot(xVals, sorted(yVals))
# pylab.plot(sorted(xVals), yVals)
# pylab.plot(sorted(xVals), sorted(yVals))

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    count = 0
    for i in range(numTrials):
        L = ['R','R','R','R','G','G','G','G']
        M = []
        for j in range(3):
            x = random.randint(0, (len(L)-1))
            M.append(L[x])
            L.remove(L[x])
        if M[0] == M[1] and M[1] == M[2]:
            count+=1
    return round(float(count/numTrials),3)

    
# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values,bins = numBins)
    if title:    
        pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.show()

# makeHistogram([], 1, "A", "B", "C")
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    result = []
    for i in range(numTrials):
        rolls = []
        L = []
        count = 1
        for j in range(numRolls):
            rolls.append(die.roll())
            if j != 0:
                if rolls[-1] == rolls[-2]:
                    count +=1
                else:
                    L.append(count)
                    count = 1
        L.append(count)
        x = max(L)
        result.append(x)
    makeHistogram(result, 10, "Run", "Longest Runs")
    return round(float(sum(result)/numTrials)) 
    
# One test case
# print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))

# A = [10, 	30, 	90, 	100, 	120, 	60]
# B = [4, 	10, 	5, 	1, 	1, 	6]
# labels = [1,2,3,4,5,6]
# pylab.plot(A,B,"bo")
# pylab.show()




    
    
    
    
    
