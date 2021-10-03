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

    def __str__(self):
        return "BoundingBoxF: centre=" + str(self.centre) + \
               ", width=" + str(self.width) + ", height=" + str(self.height)

    def convert(self):
        return BoundingBox(left_upper=)

def main():
    bounding_box_f = BoundingBoxF(centre=(3, 5), width=3, height=3)
    print(bounding_box_f)


if __name__ == "__main__":
    main()
