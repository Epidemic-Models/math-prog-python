from bounding_box import BoundingBox
from point import Point


def main() -> None:
    bounding_box_1 = BoundingBox(width=6.0, height=4.0, left_upper=Point(p=(2, 3)))
    bounding_box_2 = BoundingBox(width=6.0, height=3.0, left_upper=Point(p=(4.0, 7.0)))
    bounding_box_3 = BoundingBox(width=3.0, height=2.0, left_upper=Point(p=(5.0, 5.0)))
    bounding_box_4 = BoundingBox(width=2.0, height=3.0, left_upper=Point(p=(2.0, 5.0)))
    bounding_box_5 = BoundingBox(width=3.0, height=2.0, left_upper=Point(p=(3.0, 2.0)))
    bounding_box_6 = BoundingBox(width=3.0, height=2.0, left_upper=Point(p=(3.0, 7.0)))

    point = Point(p=(1, 2))
    print("The Bounding Box: ", bounding_box_1)
    print("The union with left_upper corner inside: ", bounding_box_1.get_union(bounding_box_2), "\n",
          "the intersection with left_upper corner inside: ", bounding_box_1.get_intersection(bounding_box_2), "\n")
    print("The union  with right_upper corner inside: ", bounding_box_1.get_union(bounding_box_3), "\n",
          "the intersection with right_upper corner inside: ", bounding_box_1.get_intersection(bounding_box_3), "\n")
    print("The union  with upper edge inside: ", bounding_box_1.get_union(bounding_box_3), "\n",
          "the intersection with upper edge inside: ", bounding_box_1.get_intersection(bounding_box_3), "\n")
    print("The union  with lower edge inside: ", bounding_box_1.get_union(bounding_box_3), "\n",
          "the intersection with lower edge inside: ", bounding_box_1.get_intersection(bounding_box_4), "\n")
    print("The union  with right edge inside: ", bounding_box_1.get_union(bounding_box_4), "\n",
          "the intersection with right edge inside: ", bounding_box_1.get_intersection(bounding_box_5), "\n")
    print("The union  with left edge inside: ", bounding_box_1.get_union(bounding_box_4), "\n",
          "the intersection with left edge inside: ", bounding_box_1.get_intersection(bounding_box_6), "\n")


if __name__ == '__main__':
    main()
