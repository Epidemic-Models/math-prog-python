from rectangle import Rectangle
from point import Point


class BoundingBox(Rectangle):
    def __init__(self, width: float, height: float, left_upper: Point) -> None:
        super().__init__(width=width, height=height)
        self.left_upper = left_upper

    def __str__(self) -> str:
        return "BoundingBox: left_upper=" + str(self.left_upper) + \
               ", width=" + str(self.width) + ", height=" + str(self.height)


def main() -> None:
    bounding_box = BoundingBox(width=2.0, height=3.0, left_upper=Point(p=(2.3, 4)))
    print(bounding_box)


if __name__ == "__main__":
    main()
