from rectangle import Rectangle


class BoundingBoxC(Rectangle):
    def __init__(self, width: float, height: float, right_upper: tuple):
        super().__init__(width=width, height=height)
        self.right_upper = right_upper

    def __str__(self):
        return "BoundingBox: right_upper=" + str(self.right_upper) + \
               ", width=" + str(self.width) + ", height=" + str(self.height)

    def left_upper(self):
        return self.right_upper[0]-self.width, self.right_upper[1]

    def convert(self):
        return "BoundingBox: left_upper=" + str(self.left_upper()) + \
               ", width=" + str(self.width) + ", height=" + str(self.height)


def main():
    bounding_box = BoundingBoxC(width=4, height=3, right_upper=(6, 9))
    print(bounding_box)
    print(bounding_box.convert())


if __name__ == "__main__":
    main()
