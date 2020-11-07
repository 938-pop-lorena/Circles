from random import randint

from src.domain import *


def generateCircles(circles: list, number: int):
    """
    Generate a given number of distinct circles. each circle completely enclosed in a square defined by corners (0,0)
    and (20, 20).
    Distinct = at least one of x,y radius must differ
    :param circles: List of circles
    :param number: Integer determining how many circles will be generated
    """
    while number != 0:
        x = randint(0, 20)
        y = randint(0, 20)
        maxRadius = min(x, y)
        if maxRadius > 1:
            r = randint(1, maxRadius)
        else:
            r = 1
        circle = create_circle(x, y, r)
        pos = findCircle(circles, circle)
        if pos == -1:
            circles.append(circle)
            number -= 1


def findCircle(circles: list, circle: dict):
    for i in range(0, len(circles)):
        if circles[i]['center'] == circle['center'] and circles[i]['radius'] == circle['radius']:
            return i
    return -1


def displayCircles(circles: list):
    for circle in circles:
        print(to_str(circle))
