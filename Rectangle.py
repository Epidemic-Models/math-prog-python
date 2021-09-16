class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def main():
    rect = Rectangle(width=3, height=5)
    print("Height of the rectangle: ", rect.height)
    print("Area of the rectangle: ", rect.area())

if __name__ ==  "__main__":
    main()



