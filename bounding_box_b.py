from rectangle import Rectangle


class BoundingBoxB(Rectangle):
    def __init__(self, left_lower: tuple, right_upper: tuple, width: float, height: float):
        super().__init__(width, height)
        self.left_lower = left_lower
        self.right_upper = right_upper

    def __str__(self):
        return "BoundingBoxB: left_lower=" + str(self.left_lower) +\
               ", right_upper=" + str(self.right_upper)


def main():
    bounding_box_b = BoundingBoxB(left_lower=(2.3, 2.3), right_upper=(5.6, 6.2), width=True, height=True)
    print(bounding_box_b)


if __name__ == "__main__":
    main()
