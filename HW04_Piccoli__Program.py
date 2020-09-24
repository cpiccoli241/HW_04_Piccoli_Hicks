"""
 :author: Chris Piccoli
 :date: 9/17/2020
"""
import pandas as pd
from sys import maxsize
import numpy as np
from matplotlib import pyplot as plt
from math import floor, ceil, cos, sin, sqrt, pi
import scipy
from datetime import date


def hemisphere_surface(x, y, z):
    return x**2+y**2+z**2-1


def hemisphere_surface_polar_rotations(rho, phi, rotation1, rotation2, rotation3):
    return rho**2*cos(phi)


def hemisphere_volume(radius, height):
    baseRadiusSquare = radius**2-(radius-height)**2
    return pi/6*height*(3*baseRadiusSquare+height**2)


def circle_in_XYZ(x,y,z, radius):
    return x**2+y**2-radius**2


def rotate_normal(vector, axis, theta):
    """
        Return the rotation matrix associated with counterclockwise rotation about
        the given axis by theta radians.
        """
    axis = np.asarray(axis)
    axis = axis / sqrt(np.dot(axis, axis))
    a = cos(theta / 2.0)
    b, c, d = -axis * sin(theta / 2.0)
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    rotation_vector = np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                     [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                     [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])
    return np.dot(rotation_vector, np.asarray(vector))


def generate_circle(normalVector, radius):
    x*normalVector[0] + y*normalVector[1] + z*normalVector[2] = 0
    x**2+y**2 + z**2 = radius**2



def main():
    normal = rotate_normal([1,1,1], [1,1,0], pi/2)
    print(normal)
    input("Press any key to close...")


if __name__ == '__main__':
    main()