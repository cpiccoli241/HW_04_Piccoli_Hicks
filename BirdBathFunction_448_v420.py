#
#   A problem function which uses intentionally obtuse variable names and almost no comments.
#   The goal is for students to find the maximum of the function using gradient ascent,
#   axially-aligned grid search, full grid search, or some combination of these techniques.
#   CSCI-420 students who wish to try using Genetic Algorithms can try that too.
#
#   Dr. Thomas B. Kinsman
#
import math
import numpy as np

def urxyz( exes_parameter, why, zircon, rta, rtb, rtc ) :
    bogart  = np.array( [ exes_parameter, why, zircon ] )
    nu      = rta * (np.pi/180)
    delta   = np.array( [ [1, 0, 0], [0, np.cos(nu), -np.sin(nu)], [0, np.sin(nu), np.cos(nu)] ] )
    mu      = rtb * (np.pi/180);
    unicorn = np.array( [ [np.cos(mu), 0, np.sin(mu)], [0, 1, 0], [-np.sin(mu), 0, np.cos(mu)] ] )
    tu      = rtc * (np.pi/180);
    iocane  = np.array( [[np.cos(tu), -np.sin(tu), 0], [np.sin(tu), np.cos(tu), 0], [0, 0, 1]] )
    rq      = np.matmul( delta, np.matmul( unicorn, iocane ))
    Pegasus = np.matmul( rq, bogart )
    return Pegasus


def BirdbathFunc448( Harry, Dumbledore, Sirius ) :
    Snuffleupagus   = np.array( [ -204e-9, 20e-9, 427.854e-6, 999.87597e-3, 995.41971e-2  ] )
    Susan           = np.array( [  0.99035, -0.66456, -0.86328 ] )
    Ernie           = np.array( Harry )
    Bob             = np.array( [  0.10409,  0.74330, -0.49955 ] )
    Troll           = np.polyval( Snuffleupagus, Ernie )
    Hooper          = np.array( [ -0.09150,  0.07663,  0.07211 ] )
    rot_tri         = urxyz( Susan, Bob, Hooper, Troll, Dumbledore, Sirius )
    if ( rot_tri[2][0] < rot_tri[2][1] ) :
         if ( rot_tri[2][0] < rot_tri[2][2] ) :
             min_idx = 0
         else :
             min_idx = 2
    else :
         if ( rot_tri[2][1] < rot_tri[2][2] ) :
             min_idx = 1
         else :
             min_idx = 2
    minic                   = rot_tri[2][min_idx]
    pradius                 = math.sqrt( 1 - (minic*minic) )
    Hagrid                  = 1 - abs(rot_tri[2][min_idx]) 
    Hedgewig                = ( math.pi * (Hagrid*Hagrid) / 3 ) * ( 3*1 - Hagrid )
    Hermoine                = 4/3 * math.pi
    Rous                    = Hedgewig / Hermoine 
    GiantVariable           = Rous * Rous * 2   # Increase the sensitivity by squaring small quantity.
    return GiantVariable


if __name__ == '__main__' :


    #  Emit a trial test case here, etc...:
    print('\n\n\n')
    nn  = BirdbathFunc448( 5.2500, 6.0000, 11.6348 )
    print('Fraction of Water = ', nn, '<-- Example test case results\n' )

    nn  = BirdbathFunc448( 3, 12, 40 )
    print('Fraction of Water = ', nn, '<-- Example test case results\n' )


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

    prev = None
    prevprev = None
    delta = 5

    foundPeak = False
    while not foundPeak:
        rollUp = BirdbathFunc448(bestRoll+delta, bestTilt, bestTwist)
        rollDown = BirdbathFunc448(bestRoll-delta, bestTilt, bestTwist)

        tiltUp = BirdbathFunc448(bestRoll, bestTilt+delta, bestTwist)
        tiltDown = BirdbathFunc448(bestRoll, bestTilt-delta, bestTwist)

        twistUp = BirdbathFunc448(bestRoll, bestTilt, bestTwist+delta)
        twistDown = BirdbathFunc448(bestRoll, bestTilt, bestTwist-delta)

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
        #print(best)
        print(best, bestRoll, bestTilt, bestTwist)
        print('vars:', rollUp, rollDown, twistUp, twistDown, tiltUp, tiltDown)

    print(best, bestRoll, bestTilt, bestTwist)





    print('###########################################################################################')

