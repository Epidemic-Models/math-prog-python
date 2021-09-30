from __future__ import annotations

from point import Point
from rectangle import Rectangle


class BoundingBox(Rectangle):
    def __init__(self, width: float, height: float, left_upper: Point) -> None:
        super().__init__(width=width, height=height)
        self.left_upper = left_upper
        self.__right_lower = None

    def __str__(self) -> str:
        return "BoundingBox: left_upper=" + str(self.left_upper) + \
               ", width=" + str(self.width) + ", height=" + str(self.height)

    @property
    def right_lower(self) -> Point:
        shift = Point(p=(self.height, self.width))
        self.__right_lower = self.left_upper + shift
        return self.__right_lower

    def get_intersection(self, other: BoundingBox) -> BoundingBox:
        intersection_left_upper = Point(p=(max(self.left_upper.x, other.left_upper.x),
                                        max(self.left_upper.y, other.left_upper.y))
                                        )
        intersection_right_lower = Point(p=(min(self.right_lower.x, other.right_lower.x),
                                            min(self.right_lower.y, other.right_lower.y))
                                         )
        intersection_width = intersection_right_lower.y - intersection_left_upper.y
        intersection_height = intersection_right_lower.x - intersection_left_upper.x

        intersection = None
        if intersection_height > 0 and intersection_width > 0:
            intersection = BoundingBox(left_upper=intersection_left_upper,
                                       width=intersection_width,
                                       height=intersection_height)

        return intersection


def main() -> None:
    bounding_box = BoundingBox(width=2.0, height=3.0, left_upper=Point(p=(2.3, 4.3)))
    print(bounding_box)
    print("The right lower corner: ", bounding_box.right_lower)
    bounding_box_2 = BoundingBox(width=1, height=1, left_upper=Point(p=(3.3, 5.3)))
    print(bounding_box.get_intersection(other=bounding_box_2))


if __name__ == "__main__":
    main()
