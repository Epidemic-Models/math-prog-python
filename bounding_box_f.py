from rectangle import Rectangle


class BoundingBoxF(Rectangle):
    def __init__(self, width: float, height: float, centre: tuple):
        super().__init__(width=width, height=height)
        self.centre = centre

    def __str__(self):
        return "BoundingBoxF: centre=" + str(self.centre) + \
               ", width=" + str(self.width) + ", height=" + str(self.height)


def main():
    bounding_box_f = BoundingBoxF(centre=(3, 5), width=3, height=3)
    print(bounding_box_f)


if __name__ == "__main__":
    main()
