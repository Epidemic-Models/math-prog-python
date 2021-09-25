from rectangle import Rectangle
from bounding_box import BoundingBox


class BoundingBoxA(Rectangle):
    def __init__(self, left_upper: tuple, right_lower: tuple):
        self.left_upper = left_upper
        self.right_lower = right_lower
        width = self.right_lower[0] - self.left_upper[0]
        height = self.left_upper[1] - self.right_lower[1]
        super().__init__(width=width, height=height)

    def __str__(self):
        return "BoundingBoxA: left_upper=" + str(self.left_upper) +\
               ", right_lower=" + str(self.right_lower)

    def convert(self):
        return BoundingBox(self.width, self.height, self.left_upper)


def main():
    bounding_box_a = BoundingBoxA(left_upper=(2, 3), right_lower=(5, 1))
    print(bounding_box_a)
    print(bounding_box_a.convert())


if __name__ == "__main__":
    main()
