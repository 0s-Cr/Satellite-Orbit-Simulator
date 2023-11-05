# Importing useful libraries for program and defining constants
from Prototype4Animation import *
from Prototype4Library import *

uniGrav = float(6.67408e-11)


def main():  # This process is used for taking the initial values the program utilises
    print("Please enter the mass of the central body:", end="")  # Each variable is taken by calling the function
    # floatInputConverter
    parentMass = floatInputConverter()  # This function takes the variable and automatically converts it to a float
    print("Please enter the radius of the central body:", end="")
    parentRadius = floatInputConverter()
    print("Please enter the satellite apogee:", end="")
    rApo = floatInputConverter()
    print("Please enter the satellite perigee:", end="")
    rPer = periapsis(rApo)
    print("Please enter the mass of the satellite:", end="")
    satMass = floatInputConverter()
    phase2(uniGrav, parentMass, parentRadius, rApo, rPer, satMass)



def phase2(uniGrav, parentMass, parentRadius, rApo, rPer, satMass):  # This function is used for calculating the
    # coordinates of the parent body and orbit trace of the satellite on the graph along with some other constants
    constants = constantCalculations(uniGrav, parentMass, parentRadius, rApo, rPer, )
    if constants[6] >= 1:  # This statement ensures that the orbit is elliptic, and therefore all calculations used
        # by this program apply to it.
        print("Trajectory is parabolic or hyperbolic, and therefore cannot be shown with this program.\nRestarting.")
        main()
    else:
        parentCoords = [[-2, -2], [2, 2]]  # The parent body will always have a scale radius of 2 units, making scaling
        # calculations easier
        coordScale = 2 / parentRadius
        satCoords = [coordScale * -constants[4],  # In order of periapsis then apoapsis, x y
                     coordScale * -(parentRadius + rPer),
                     coordScale * constants[4],
                     coordScale * (parentRadius + rApo)]
        fig = graph(parentCoords, satCoords, coordScale, parentRadius, constants, satMass)
        fig.show()
    refresh()


def refresh():  # This function simply asks the user if they wish to restart the program or not
    choice = input("To restart the program, please enter 'r'.  Enter any other input to quit.")
    if choice == "r":
        main()
    else:  # If any input other than "r" is entered, the program stops
        quit()


main()
