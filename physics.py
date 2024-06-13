'''
File name: physics.py

-------------------Description-------------------

In this file, I have written codes for required physics for a basic golf play. In this file I have written code on hitting the ball, throwing
from vaarious angles, shot angles and other required stuffs that must needed for a golf player. 

'''


import math  # import the main package

# deploy the physics mechanism of a golf ball


def ballPath(startx, starty, power, ang, time):
    angle = ang
    velx = math.cos(angle) * power  # for x-axis or surface cos is the main key
    # for y-axis or  in sky or air or vacumme sin is the main key
    vely = math.sin(angle) * power

    distX = velx * time  # total time for x-axis and the equation is s = vt
    # time for y-axis and the equation is s = ut + (1/2) * (-9.8) * t^2, since ball is working against the gravity, I took -9.8 as a default gravity value
    distY = (vely * time) + ((-9.8 * (time ** 2)) / 2)

    newx = round(distX + startx)  # final position x-axis
    newy = round(starty - distY)  # final position y-axis

    return (newx, newy)

# physics of hitting ball with a certain amount of power


def findPower(power, angle, time):
    # x-axis, v= u cos(theta), u refered as power
    velx = math.cos(angle) * power
    # y-axis, v= u sin(theta), u refered as power
    vely = math.sin(angle) * power

    vfy = vely + (-9.8 * time)  # generate initial power v = u + (-9.8) * t
    # 2 dimentional physics law for final power of hitting ball root of x^2 + y^2
    vf = math.sqrt((vfy**2) + (velx**2))

    return vf

# angular physics for complicated shot


def findAngle(power, angle):
    vely = math.sin(angle) * power
    velx = math.cos(angle) * power

    # y-axis angle / x-axis angle =  tan(theta)
    ang = math.atan(abs(vely) / abs(velx))

    return ang

# time limit for a ball to float in the air based on hiting power


def maxTime(power, angle):
    vely = math.sin(angle) * power
    time = ((power * -1) - (math.sqrt(power**2))) / -9.8

    return time / 2
