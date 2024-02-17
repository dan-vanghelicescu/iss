from math import * # For using sin and cos
from decimal import Decimal # For precise calculations :3
from time import sleep # For getting data every X seconds
from datetime import datetime # For monitoring program runtime
from orbit import ISS # For the actual location data

a = Decimal(6378.1370) # Earth's equatorial radius (for the formula below)
b = Decimal(6357.7523) # Earth's polar radius (for the formula below)
def earthRadius(latitude): # We are calculating Earth's radius at a given latitude
    
    phi = Decimal(latitude)
    cosine = Decimal(cos(phi))
    sine = Decimal(sin(phi))
    
    num = (((a * a) * cosine)**2 + ((b * b) * sine)**2)
    den=(Decimal(a * cosine)**2 + Decimal(b * sine)**2)
    radius=Decimal(sqrt((num) / (den)))
    
    return radius

g = Decimal(6.673e-20) # This is the gravitational constant (for the formula below)
m = Decimal(5.972e24) # This is Earth's mass (for the formula below)
def calcSpeed(radius, distance): # We are using the equation for orbital speed that is based on Kepler's Third Law
    
    r = radius + distance # This is the distance between the center of masses of the earth and the space station
    speed = Decimal(sqrt((g * m) / r))
    return speed

def calcFromLocation(): # This function gets the Space Station's location and does the calculations for the necessary speed
    
    location = ISS().coordinates()
    
    latitude = Decimal(location.latitude.degrees)
    height = Decimal(location.elevation.km)
    
    return (calcSpeed(earthRadius(latitude), height))
 
def printOutput(speed): # Prints in the result.txt file, creates it if it does not exist
    
    f = open("result.txt", "w", encoding="ascii")
    
    formatted = "{:.4f}".format(speed) # We format our result to have 4 decimals
    f.write(str(formatted))
    
    f.close()

def mainProgram(): # Main program, monitores the time such that it does not run for more than 10 minutes, does the arithmetic mean of the speeds
    
    mean = Decimal(0)
    cnt = 0 # This is the number of data sets processed so far
    iterations = 38 # This is the maximum number of iterations
    
    mins = 9
    secs = 30
    time = mins * 60 + secs # This is the maximum time we allow the program to run for
    
    startTime = datetime.now()
    
    for i in range(1, iterations+1):
        
        currentTime = datetime.now()
        if((currentTime-startTime).seconds >= time): 
            break # Stops the loop after running for 9 minutes and 30 seconds
        
        mean += calcFromLocation()
        cnt += 1
        
        sleep(15) # Assures there is a fair distance between now and the next data set
    
    mean /= cnt
    printOutput(mean)
    
mainProgram()
