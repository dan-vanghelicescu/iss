import math
from math import *
from time import sleep
from datetime import datetime
#from orbit import ISS # For the actual location data

class earth:
    equatorialRadius = 6378.1370
    polarRadius = 6357.7523
    gravitationalConstant = 6.673e-20
    mass = 5.972e24

class dummyISS:
    class coordinates:
        class latitude:
            def getDegree():
                while True:
                    yield math.pi / 4 + math.pi / 128
            degrees = next(getDegree())
        class elevation:
            km = 403

earthRadius = lambda latitude: sqrt(
    (((earth.equatorialRadius ** 2) * cos(latitude)) ** 2 + ((earth.polarRadius ** 2) * sin(latitude)) ** 2)
    / ((earth.equatorialRadius * cos(latitude)) ** 2 + (earth.polarRadius * sin(latitude)) **2 ))

keplersThird = lambda distance: sqrt((earth.gravitationalConstant * earth.mass) / distance)

speedFromLocation = lambda location: keplersThird(earthRadius(location.latitude.degrees) + location.elevation.km)

printOutput = lambda txt: print("{:.4f}".format(txt), file = open("result.txt", "w"))

def mainProgram(): # Main program, runs for max than 10 minutes, computes the arithmetic mean of the speeds
    
    mean = 0.0
    tenMinutes = 10 * 60
    startTime = datetime.now()
    
    for i in range(1, 39):        
        location = dummyISS.coordinates
        mean += speedFromLocation(location)        
        if((datetime.now() - startTime).seconds > tenMinutes): 
            break 
        sleep(.15)
    
    mean /= i 
    printOutput(mean)
    
mainProgram()
