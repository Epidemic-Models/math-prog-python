import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def circumference(self):
        return 2 * (self.height + self.width)

    def calculate_diagonal(self):
        return math.sqrt(self.height ** 2 + self.width ** 2)


def main():
    rect = Rectangle(width=3, height=5)
    print("Height of the rectangle: ", rect.height)
    print("Area of the rectangle: ", rect.area())
    print("Circumference of the rectangle is: ", rect.circumference())
    print("The length of the diagonal is: ", rect.calculate_diagonal())

if __name__ ==  "__main__":
    main()



