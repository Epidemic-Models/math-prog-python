from src.bounding_box import BoundingBox
from src.point import Point


def main() -> None:
    bounding_box = BoundingBox(width=6.0, height=4.0, left_upper=Point(p=(2, 3)))
    bounding_box_1 = BoundingBox(width=6.0, height=3.0, left_upper=Point(p=(4.0, 7.0)))
    bounding_box_2 = BoundingBox(width=3.0, height=2.0, left_upper=Point(p=(5.0, 1.0)))
    bounding_box_3 = BoundingBox(width=3.0, height=4.0, left_upper=Point(p=(5.0, 4.0)))
    bounding_box_4 = BoundingBox(width=2.0, height=4.0, left_upper=Point(p=(1.0, 4.0)))
    bounding_box_5 = BoundingBox(width=3.0, height=2.0, left_upper=Point(p=(3.0, 7.0)))
    bounding_box_6 = BoundingBox(width=3.0, height=2.0, left_upper=Point(p=(3.0, 1.0)))
    point = Point(p=(1, 2))

    print("The Bounding Box: ", bounding_box, "\n")
    print("Attributes of bounding box")
    print("The union with left_upper corner inside: \n ", bounding_box.get_union(bounding_box_1), "\n",
          "The intersection with left_upper corner inside: \n ", bounding_box.get_intersection(bounding_box_1), "\n")
    print("The union  with right_upper corner inside: \n ", bounding_box.get_union(bounding_box_2), "\n",
          "The intersection with right_upper corner inside: \n ", bounding_box.get_intersection(bounding_box_2), "\n")
    print("The union  with upper edge inside: \n ", bounding_box.get_union(bounding_box_3), "\n",
          "The intersection with upper edge inside: \n", bounding_box.get_intersection(bounding_box_3), "\n")
    print("The union  with lower edge inside: \n ", bounding_box.get_union(bounding_box_4), "\n",
          "The intersection with lower edge inside: \n ", bounding_box.get_intersection(bounding_box_4), "\n")
    print("The union  with left edge inside: \n ", bounding_box.get_union(bounding_box_5), "\n",
          "The intersection with left edge inside: \n ", bounding_box.get_intersection(bounding_box_5), "\n")
    print("The union  with right edge inside: \n ", bounding_box.get_union(bounding_box_6), "\n",
          "The intersection with right edge inside: \n ", bounding_box.get_intersection(bounding_box_6), "\n")
    print("The shifted bounding box is: \n ", bounding_box_1.get_shifted(point))


if __name__ == '__main__':
    main()
