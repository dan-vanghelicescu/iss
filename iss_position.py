import math
from math import *
from time import sleep
from datetime import datetime
#from orbit import ISS # For the actual location data
step = 0
class dummyISS:
    class coordinates:
        class latitude:
            def degrees():
                global step
                return (math.pi / 4) + (step:=step+1) * (math.pi / 2**16)
        class elevation:
            km = 403

class earth:
    equatorialRadius = 6378.1370
    polarRadius = 6357.7523
    gravitationalConstant = 6.673e-20
    mass = 5.972e24

earthRadius = lambda latitude: sqrt(
    (((earth.equatorialRadius ** 2) * cos(latitude)) ** 2 + ((earth.polarRadius ** 2) * sin(latitude)) ** 2)
    / ((earth.equatorialRadius * cos(latitude)) ** 2 + (earth.polarRadius * sin(latitude)) **2 ))

keplersThird = lambda distance: sqrt((earth.gravitationalConstant * earth.mass) / distance)

speedFromLocation = lambda location: keplersThird(earthRadius(location.latitude.degrees()) + location.elevation.km)

def mainProgram(): # Main program, runs for max than 10 minutes, computes the arithmetic mean of the speeds
    
    mean, tenMinutes, startTime = 0.0, 10 * 60, datetime.now()
    for i in range(1,39):
        if ((datetime.now() - startTime).seconds > tenMinutes):
            break;
        mean += speedFromLocation(dummyISS.coordinates)
        sleep(.15)
    
    mean /= i 
    print("{:.4f}".format(mean), file = open("result.txt", "w"))
    print(i)
    
mainProgram()
