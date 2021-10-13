from complex import Complex


def main() -> None:
    print("Testing functionalities of Complex class: ")
    complex_a = Complex(real=-2, imaginary=-2)
    print("complex_a = " + str(complex_a))
    print("Conjugate of the complex_a = " + str(complex_a.conjugate()))
    complex_b = Complex(real=-2, imaginary=-5)
    print("complex_b = " + str(complex_b))
    print("Conjugate of b = " + str(complex_b.conjugate()))
    print("complex_a == complex_b is " + str(complex_a == complex_b))
    print("complex_a != complex_b is " + str(complex_a != complex_b))
    print("complex_a + complex_b = " + str(complex_a+complex_b))
    print("complex_a - complex_b = " + str(complex_a-complex_b))
    print("complex_a * complex_b = " + str(complex_a*complex_b))
    print("complex_a / complex_b = " + str(complex_a/complex_b))
    n = 5
    print("complex_a ** 5 = " + str(complex_a**n))


if __name__ == '__main__':
    main()
