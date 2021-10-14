from __future__ import annotations

from src.bounding_box import BoundingBox
from src.point import Point
from src.rectangle import Rectangle


class BoundingBoxB(Rectangle):
    def __init__(self, left_lower: Point, right_upper: Point) -> None:
        self.left_lower = left_lower
        self.right_upper = right_upper
        width = self.right_upper.x - self.left_lower.x
        height = self.right_upper.y - self.left_lower.x
        super().__init__(width=width, height=height)
        self.__left_upper = None
        self.__right_lower = None
        self.__centre = None

    def __str__(self) -> str:
        return "BoundingBoxB: left_lower=" + str(self.left_lower) +\
               ", right_upper=" + str(self.right_upper)

    def convert(self) -> BoundingBox:
        return BoundingBox(width=self.width, height=self.height, left_upper=self.left_lower)

    @property
    def left_upper(self) -> Point:
        self.__left_upper = Point(p=(self.left_lower.x, self.right_upper.y))
        return self.__left_upper

    @property
    def right_lower(self) -> Point:
        self.__right_lower = Point(p=(self.right_upper.x, self.left_lower.y))
        return self.__right_lower

    @property
    def centre(self) -> Point:
        shift = Point(p=(self.width / 2, self.height / 2))
        self.__centre = self.left_lower + shift
        return self.__centre

    def get_union(self, other: BoundingBoxB) -> BoundingBoxB:
        union_left_lower = Point(p=(min(self.left_lower.x, other.left_lower.x),
                                    min(self.left_lower.y, other.left_lower.y))
                                 )
        union_right_upper = Point(p=(max(self.right_upper.x, other.right_upper.x),
                                     max(self.right_upper.y, other.right_upper.y))
                                  )
        union = BoundingBoxB(left_lower=union_left_lower, right_upper=union_right_upper)
        return union

    def get_intersection(self, other: BoundingBoxB) -> BoundingBoxB:
        intersection_left_lower = Point(p=(max(self.left_lower.x, other.left_lower.x),
                                           max(self.left_lower.y, other.left_lower.y))
                                        )
        intersection_right_upper = Point(p=(min(self.right_upper.x, other.right_upper.x),
                                            min(self.right_upper.y, other.right_upper.y))
                                         )
        intersection_width = intersection_right_upper.x-intersection_left_lower.x
        intersection_height = intersection_right_upper.y-intersection_left_lower.y

        intersection = None
        if intersection_height > 0 and intersection_width > 0:
            intersection = BoundingBoxB(left_lower=intersection_left_lower,
                                        right_upper=intersection_right_upper)

        return intersection


def main() -> None:
    bounding_box_1 = BoundingBoxB(left_lower=Point(p=(2.1, 2)), right_upper=Point(p=(3, 3)))
    print(bounding_box_1)
    bounding_box_2 = BoundingBoxB(left_lower=Point(p=(2, 2)), right_upper=Point(p=(4, 4)))
    print("A different representation of the bounding box: ", bounding_box_1.convert())
    print("The union of the two bounding boxes: ", bounding_box_1.get_union(bounding_box_2))
    print("The intersection of the two bounding boxes: ", bounding_box_1.get_intersection(bounding_box_2))


if __name__ == "__main__":
    main()
