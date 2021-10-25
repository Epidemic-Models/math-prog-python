from src.complex import Complex


def main() -> None:
    print("Testing functionalities of Complex class: ",  "\n")

    print("The complex numbers in canonical form = trigonometric form: ")
    complex_a = Complex(re=2, im=2)
    print("complex_a = " + str(complex_a))
    complex_b = Complex(re=-5, im=-0.9)
    print("complex_b = " + str(complex_b))
    complex_c = Complex(re=-2.7, im=5)
    print("complex_c = " + str(complex_c))
    complex_d = Complex(re=6, im=-4)
    print("complex_d = " + str(complex_d))
    complex_e = Complex(re=2.7, im=0)
    print("complex_e = " + str(complex_e))
    complex_f = Complex(re=0, im=5.3)
    print("complex_f = " + str(complex_f))
    complex_g = Complex(re=5.9)
    print("complex_g = " + str(complex_g))
    complex_h = Complex(re=0, im=0)
    print("complex_h = " + str(complex_h), "\n")
    real_a = 4
    real_b = -4

    print("Conjugates of the given complex numbers:")
    print("Conjugate of the complex_a = " + str(complex_a.conjugate()))
    print("Conjugate of the complex_b = " + str(complex_b.conjugate()))
    print("Conjugate of the complex_c = " + str(complex_c.conjugate()))
    print("Conjugate of the complex_d = " + str(complex_d.conjugate()))
    print("Conjugate of the complex_e = " + str(complex_e.conjugate()))
    print("Conjugate of the complex_f= " + str(complex_f.conjugate()),  "\n")

    print("Test whether two complex numbers are equal or not equal:")
    print("complex_a == complex_b is " + str(complex_a == complex_b))
    print("complex_a != complex_b is " + str(complex_a != complex_b),  "\n")

    print("Test the addition and subtraction methods:")
    print("complex_a + complex_b = " + str(complex_a + complex_b))
    print("complex_a + complex_g = " + str(complex_a + complex_g))
    print("complex_a - complex_g = " + str(complex_a - complex_g))
    print("complex_a - complex_b = " + str(complex_a - complex_b),  "\n")

    print("Find the nth power of a complex number:")
    n = 5
    print("complex_a ** 5 = " + str(complex_a ** n),  "\n")

    print("Test method to add a real and a complex number.")
    print("real_a + complex_a = " + str(real_a + complex_a))
    print("real_b + complex_a = " + str(real_b + complex_a), "\n")

    print("Test method to find the difference of a real and a complex number.")
    print("real_a - complex_a = " + str(real_a - complex_a), "\n")

    print("Test method to find the product of a real and a complex number.")
    print("real_a * complex_a = " + str(real_a * complex_a), "\n")

    print("Test method to find the quotient of a real and a complex number.")
    print("real_a / complex_a = " + str(real_a / complex_a), "\n")

    print("Test the multiplication and division methods")
    print("complex_a * complex_b = " + str(complex_a * complex_b))
    print("complex_a * complex_h = " + str(complex_a * complex_h))
    print("complex_a * complex_g = " + str(complex_a * complex_g))
    print("complex_a / complex_h = " + str(complex_a / complex_h),  "\n")


if __name__ == '__main__':
    main()
