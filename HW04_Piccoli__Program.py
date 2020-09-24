"""
 :author: Chris Piccoli
 :date: 9/17/2020
"""
import numpy as np
from BirdBathFunction_425_v420 import BirdbathFunc425
from BirdBathFunction_448_v420 import BirdbathFunc448

def gradientDescentTESTER():
    # best = 0
    # bestRoll = 0
    # bestTwist = 0
    # bestTilt = 0
    # for roll in range(-10, 100):
    #     for tilt in range(-10, 100):
    #         for twist in range(-10, 100):
    #             print(roll, tilt, twist)
    #             nn = BirdbathFunc448(roll, tilt, twist)
    #             if nn > best:
    #                 best = nn
    #                 bestRoll = roll
    #                 bestTilt = tilt
    #                 bestTwist = twist
    # print(best, bestRoll, bestTilt, bestTwist)
    # 0.4983496320637728 -8 -5 31

    best = 0
    bestRoll = 0
    bestTilt = 0
    bestTwist = 0

    prev = BirdbathFunc448(bestRoll, bestTilt, bestTwist)
    prevprev = None
    delta = 5

    foundPeak = False

    bests = []

    while not foundPeak:
        rollUp = BirdbathFunc448(bestRoll + delta, bestTilt, bestTwist)
        rollDown = BirdbathFunc448(bestRoll - delta, bestTilt, bestTwist)

        tiltUp = BirdbathFunc448(bestRoll, bestTilt + delta, bestTwist)
        tiltDown = BirdbathFunc448(bestRoll, bestTilt - delta, bestTwist)

        twistUp = BirdbathFunc448(bestRoll, bestTilt, bestTwist + delta)
        twistDown = BirdbathFunc448(bestRoll, bestTilt, bestTwist - delta)

        if rollUp > rollDown and rollUp > tiltUp and rollUp > tiltDown and rollUp > twistUp and rollUp > twistDown:
            best = rollUp
            bestRoll += delta
            print("roll up")

        elif rollDown > rollUp and rollDown > tiltUp and rollDown > tiltDown and rollDown > twistUp and rollDown > twistDown:
            best = rollDown
            bestRoll -= delta
            print("roll down")

        elif tiltUp > rollUp and tiltUp > rollDown and tiltUp > tiltDown and tiltUp > twistUp and tiltUp > twistDown:
            best = tiltUp
            bestTilt += delta
            print("tilt up", tiltUp, tiltDown)

        elif tiltDown > rollUp and tiltDown > rollDown and tiltDown > tiltUp and tiltDown > twistUp and tiltDown > twistDown:
            best = tiltDown
            bestTilt -= delta
            print("tilt down", tiltUp, tiltDown)

        elif twistUp > rollUp and twistUp > rollDown and twistUp > tiltUp and twistUp > tiltDown and twistUp > twistDown:
            best = twistUp
            bestTwist += delta
            print("twist up", twistUp, twistDown)


        elif twistDown > rollUp and twistDown > rollDown and twistDown > tiltUp and twistDown > tiltDown and twistDown > twistUp:
            best = twistDown
            bestTwist -= delta
            print("twist down", twistUp, twistDown)


        else:
            foundPeak = True

        prev = best
        prevprev = prev

        if prevprev == best:
            delta = delta / 2

        # print(best)
        print(best, bestRoll, bestTilt, bestTwist)
        print('vars:', rollUp, rollDown, twistUp, twistDown, tiltUp, tiltDown)

    print(best, bestRoll, bestTilt, bestTwist)

    print('###########################################################################################')
    return bests


def gradientDescentTest(start1, start2, start3, delta=.1, steps=100000):
    '''
    Okay so I just want to try optimizing one point on the sphere
    :param start1:
    :param delta:
    :param steps:
    :return: list of all the steps taken
    '''
    point1 = start1
    point2 = start1 + delta

    volumeLast = BirdbathFunc425( point1, start2, start3 )
    volumeNext = BirdbathFunc425( point2, start2, start3)

    if volumeLast < volumeNext:
        point1 = point2 + delta
        volumeLast = volumeNext
        volumeNext = BirdbathFunc425(point1, start2, start3)
    elif volumeLast > volumeNext:
        point1 = point1 - delta
        volumeLast = volumeNext
        volumeNext = BirdbathFunc425(point1, start2, start3)

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


def main():
    gradientDescentTESTER()
    print(gradientDescentTest(9,2,15)[-1])


if __name__ == '__main__':
    main()