from src.rectangle import Rectangle


class BoundingBoxC(Rectangle):
    def __init__(self, width: float, height: float, right_lower: tuple):
        super().__init__(width=width, height=height)
        self.right_lower = right_lower

    def __str__(self):
        return "BoundingBox: right_lower=" + str(self.right_lower) + \
               ", width=" + str(self.width) + ", height=" + str(self.height)


def main():
    bounding_box = BoundingBoxC(width=4, height=7, right_lower=(2.0, 3.7))
    print(bounding_box)


if __name__ == "__main__":
    main()
