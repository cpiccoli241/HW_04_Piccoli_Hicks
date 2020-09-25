"""
 :author: Chris Piccoli
 :date: 9/17/2020
"""
import numpy as np
from BirdBathFunction_425_v420 import BirdbathFunc425
from BirdBathFunction_448_v420 import BirdbathFunc448
from random import random
from matplotlib import pyplot as py

def stochGradientDescent(func, initialRoll = 0, initialTilt = 0, initialTwist = 0, learningRate = 1, stepsize = 4, steps = 100000):


    bestRoll = initialRoll
    bestTilt = initialTilt
    bestTwist = initialTwist

    nextRoll = initialRoll + (random()*2-1)*stepsize
    nextTilt = initialTilt + (random()*2-1)*stepsize
    nextTwist = initialTwist + + (random()*2-1)*stepsize

    volumePrev = func(initialRoll, initialTilt, initialTwist)
    volumeNext = func(nextRoll, nextTilt, nextTwist)

    volumeBest = volumePrev

    if volumeBest < volumeNext:
        bestRoll = nextRoll
        bestTilt = nextTilt
        bestTwist = nextTwist
        volumeBest = volumeNext

    while volumeBest + 5/(10**(3)) < 0.5:

        # This is the gradient
        derivRoll = (volumeNext-volumePrev)/(nextRoll - initialRoll)
        derivTilt = (volumeNext - volumePrev) / (nextTilt - initialTilt)
        derivTwist = (volumeNext - volumePrev) / (nextTwist - initialTwist)

        # reset some data
        initialRoll = nextRoll
        initialTilt = nextTilt
        initialTwist = nextTwist

        # find the next point
        nextRoll = nextRoll+learningRate*derivRoll
        nextTilt = nextTilt+learningRate*derivTilt
        nextTwist = nextTwist + learningRate*derivTwist

        volumeNext = func(nextRoll, nextTilt, nextTwist)

        if volumeNext > volumeBest:
            bestRoll = nextRoll
            bestTilt = nextTilt
            bestTwist = nextTwist
            volumeBest = volumeNext

        # pick a random point
        nextRoll = initialRoll + (random() * 2 - 1) * stepsize
        nextTilt = initialTilt + (random() * 2 - 1) * stepsize
        nextTwist = initialTwist + + (random() * 2 - 1) * stepsize

        volumeNext = func(nextRoll, nextTilt, nextTwist)

        # maybe its better I probably shouldnt do this though
        if volumeNext > volumeBest:
            bestRoll = nextRoll
            bestTilt = nextTilt
            bestTwist = nextTwist
            volumeBest = volumeNext



        # print(volumeBest)

    print(bestRoll, bestTilt, bestTwist)
    print(volumeBest)
    return [bestRoll, bestTilt, bestTwist]


def gradientDescentTESTER(func, initialRoll=0, initialTilt=0, initalTwist=0):
    best = 0
    bestRoll = initialRoll
    bestTilt = initialTilt
    bestTwist = initalTwist

    prev = 0

    delta = 5

    # stop trying when delta approaches 0
    # I found this value of delta gave me a return value > .499 for 425
    # brute-forcing 425 with many many values gave me .5 so it's accurate
    while delta >= .01:
        # store return value and params as [( returnValue, roll, tilt, twist )]
        funcValuesParams = []
        for rollDelta in range(-1, 1):
            for tiltDelta in range(-1, 1):
                for twistDelt in range(-1, 1):

                    # brute force try the function with each set of parameters
                    value = func(bestRoll + (delta*rollDelta), bestTilt + (delta*tiltDelta), bestTwist + (delta+twistDelt))

                    # save what's returned
                    funcValuesParams.append((value, rollDelta, tiltDelta, twistDelt))

        # sort the list so the tuple with the highest return value is first
        funcValuesParams.sort(key=lambda x: x[0], reverse=True)

        # grab the tuple
        bestParams = funcValuesParams[0]
        best = bestParams[0]

        # adjust the variables based on if parameters changed
        bestRoll += bestParams[1] * delta
        bestTilt += bestParams[2] * delta
        bestTwist += bestParams[3] * delta

        # if the best value hasn't changed for two iterations, decrease delta
        prevprev = prev
        prev = best
        prevprev = prev

        if prevprev == best:
            delta = delta / 2




    return best


def gradientDescentTest(start1, start2, start3, delta=.1, steps=100000, func = BirdbathFunc425):
    '''
    Okay so I just want to try optimizing one point on the sphere
    :param start1:
    :param delta:
    :param steps:
    :return: list of all the steps taken
    '''
    point1 = start1
    point2 = start1 + delta

    volumeLast = func( point1, start2, start3 )
    volumeNext = func( point2, start2, start3)

    if volumeLast < volumeNext:
        point1 = point2 + delta
        volumeLast = volumeNext
        volumeNext = func(point1, start2, start3)
    elif volumeLast > volumeNext:
        point1 = point1 - delta
        volumeLast = volumeNext
        volumeNext = func(point1, start2, start3)

    volumes = []

    for i in range(0, steps):
        if volumeLast < volumeNext:
            point1 += delta
            volumeLast = volumeNext
            volumeNext = BirdbathFunc425(point1, start2, start3)
        elif volumeLast > volumeNext:
            point1 += point1 - delta
            volumeLast = volumeNext
            volumeNext = BirdbathFunc425(point1, start2, start3)
        else:
            return volumes

        volumes.append(volumeNext)

    return volumes


def justSee(func, delta = .1, steps = 10000, start2 = 0, start3 = 0):
    l = []
    for i in range(0, steps):
        l.append(func(i*delta, start2, start3))

    py.plot(np.arange(0, steps), l)
    py.show()



def main():
    best448 = 0
    best425 = 0

    '''
    for roll in range(0, 18):
        for twist in range(0, 18):
            for tilt in range(0, 18):
                output = gradientDescentTESTER(BirdbathFunc448, roll*80, twist*80, tilt*80)
                if output > best448:
                    best448 = output
                print(roll, twist, tilt)
    '''

    stochGradientDescent(BirdbathFunc425)
    stochGradientDescent(BirdbathFunc448)

    # print(best425, best448)

if __name__ == '__main__':
    main()