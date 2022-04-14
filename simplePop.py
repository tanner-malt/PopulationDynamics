import math
import numpy

def allKnownCase():
    #Runs simplest Dynamics
    # Assume Migration = 0.
    # Assume everything is none, use as calculator
    n_0 = float(input("Enter initial population value: "))
    # k = input("Enter carrying capacity value: ")
    r = float(input("Enter birthrate value: "))
    t = float(input("Enter time step value: "))
    population = round(n_0 * math.exp(r*t))

    return population


def findrval():
    n0 = float(input("Enter initial population value: "))
    n1 = float(input("Enter timestamp of a known pop value: "))
    t1 = float(input("Enter population value of known timestamp: "))

    r = round(numpy.log(n1/n0)/t1,3)
    return r
