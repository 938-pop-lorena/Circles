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
    x = randint(0, 20)
    y = randint(0, 20)
    maxRadius = min(x, y)
    r = randint(1, maxRadius)
    circle = create_circle(x, y, r)


def findCircle(circles: list, circle: dict):
    """
    Returns the position of the circle in the list.

    """