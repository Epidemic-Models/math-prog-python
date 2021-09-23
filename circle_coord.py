import math


class Circlecoord:

    def __init__(self, radius, c_x, c_y):
        self.radius = radius
        self.c_x = c_x
        self.c_y = c_y

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def get_diameter(self):
        return 2 * self.radius

    def contains(self, p_x=4, p_y=6):
        distance = math.sqrt((self.c_x - p_x) ** 2 + (self.c_y - p_y) ** 2)
        return distance <= self.radius

    def overlaps(self, other):
        distance_center = math.sqrt((self.c_x - other.c_x) ** 2 + (self.c_y - other.c_y) ** 2)
        sum_radii = self.radius + other.radius
        return distance_center < sum_radii


def main():
    circle_1 = Circlecoord(radius=5, c_x=2, c_y=3)
    circle_2 = Circlecoord(radius=10, c_x=5, c_y=10)
    print("The circumference of the circle is: ", circle_1.circumference())
    print("The area of the circle is: ", circle_1.area())
    print("The diameter of the circle is: ", circle_1.get_diameter())
    print("Is the point with coordinates (4, 5) inside the circle?: ", circle_1.contains())
    print("Does the circle overlap with the other circle?: ", circle_1.overlaps(circle_2))


if __name__ == "__main__":
    main()
