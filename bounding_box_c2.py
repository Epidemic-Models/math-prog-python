from rectangle import Rectangle


class BoundingBoxC(Rectangle):
    def __init__(self, width: float, height: float, left_lower: tuple):
        super().__init__(width, height)
        self.left_lower = left_lower

    def __str__(self):
        return "BoundingBox: left_lower=" + str(self.left_lower) + \
               ", width=" + str(self.width) + ", height=" + str(self.height)


def main():
    bounding_box = BoundingBoxC(width=4, height=7, left_lower=(2.0, 3.7))
    print(bounding_box)


if __name__ == "__main__":
    main()