from __future__ import annotations
from rectangle import Rectangle


class BoundingBoxC(Rectangle):
    def __init__(self, width: float, height: float, left_upper: tuple):
        super().__init__(width=width, height=height)
        self.left_upper = left_upper
        right_lower = self.left_upper[0] + self.width, self.left_upper[1] - self.height
        self.right_lower = right_lower

    def __str__(self):
        return "BoundingBox: left_upper=" + str(self.left_upper) + \
               ", width=" + str(self.width) + ", height=" + str(self.height)

    def get_union(self, other: BoundingBoxC):
        union_left_upper = min(self.left_upper[0], other.left_upper[0]), max(self.left_upper[1], other.left_upper[1])
        union_right_lower = (max(self.right_lower[0], other.right_lower[0]), min(self.right_lower[1],
                                                                                 other.right_lower[1]))
        union_width = union_right_lower[0] - union_left_upper[0]
        union_height = union_left_upper[1] - union_right_lower[1]
        return "left_upper=" + str(union_left_upper) + \
               ", width=" + str(union_width) + ", height=" + str(union_height)


def main():
    bounding_box_c = BoundingBoxC(width=4, height=5, left_upper=(2.0, 10))
    bounding_box_c1 = BoundingBoxC(width=3, height=5, left_upper=(5.0, 8))
    print(bounding_box_c)
    print("The union of the two bounding boxes: ", bounding_box_c.get_union(bounding_box_c1))


if __name__ == "__main__":
    main()
