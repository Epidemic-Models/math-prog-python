from __future__ import annotations


class Point:
    def __init__(self, p: tuple) -> None:
        self.x = p[0]
        self.y = p[1]

    def __str__(self) -> str:
        return "Point(" + str(self.x) + "," + str(self.y) + ")"

    def __add__(self, other: Point) -> Point:
        result = (self.x + other.x, self.y + other.y)
        return Point(p=result)

    def __sub__(self, other: Point) -> Point:
        result = (self.x - other.x, self.y - other.y)
        return Point(p=result)
