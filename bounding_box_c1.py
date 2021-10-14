from __future__ import annotations

from src.bounding_box import BoundingBox
from src.point import Point
from src.rectangle import Rectangle


class BoundingBoxC1(Rectangle):
    def __init__(self, width: float, height: float, right_upper: Point) -> None:
        super().__init__(width=width, height=height)
        self.right_upper = right_upper
        self.__left_upper = None
        self.__left_lower = None
        self.__right_lower = None
        self.__centre = None

    def __str__(self) -> str:
        return "BoundingBox: right_upper=" + str(self.right_upper) + \
               ", width=" + str(self.width) + ", height=" + str(self.height)

    def convert(self) -> BoundingBox:
        return BoundingBox(width=self.width, height=self.height, left_upper=self.left_lower)

    def shift_by(self, shift: Point) -> None:
        self.right_upper += shift

    def get_shifted(self, shift: Point) -> BoundingBox:
        left_upper_shifted = self.left_upper + shift
        return BoundingBox(left_upper=left_upper_shifted, width=self.width, height=self.height)

    @property
    def left_upper(self) -> Point:
        shift = Point(p=(self.width, 0))
        self.__left_upper = self.right_upper - shift
        return self.__left_upper

    @property
    def left_lower(self) -> Point:
        shift = Point(p=(self.width, self.height))
        self.__left_lower = self.right_upper - shift
        return self.__left_lower

    @property
    def right_lower(self) -> Point:
        shift = Point(p=(0, self.height))
        self.__right_lower = self.left_upper - shift
        return self.__right_lower

    @property
    def centre(self) -> Point:
        shift = Point(p=(self.width / 2, self.height / 2))
        self.__centre = self.left_upper - shift
        return self.__centre

    def get_union(self, other: BoundingBoxC1) -> BoundingBoxC1:
        union_right_upper = Point(p=(max(self.right_upper.x, other.right_upper.x),
                                     max(self.right_upper.y, other.right_upper.y))
                                  )
        union_right_lower = Point(p=(min(self.right_lower.x, other.right_lower.x),
                                     min(self.right_lower.y, other.right_lower.y))
                                  )
        union_height = union_right_upper.y - union_right_lower.y
        union_width = union_right_lower.x - union_right_lower.x
        union = BoundingBoxC1(width=union_width, height=union_height, right_upper=union_right_upper)
        return union

    def get_intersection(self, other: BoundingBoxC1) -> BoundingBoxC1:
        intersection_right_upper = Point(p=(min(self.right_upper.x, other.right_upper.x),
                                            min(self.right_upper.y, other.right_upper.y))
                                         )
        intersection_right_lower = Point(p=(max(self.right_lower.x, other.right_lower.x),
                                            max(self.right_lower.y, other.right_lower.y))
                                         )
        intersection_width = intersection_right_upper.x-intersection_right_lower.x
        intersection_height = intersection_right_upper.y-intersection_right_lower.y

        intersection = None
        if intersection_height > 0 and intersection_width > 0:
            intersection = BoundingBoxC1(width=intersection_width, height=intersection_height,
                                         right_upper=intersection_right_upper)

        return intersection


def main() -> None:
    bounding_box = BoundingBoxC1(width=1, height=1, right_upper=Point(p=(3, 4)))
    bounding_box_other = BoundingBoxC1(width=1.5, height=2, right_upper=Point(p=(4, 5)))
    print(bounding_box)
    print(bounding_box.convert())
    print("A different representation of the bounding box: ", bounding_box.convert())
    print("The intersection of the two bounding boxes: ", bounding_box.get_intersection(bounding_box_other))
    print("The union of the two bounding boxes: ", bounding_box.get_union(bounding_box_other))


if __name__ == "__main__":
    main()
