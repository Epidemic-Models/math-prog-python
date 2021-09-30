from rectangle import Rectangle
from point import Point


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
        shift = Point(p=(self.width, self.height))
        self.__right_lower = self.left_upper + shift
        return self.__right_lower


def main() -> None:
    bounding_box = BoundingBox(width=2.0, height=3.0, left_upper=Point(p=(2.3, 4.3)))
    print(bounding_box)
    print("The right lower corner: ", bounding_box.right_lower)


if __name__ == "__main__":
    main()
