from __future__ import annotations

from src.bounding_box import BoundingBox
from src.point import Point
from src.rectangle import Rectangle


class BoundingBoxA(Rectangle):
    def __init__(self, left_upper: Point, right_lower: Point) -> None:
        self.left_upper = left_upper
        self.right_lower = right_lower
        width = self.right_lower.x - self.left_upper.x
        height = self.left_upper.y - self.right_lower.y
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
        self.right_lower += shift
        self.__right_upper += shift
        self.__left_lower += shift
        self.__centre += shift

    def get_shifted(self, shift: Point) -> BoundingBoxA:
        left_upper_shifted = self.left_upper + shift
        right_lower_shifted = self.right_lower + shift
        return BoundingBoxA(left_upper=left_upper_shifted, right_lower=right_lower_shifted)

    @property
    def left_lower(self) -> Point:
        shift = Point(p=(0, self.height))
        self.__left_lower = self.left_upper - shift
        return self.__left_lower

    @property
    def right_upper(self) -> Point:
        shift = Point(p=(0, self.height))
        self.__right_upper = self.right_lower + shift
        return self.__right_upper

    @property
    def centre(self) -> Point:
        shift = Point(p=(self.width / 2, - self.height / 2))
        self.__centre = self.left_upper + shift
        return self.__centre

    def attribute(self) -> str:
        return "Attributes of BoundingBoxA in the usual co-ordinate system:  \n left_upper: " + str(self.left_upper) + \
               ", right_upper: " + str(self.right_upper) + ", left_lower: " + str(self.left_lower) + ", right_lower: " \
               + str(self.right_lower) + ", centre: " + str(self.centre) + ", width: " + str(self.width) + \
               ", height: " + str(self.height)

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

    def get_difference(self, other: BoundingBoxA) -> str:
        intersection = self.get_intersection(other=other)
        return "(" + str(self) + ") \\ (" + str(intersection) + ")"

    def get_symmetric_difference(self, other: BoundingBoxA) -> str:
        intersection = self.get_intersection(other=other)
        return "((" + str(self) + ") U (" + str(other) + ")) \\ (" + str(intersection) + ")"


def main() -> None:
    bounding_box_a = BoundingBoxA(left_upper=Point(p=(2, 7)), right_lower=Point(p=(9, 3)))
    bounding_box_other = BoundingBoxA(left_upper=Point(p=(4, 5)), right_lower=Point(p=(13, 1)))
    print(bounding_box_a)
    point = Point(p=(1, 1))
    print("Representation of the boundingBoxA in the alternate co-ordinate system: ", bounding_box_a.convert())
    print("The intersection of the two bounding boxes: ", bounding_box_a.get_intersection(bounding_box_other))
    print("The union of the two bounding boxes: ", bounding_box_a.get_union(bounding_box_other))
    print("Shifted bounding box: ", bounding_box_a.get_shifted(point))
    print("Difference: ", bounding_box_a.get_difference(bounding_box_other))
    print("Symmetric Difference: ", bounding_box_a.get_symmetric_difference(bounding_box_other))
    print(bounding_box_a.attribute())
    print("shifted bounding_box_a: ", bounding_box_a.get_shifted(point))


if __name__ == "__main__":
    main()
