"""
 :author: Chris Piccoli
 :date: 9/17/2020
"""
import numpy as np
from BirdBathFunction_425_v420 import BirdbathFunc425
from BirdBathFunction_448_v420 import BirdbathFunc448
from matplotlib import pyplot as py

def gradientDescentTESTER(func, initialRoll=0, initialTilt=0, initalTwist=0):
    best = 0
    bestRoll = initialRoll
    bestTilt = initialTilt
    bestTwist = initalTwist

    prev = func(bestRoll, bestTilt, bestTwist)
    prevprev = None
    delta = 5

    foundPeak = False


    while not foundPeak:
        rollUp = func(bestRoll + delta, bestTilt, bestTwist)
        rollDown = func(bestRoll - delta, bestTilt, bestTwist)

        tiltUp = func(bestRoll, bestTilt + delta, bestTwist)
        tiltDown = func(bestRoll, bestTilt - delta, bestTwist)

        twistUp = func(bestRoll, bestTilt, bestTwist + delta)
        twistDown = func(bestRoll, bestTilt, bestTwist - delta)

        if rollUp > rollDown and rollUp > tiltUp and rollUp > tiltDown and rollUp > twistUp and rollUp > twistDown:
            best = rollUp
            bestRoll += delta

        elif rollDown > rollUp and rollDown > tiltUp and rollDown > tiltDown and rollDown > twistUp and rollDown > twistDown:
            best = rollDown
            bestRoll -= delta

        elif tiltUp > rollUp and tiltUp > rollDown and tiltUp > tiltDown and tiltUp > twistUp and tiltUp > twistDown:
            best = tiltUp
            bestTilt += delta

        elif tiltDown > rollUp and tiltDown > rollDown and tiltDown > tiltUp and tiltDown > twistUp and tiltDown > twistDown:
            best = tiltDown
            bestTilt -= delta

        elif twistUp > rollUp and twistUp > rollDown and twistUp > tiltUp and twistUp > tiltDown and twistUp > twistDown:
            best = twistUp
            bestTwist += delta

        elif twistDown > rollUp and twistDown > rollDown and twistDown > tiltUp and twistDown > tiltDown and twistDown > twistUp:
            best = twistDown
            bestTwist -= delta

        else:
            foundPeak = True

        prev = best
        prevprev = prev

        if prevprev == best:
            delta = delta / 2


    print(best, bestRoll, bestTilt, bestTwist)

    print('###########################################################################################')


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
    print("Testing 448 defaults 0, 0, 0,")
    gradientDescentTESTER(BirdbathFunc448)
    print("Testing 425 defaults 0, 0, 0,")
    gradientDescentTESTER(BirdbathFunc425)


    print('Testing 425 other function', gradientDescentTest(9,2,15)[-1])

    justSee(BirdbathFunc425)

if __name__ == '__main__':
    main()