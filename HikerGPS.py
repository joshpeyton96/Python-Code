#!/usr/bin/python
#Joshua Peyton
#Assignment 2
#GPS for hikers
__author__ = 'C14348526'
import random
import math
from math import sin, cos, sqrt, atan2, radians

#These are the functions which will execute each option
def option_1():
    #Random function is used to retrieve the Current Location
    #Longitude and Latitude are set between particular float values
    #The Long and Lat floats will be put into a tuple which is returned
    #Current Location set to Global so it can be used in other functions
    print('\nSet and retrieve the current location\n')
    #Random function is used to retrieve two float points(longitude, latitude) between float ranges
    longitude = random.uniform(-11.0, -5.0) #random floats between -11.0 - -5.0
    latitude = random.uniform(51.0, 55.0) #random floats between 51.0 - 55.0
    #assigning the float values to 1 decimal place
    "{:.2f}".format(longitude)
    "{:.2f}".format(latitude)
    #Current Location set to Global to use in other functions
    global CurrentLocation
    #Create tuple called CurrentLocation to store these points(longitude and latitude)
    CurrentLocation = (longitude, latitude)
    #return the tuple
    return CurrentLocation

def option_2():
    #The user will be asked how many waypoints they want to enter which will become the given waypoints
    #Longitude and Latitude pair will be set by the user which will be placed in a tuple then appending to a list
    #This list will be returned
    #Waypoints(The list of waypoints) is set to Global to be used in other functions
    print('\nSet and retrieve other user defined waypoints')
    #The str no_of_waypoints is used to store the number of waypoints the user wants to enter
    #User enters how many waypoints thet wish to enter
    no_of_waypoints = input('\nHow many waypoints do you want to enter?: ')
    #create a list called Waypoints to store the waypoints entered by user
    #Set it to global to use in other functions
    global Waypoints
    Waypoints = []
    #For loop which loops until x is not in range with the integer number stored in the str no_of_waypoints
    #int(no_of_waypoints) gets the integer value of the string
    #Each loop will save the numbera(points) entered by the user into a tuple(waypoint) and store it in a list which is returned
    for x in range(0,int(no_of_waypoints)):
        #longitude and latitude are equal to the two float pointd entered by the user
        #float(x) means only float numbers are allowed to be entered for the points
        #the .split() will split the numbers separately into longitude and latitude strs
        print('\n-Enter your Waypoint-')
        name = [str(x) for x in input('\nEnter the name of the waypoint: ').split()]
        longitude, latitude = [float(x) for x in input("Enter the Longitude and Latitude points: ").split()]
        #A Tuple is created to store the two points longitude and latitude
        #This Tuple containing longitude and latitude is a equal to one of the waypoints entered by the user
        Waypoint_Tuple = (name, longitude, latitude)
        #Append the Tuple(Waypoint) to the list called Waypoints to store each waypoint entered by the user
        Waypoints.append(Waypoint_Tuple)
        #The list of waypoints is returned from the function
    return Waypoints

def option_3():
    #In this option the user will be asked how many paths they want to enter which are a sequence of waypoints
    #Then the user will be asked how many waypoints they want in the path
    #Long and Lat are set by user again placed in a tuple and appended to list
    #Once the path or paths are retrieved then they will be returned
    print('\nSave and retrieve named paths consisting of a sequence of waypoints')
    #A path is a list of waypoints therefore - A list of lists
    #We need to ask the user to enter a list of waypoints and store it in a Paths list
    #We will ask the user how many paths they want to enter
    #We will then ask how many waypoints they want to enter into the path
    #The str no_of_waypoints is used to store the number of waypoints the user wants to enter
    no_of_paths = input('\nHow many paths do you want to enter?: ')
    #create a list called paths to store the lists of waypoints entered by user
    Paths = []
    #nested for loop to make a path which is a number of waypoints(list of lists)
    #This for loop used to get number of paths to be entered by user
    for x in range(0, int(no_of_paths)):
        #user asked to name the path enter
        name = input('\nEnter the name of path: ')
        #how many wayponts do you want to enter for your path
        no_waypoints = input('\nHow many waypoints are in this path: ')
        #This for loop used to get number of waypoints entered by user
        for y in range(0, int(no_waypoints)):
           print('\n-Enter Waypoint-')
           longitude, latitude = [float(y) for y in input("Enter Longitude and Latitude points: ").split()]
           waypoint_tuple = (name, longitude, latitude)
           Paths.append(waypoint_tuple)
    return Paths

def selectGivenWaypoint():
    #This function is used for option 4 and 5
    #It will allow the user to choose a waypoint from the waypoints entered in option 2
    #the longitude and latitude pairs will be returned
    #This print statement will display the waypoints entered
    print(Waypoints)
    #pick will be equal to the name the user enters for the given waypoint
    pick = input("\nPlease enter the name of one of the above given waypoints: ")
    #checks if the name entered is equal to one of the names of a given waypoint
    num = [i for i, v in enumerate(Waypoints) if v[0][0] == pick]
    #tuple is equal to iven waypoint
    tuple = Waypoints[num[0]]
    lon2 = tuple[1]
    lat2 = tuple[2]
    print(tuple[1])
    #convert to radians
    radians(float(tuple[1]))
    radians(float(tuple[2]))
    return (lon2, lat2)

def option_4(lon2, lat2):
    #In the option we find the distance from a given waypoint which is a user defined waypoint from the Current location
    #The Current Location is defined in option 1 and the given waypoints are entered by the user in option 2
    #In this option the user must be able to pick a waypoint from the waypoint list entered in option 2
    #The waypoint picked by the user is used to find distance from the Current Location
    #Code for option 4 - code to put each point in given waypoint and current location in separate vars and find distance to current location
    print("\nCalculate the distance to a given waypoint from the current location.")
    #Approximate radius of earth in km
    R = 6373.0
    #lon1 is equal to point 1 in current location
    lon1 = repr(CurrentLocation[0])
    #convert lon1 to radians
    radians(float(lon1))
    #lat1 is equal to point 2 in current location
    lat1 = repr(CurrentLocation[1])
    #convert lat1 to radians
    radians(float(lat1))

    print("\nThe Current Location is: (%.1f, %.1f)" % (CurrentLocation[0], CurrentLocation[1]))
    print('\nThe Given Waypoint is: ', lon2, lat2)

    #finding the distance
    #dlon is the distance of the lonitude and dlat is distance of the latitude
    dlon = float(lon2) - float(lon1)
    dlat = float(lat2) - float(lat1)

    #formula
    a = (sin(dlat/2))**2 + cos(float(lat1)) * cos(float(lat2)) * (sin(dlon/2))**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c
    return distance

def option_5(lon2, lat2):
    print("\nCalculate the direction as a compass bearing from the current location to a given waypoint. Range is 0 <= bearing < 360")
    #Compass bearing formula used to find direction as a compass bearing from Current location to given waypoint
    #`CurrentLocation: The tuple representing the latitude/longitude for the currentloaction point. Latitude and longitude must be in decimal degrees
    #`waypoint: The tuple representing the latitude/longitude for the given point. Latitude and longitude must be in decimal degrees
    waypoint = (lon2, lat2)
    print(CurrentLocation[0])
    print(waypoint[0])
    lat1 = math.radians(CurrentLocation[0])
    lat2 = math.radians(waypoint[0])

    diffLong = math.radians(waypoint[1] - CurrentLocation[1])

    #Formula
    y = math.sin(diffLong) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
            * math.cos(lat2) * math.cos(diffLong))
    initial_bearing = math.atan2(y, x)
    #degrees
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360
    return compass_bearing

#A list called menu is created which store the numbers 1-6
#This is used for the main menu
#If-else statements will be placed in a while loop which only terminates when option 6 is enetered
menu = {}
menu['1'] = "Set and retrieve the current location."
menu['2'] = "Set and retrieve other user-defined waypoints."
menu['3'] = "Save and retrieve named paths consisting of a sequence of waypoints."
menu['4'] = "Calculate the distance to a given waypoint from the current location."
menu['5'] = "Calculate the direction as a compass bearing from the current location to a given waypoint. Range is 0 <= bearing < 360"
menu['6'] = "Exit"
while True:
    #using a dictionary to store menu option as the key, and the text to display that option as the value
    options = menu.keys() #key in menu is equal to options
    for entry in sorted(options): #sorted(options) = sorts the options when displayed on screen
       print(entry, menu[entry])
    #if-else statements to call each function when user enters that particular option
    print('----------------------------------------------------------------------------------------------------------------------------')
    selection = input("Please enter an option between 1-6: ") #selection is equal to users input
    #if the user enters 1 as the option then implement option 1
    if selection == '1':
       #tuple returned is equal to two_pointTuple
       CurrentLocation = option_1()
       #Display the points for Current Location to one decimal point
       print("The Current Location is: (%.1f, %.1f)" % (CurrentLocation[0], CurrentLocation[1]))
       #Option separator
       print('----------------------------------------------------------------------------------------------------------------------------')
    #if the user enters 2 as the option then implement option 2
    elif selection == '2':
       waypoints = option_2()
       print('The waypoints: ', waypoints)
       #Option separator
       print('----------------------------------------------------------------------------------------------------------------------------')
    #if the user enters 3 as the option then implement option 3
    elif selection == '3':
       paths = option_3()
       #Option separator
       print('----------------------------------------------------------------------------------------------------------------------------')
    #if the user enters 4 as the option then implement option 4
    elif selection == '4':
       #selectGivenWaypoint function called in order for option 4 function to execute
       #lon2, lat2 returned and passed to option4 function
       lon2, lat2 = selectGivenWaypoint()
       distance = option_4(lon2, lat2)
       print('\nThe distance from the given waypoint to current loaction: %.1f km' % (distance))
       #Option separator
       print('----------------------------------------------------------------------------------------------------------------------------')
    #if the user enters 5 as the option then implement option 5
    elif selection == '5':
       #selectGivenWaypoint function called in order for option 5 function to execute
       #lon2, lat2 returned and passed to option4 function
       lon2, lat2 = selectGivenWaypoint()
       compass_bearing = option_5(lon2, lat2)
       print('\nThe direction as a compass bearing from the current location to a given waypoint: %.1f degrees' % (compass_bearing))
       #Option separator
       print('----------------------------------------------------------------------------------------------------------------------------')
    #if the user enters 6 as the option then implement option 6
    elif selection == '6':
       print('Program has been exited')
       break
    else:
       #This option used for error-checking
       print("Invalid option entered")
       #Option separator
       print('----------------------------------------------------------------------------------------------------------------------------')
