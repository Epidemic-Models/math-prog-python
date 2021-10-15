from complex import Complex


def main() -> None:
    print("Testing functionalities of Complex class: ")
    complex_a = Complex(re=2, im=-2)
    print("complex_a = " + str(complex_a))
    print("Conjugate of the complex_a = " + str(complex_a.conjugate()))
    complex_b = Complex(re=2, im=0)
    print("complex_b = " + str(complex_b))
    print("Conjugate of b = " + str(complex_b.conjugate()))
    print("complex_a == complex_b is " + str(complex_a.__eq__(complex_b)))
    print("complex_a != complex_b is " + str(complex_a.__ne__(complex_b)))
    print("complex_a + complex_b = " + str(complex_a.__add__(complex_b)))
    print("complex_a - complex_b = " + str(complex_a.__sub__(complex_b)))
    print("complex_a * complex_b = " + str(complex_a.__mul__(complex_b)))
    print("complex_a / complex_b = " + str(complex_a.__truediv__(complex_b)))
    n = 5
    print("complex_a ** 5 = " + str(complex_a.__pow__(n)))


if __name__ == '__main__':
    main()
