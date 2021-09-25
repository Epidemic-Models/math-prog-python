from __future__ import annotations
from rectangle import Rectangle


class BoundingBoxC(Rectangle):
    def __init__(self, width: float, height: float, left_upper: tuple):
        super().__init__(width, height)
        self.left_upper = left_upper

    def __str__(self):
        return "BoundingBox: left_upper=" + str(self.left_upper) + \
               ", width=" + str(self.width) + ", height=" + str(self.height)

    def get_union(self, other: BoundingBoxC):
        union_left_upper = max(self.left_upper, other.left_upper)
        union_width = self.width + other.width
        union_height = self.height + other.height
        return "UnionOfBoundingBoxCandBoundingBoxC1: left_upper=" + str(union_left_upper) + \
               ", width=" + str(union_width) + ", height=" + str(union_height)


def main():
    bounding_box_c = BoundingBoxC(width=4, height=7, left_upper=(2.0, 3.7))
    bounding_box_c1 = BoundingBoxC(width=3, height=5, left_upper=(5.0, 32.7))
    print(bounding_box_c)
    print(bounding_box_c.get_union(bounding_box_c1))


if __name__ == "__main__":
    main()
