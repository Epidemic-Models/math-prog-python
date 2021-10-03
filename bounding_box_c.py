from __future__ import annotations

from bounding_box import BoundingBox
from point import Point
from rectangle import Rectangle


class BoundingBoxC(Rectangle):
    def __init__(self, width: float, height: float, left_upper: Point) -> None:
        self.left_upper = left_upper
        super().__init__(width=width, height=height)
        self.__left_lower = None
        self.__right_upper = None
        self.__centre = None

    def __str__(self) -> str:
        return "BoundingBoxA: left_upper=" + str(self.left_upper) +\
               ", right_lower=" + str(self.right_lower)

    def convert(self) -> BoundingBox:
        return BoundingBox(width=self.width, height=self.height, left_upper=self.left_lower)

    def shift_by(self, shift: Point) -> None:
        self.left_upper += shift

    def get_shifted(self, shift: Point) -> BoundingBox:
        left_upper_shifted = self.left_upper + shift
        return BoundingBox(left_upper=left_upper_shifted, width=self.width, height=self.height)

    @property
    def left_lower(self) -> Point:
        shift = Point(p=(0, self.height))
        self.__left_lower = self.left_upper - shift
        return self.__left_lower

    @property
    def right_upper(self) -> Point:
        shift = Point(p=(self.width, 0))
        self.__right_upper = self.left_upper + shift
        return self.__left_lower

    @property
    def centre(self) -> Point:
        shift = Point(p=(self.width / 2, - self.height / 2))
        self.__centre = self.left_upper + shift
        return self.__centre

    def get_union(self, other: BoundingBoxA) -> BoundingBoxA:
        union_left_upper = Point(p=(min(self.left_upper.x, other.left_upper.x),
                                    max(self.left_upper.y, other.left_upper.y))
                                 )
        union_right_lower = Point(p=(max(self.right_lower.x, other.right_lower.x),
                                     min(self.right_lower.y, other.right_lower.y))
                                  )
        union = BoundingBoxA(left_upper=union_left_upper, right_lower=union_right_lower)
        return union

    def get_intersection(self, other: BoundingBoxA) -> BoundingBoxA:
        intersection_left_upper = Point(p=(max(self.left_upper.x, other.left_upper.x),
                                           min(self.left_upper.y, other.left_upper.y))
                                        )
        intersection_right_lower = Point(p=(min(self.right_lower.x, other.right_lower.x),
                                            max(self.right_lower.y, other.right_lower.y))
                                         )
        intersection_width = intersection_right_lower.x-intersection_left_upper.x
        intersection_height = intersection_left_upper.y-intersection_right_lower.y

        intersection = None
        if intersection_height > 0 and intersection_width > 0:
            intersection = BoundingBoxA(left_upper=intersection_left_upper,
                                        right_lower=intersection_right_lower)

        return intersection
