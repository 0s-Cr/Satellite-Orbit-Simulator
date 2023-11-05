import math


def floatInputConverter():  # This function takes a user input and converts it into a float
    while True:  # This creates an infinite while loop
        x = input("")  # Variable is names x due to the fact it is a generic unknown variable with several different
        try:  # This tells the program to try to convert the variable x into a float
            x = float(x)
        except ValueError:  # This allows the program to continue running if an error occurs in this situation
            print("Invalid input, please try again:", end="")
            continue
        if x <= 0:
            print("Number must be greater than 0, please try again:", end="")
            continue
        break
    return x  # This returns x to the variable which called this function


def periapsis(rApo):  # Periapsis requires more validation than just checking if it is a float
    while True:  # This creates an infinite while loop
        x = input("")
        try:  # This tells the program to try to convert the variable x into a float
            x = float(x)
        except ValueError:  # This allows the program to continue running if an error occurs in this situation
            print("Invalid input, please try again:", end="")
            continue
        if x > rApo:  # This statement compares the input value with the previous apogee value, and will only allow the
            # program to continue running if perigee <= apogee
            print("Perigee must be less than or equal to apogee.  Please try again:", end="")
            continue
        elif x <= 0:
            print("Number must be greater than 0, please try again:", end="")
            continue
        break
    x = float(x)
    if x == rApo:  # This statement check to see if the perigee is equal to the apogee, making the orbit a
        # perfect circle
        global circle  # This variable will be used later on to skip certain calculations because in a perfectly
        circle = True  # circular obit, some parameters are constant
    return x


def constantCalculations(uniGrav, parentMass, parentRadius, rApo, rPer):
    constants = [0, 0, 0, 0, 0, 0, 0, 0]  # in order of 0=g, 1=standardGrav, 2=rMax, 3=rMin, 4=smB, 5=smA,
    # 6=eccentricity and 7=period
    constants[0] = (uniGrav * parentMass) / parentRadius ** 2  # acceleration
    constants[1] = uniGrav * parentMass  # standard gravitational parameter
    constants[2] = rApo + parentRadius  # Maximum and minimum orbital radii
    constants[3] = rPer + parentRadius
    constants[4] = math.sqrt(constants[2] * constants[3])  # Semi-minor axis
    constants[5] = (constants[2] + constants[3]) / 2  # Semi-major axis
    constants[6] = math.sqrt(1 - (constants[4] ** 2 / constants[5] ** 2))  # Eccentricity
    constants[7] = 2 * math.pi * math.sqrt(constants[5] ** 3 / constants[1])  # Period
    return constants


def radius(xx, yy, k, scale):  # a function to calculate radius at any given point in the orbit
    r = math.sqrt(xx[k] ** 2 + yy[k] ** 2) / scale
    return r


def speed(xx, yy, k, scale, standardGrav, smA):  # a function to calculate the instantaneous speed of an object as
    # it orbits
    r = math.sqrt(xx[k] ** 2 + yy[k] ** 2) / scale
    v = math.sqrt(standardGrav * ((2 / r) - (1 / smA)))
    if v > 1:
        v = round(v, 2)
    return v
