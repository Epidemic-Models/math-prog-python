class Point:
    def __init__(self, p: tuple) -> None:
        self.x = p[0]
        self.y = p[1]

    def __str__(self) -> str:
        return "Point(" + str(self.x) + "," + str(self.y) + ")"
