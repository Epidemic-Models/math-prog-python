from rectangle import Rectangle


class BoundingBox(Rectangle):
    def __init__(self, width: float, height: float, left_upper: tuple):
        super().__init__(width=width, height=height)
        self.left_upper = left_upper

    def __str__(self):
        return "BoundingBox: left_upper=" + str(self.left_upper) + \
               ", width=" + str(self.width) + ", height=" + str(self.height)


def main():
    bounding_box = BoundingBox(width=2.0, height=3.0, left_upper=(2.3, 4))
    print(bounding_box)


if __name__ == "__main__":
    main()
