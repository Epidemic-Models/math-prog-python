from __future__ import annotations
from typing import Union

from point import Point
from rectangle import Rectangle


class BoundingBox(Rectangle):
    def __init__(self, width: Union[float, int],
                 height: Union[float, int],
                 left_upper: Union[Point, tuple]) -> None:
        """
        Constructor for the bounding box D representation
        The representation uses left upper corner in rotated co-ordinate system,
        and the width and the height of the bounding box
        :param Union[float, int] width: width of the rectangle (dimension y)
        :param Union[float, int] height: height of the rectangle (dimension x)
        :param Union[Point, tuple] left_upper: left upper corner of the rectangle
        :return None
        """
        super().__init__(width=width, height=height)
        if isinstance(left_upper, Point):
            self.left_upper = left_upper
        elif isinstance(left_upper, tuple):
            self.left_upper = Point(p=left_upper)
        else:
            raise Exception("Left upper corner, which was passed is neither a point nor a tuple.")

        self.__right_upper = None
        self.__left_lower = None
        self.__right_lower = None
        self.__centre = None

    def __str__(self) -> str:
        return "BoundingBox: left_upper=" + str(self.left_upper) + \
               ", width=" + str(self.width) + ", height=" + str(self.height)

    @property
    def right_upper(self) -> Point:
        shift = Point(p=(0, self.width))
        self.__right_upper = self.left_upper + shift
        return self.__right_upper

    @property
    def left_lower(self) -> Point:
        shift = Point(p=(self.height, 0))
        self.__left_lower = self.left_upper + shift
        return self.__left_lower

    @property
    def right_lower(self) -> Point:
        shift = Point(p=(self.height, self.width))
        self.__right_lower = self.left_upper + shift
        return self.__right_lower

    @property
    def centre(self) -> Point:
        shift = Point(p=(self.height / 2, - self.width / 2))
        self.__centre = self.left_upper + shift
        return self.__centre

    def attribute(self) -> str:
        return "Attributes of BoundingBox:  \n left_upper: " + str(self.left_upper) + \
               ", right_upper: " + str(self.right_upper) + ", left_lower: " + str(self.left_lower) + ", right_lower: " \
               + str(self.right_lower) + ", centre: " + str(self.centre) + ", width: " + str(self.width) + \
               ", height: " + str(self.height)

    def shift_by(self, shift: Point) -> None:
        self.left_upper += shift
        self.__right_upper += shift
        self.__left_lower += shift
        self.__right_lower += shift
        self.__centre += shift

    def get_shifted(self, shift: Point) -> BoundingBox:
        left_upper_shifted = self.left_upper + shift
        return BoundingBox(left_upper=left_upper_shifted, width=self.width, height=self.height)

    def get_union(self, other: BoundingBox) -> BoundingBox:
        union_left_upper = Point(p=(min(self.left_upper.x, other.left_upper.x),
                                    min(self.left_upper.y, other.left_upper.y)
                                    )
                                 )
        union_right_lower = Point(p=(max(self.right_lower.x, other.right_lower.x),
                                     max(self.right_lower.y, other.right_lower.y)
                                     )
                                  )
        union_width = union_right_lower.y - union_left_upper.y
        union_height = union_right_lower.x - union_left_upper.x
        union = BoundingBox(left_upper=union_left_upper, width=union_width, height=union_height)
        return union

    def get_intersection(self, other: BoundingBox) -> BoundingBox:
        """
        Returns the intersection of the actual bounding box and the other one,
        the intersection is the common part of both the bounding boxes, and it is a bounding box.
        The other and the resulting bounding box has the same representation as the actual one.
        :param BoundingBox other: input bounding box, with which the intersection is calculated
        :return BoundingBox: the intersection of the two bounding boxes,
        if it exists, otherwise it is None
        """
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
    point1 = Point(p=(1, 1))
    print(bounding_box)
    print("The right lower corner: ", bounding_box.right_lower)
    bounding_box_2 = BoundingBox(width=1, height=1, left_upper=Point(p=(3.3, 5.3)))
    print(bounding_box.get_intersection(other=bounding_box_2))
    print(bounding_box.attribute())
    print("shifted bounding box: ", bounding_box.get_shifted(point1))


if __name__ == "__main__":
    main()
