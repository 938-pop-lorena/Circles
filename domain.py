def create_circle(x: int, y: int, r: int):
    circle = {'center': (x, y),
              'radius': r}
    return circle


def get_center(circle: dict):
    return circle['center']


def get_radius(circle: dict):
    return circle['radius']


def to_str(circle: dict):
    return "Circle with center {} and radius {}".format(circle['center'],
                                                        circle['radius'])
