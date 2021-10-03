from __future__ import annotations

from bounding_box import BoundingBox
from point import Point
from rectangle import Rectangle


class BoundingBoxF(Rectangle):
    def __init__(self, width: float, height: float, centre: Point) -> None:
        super().__init__(width=width, height=height)
        self.centre = centre
        self.__left_upper = None
        self.__left_lower = None
        self.__right_upper = None
        self.__right_lower = None

    def __str__(self) -> str:
        return "BoundingBoxF: centre=" + str(self.centre) + \
               ", width=" + str(self.width) + ", height=" + str(self.height)

    def convert(self) -> BoundingBox:
        return BoundingBox(self.width, self.height, self.left_lower)

    @property
    def left_upper(self) -> Point:
        shift = Point(p=(- self.width / 2, self.height / 2))
        self.__left_upper = self.centre + shift
        return self.__left_upper

    @property
    def left_lower(self) -> Point:
        shift = Point(p=(- self.width / 2, - self.height / 2))
        self.__left_lower = self.centre + shift
        return self.__left_lower

    @property
    def right_upper(self) -> Point:
        shift = Point(p=(self.width / 2, self.height / 2))
        self.__right_upper = self.centre + shift
        return self.__right_upper

    @property
    def right_lower(self) -> Point:
        shift = Point(p=(self.width / 2, - self.height / 2))
        self.__right_lower = self.centre + shift
        return self.__right_lower

    def get_union(self, other: BoundingBoxF) -> BoundingBoxF:
        union_left_upper = Point(p=(min(self.left_upper.x, other.left_upper.x),
                                    max(self.left_upper.y, other.left_upper.y)
                                    )
                                 )
        union_right_lower = Point(p=(max(self.right_lower.x, other.right_lower.x),
                                     min(self.right_lower.y, other.right_lower.y)
                                     )
                                  )
        union_height = union_left_upper.y - union_right_lower.y
        union_width = union_right_lower.x - union_left_upper.x
        shift = Point(p=(union_width / 2, - union_height / 2))
        union_centre = union_left_upper + shift
        return BoundingBoxF(centre=union_centre, width=union_width, height=union_height)

    def get_intersection(self, other: BoundingBoxF) -> BoundingBoxF:
        intersection_left_upper = Point(p=(max(self.left_upper.x, other.left_upper.x),
                                           min(self.left_upper.y, other.left_upper.y)
                                           )
                                        )
        intersection_right_lower = Point(p=(min(self.right_lower.x, other.right_lower.x),
                                            max(self.right_lower.y, other.right_lower.y)
                                            )
                                         )
        intersection_width = intersection_right_lower.x - intersection_left_upper.x
        intersection_height = intersection_left_upper.y - intersection_right_lower.y

        intersection = None
        if intersection_height > 0 and intersection_width > 0:
            shift = Point(p=(intersection_width / 2, - intersection_height / 2))
            intersection_center = intersection_left_upper + shift
            intersection = BoundingBoxF(centre=intersection_center,
                                        width=intersection_width, height=intersection_height
                                        )
        return intersection




if __name__ == "__main__":
    main()
