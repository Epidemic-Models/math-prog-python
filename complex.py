from __future__ import annotations
import math
from typing import Union


class Complex:
    def __init__(self, re: Union[float, int], im: Union[float, int]) -> None:
        """
        Constructor for a complex number, represented in it's canonical form
        :param Union[float, int] re: real part of the complex number
        :param Union[float, int] im: imaginary part of the complex number
        """
        if isinstance(re, float) or isinstance(re, int):
            self.re = re
        else:
            raise Exception("The real part being passed is neither a float nor an integer.")

        if isinstance(im, float) or isinstance(im, int):
            self.im = im
        else:
            raise Exception("The imaginary part being passed is neither a float nor an integer.")

        self.__r = None
        self.__phi = None

    @property
    def r(self) -> float:
        """
        Returns the modulus of the complex number
        :return float: modulus of the complex number
        """
        self.__r = math.sqrt(self.re ** 2 + self.im ** 2)
        return self.__r

    @property
    def phi(self) -> float:
        """
        Returns the argument of a complex number
        :return float: argument of a complex number
        """
        if self.re == 0.0:
            if self.im == 0.0:
                self.__phi = 0.0
            elif self.im > 0.0:
                self.__phi = math.pi / 2.0
            else:
                self.__phi = 3.0 * math.pi / 2.0
        elif self.re > 0.0:
            if self.im >= 0.0:
                self.__phi = math.atan(self.im / self.re)
            else:
                self.__phi = math.atan(self.im / self.re) + 2.0 * math.pi
        else:
            self.__phi = math.atan(self.im / self.re) + math.pi
        return self.__phi

    def __str__(self) -> str:
        """
        Converts a complex number into string format
        :return string: a string containing the complex number
                        in "canonical form = trigonometric form" format
        """
        if self.re == 0.0:
            if self.im == 0.0:
                event = "0"
            elif self.im == 1.0:
                event = "i"
            elif self.im == -1.0:
                event = "-i"
            else:
                event = format(self.im, '.3g') + "i"
        else:
            event = format(self.re)
            if self.im == 0.0:
                event = format(self.re)
            elif self.im == 1.0:
                event += "i"
            elif self.im == -1.0:
                event += "-i"
            elif self.im > 0:
                event += " + " + format(self.im, '.3g') + "i"
            elif self.im < 0:
                event += " - " + format(-self.im, '.3g') + "i"

        event += " = "
        phi_str = ""
        phi_div_pi = self.phi / math.pi
        phi_str += format(phi_div_pi, '.3g') + "\u03C0"
        if self.r == 0.0:
            event += "0"
        else:
            event += format(self.r, '.3g') + " * (cos(" + phi_str + ") + sin(" + phi_str + ")i" + ")"

        return event

    def __eq__(self, other: Union[int, float, Complex]) -> bool:
        """
        Determines the equality of two complex numbers
        :param Union[int, float, Complex] other: the other complex number
        :return bool: True if and only if self is equal to other
        """
        if isinstance(other, int) or isinstance(other, float):
            return (self.re == float(other)) and (self.im == 0.0)
        elif isinstance(other, Complex):
            return (self.re == other.re) and (self.im == other.im)
        else:
            raise Exception("The right hand operand must be either an integer, or a float or a Complex number.")

    def __ne__(self, other: Union[int, float, Complex]) -> bool:
        """
        Determines if two complex numbers are different
        :param Union[int, float, Complex] other: the other complex number
        :return bool: True if and only if self is not equal to other
        """
        return not (self == other)

    def __add__(self, other: Union[float, int, Complex]) -> Complex:
        """
        Returns the sum of two complex numbers
        :param Union[int, float, Complex] other: the other complex number
        :return Complex: the sum of the self and the other
        """
        if isinstance(other, float) or isinstance(other, int):
            return Complex(re=self.re + other, im=self.im)
        elif isinstance(other, Complex):
            return Complex(re=self.re + other.re, im=self.im + other.im)
        else:
            raise Exception("The right hand operand must be either an integer, or a float or a Complex number.")

    def __sub__(self, other: Union[float, int, Complex]) -> Complex:
        """
        Returns the difference of two complex numbers
        :param Union[int, float, Complex] other: the other complex number
        :return: the difference of the self and the other
        """
        if isinstance(other, float) or isinstance(other, int):
            return Complex(re=self.re - other, im=self.im)
        elif isinstance(other, Complex):
            return Complex(re=self.re - other.re, im=self.im - other.im)
        else:
            raise Exception("The right hand operand must be either an integer, or a float or a Complex number.")

    def __mul__(self, other: Union[int, float, Complex]) -> Complex:
        """
        Returns the product of two complex numbers
        :param Union[int, float, Complex] other: the other complex number
        :return Complex: the product of the self and the other
        """
        if isinstance(other, int) or isinstance(other, float):
            return Complex(re=self.re * other, im=self.im * other)
        elif isinstance(other, Complex):
            return Complex(re=self.re * other.re - self.im * other.im,
                           im=self.re * other.im + self.im * other.re)
        else:
            raise Exception("The right hand operand must be either an integer, or a float or a Complex number.")

    def conjugate(self) -> Complex:
        """
        Returns the conjugate of a complex number
        :return Complex: the conjugate of self
        """
        return Complex(re=self.re, im=-self.im)

    def __truediv__(self, other: Union[int, float, Complex]) -> Complex:
        """
        Returns the quotient of two complex numbers
        :param Union[int, float, Complex] other: other complex number
        :return Complex: the quotient of the self and the other
        """
        if isinstance(other, int) or isinstance(other, float):
            if float(other) == 0.0:
                raise ZeroDivisionError
            else:
                return Complex(re=self.re / other, im=self.im / other)
        elif isinstance(other, Complex):
            return self * other.conjugate() / (other.r ** 2)
        else:
            raise Exception("The right hand operand must be either an integer, or a float or a Complex number.")

    def __pow__(self, n: int) -> Complex:
        """
        Returns the integer power of a complex number
        :param int n: exponent
        :return Complex: the nth power of self
        """
        if not isinstance(n, int):
            raise Exception("The exponent must be an integer!")
        r_power_n = self.r ** n
        n_phi = self.phi * n
        return Complex(re=r_power_n * math.cos(n_phi), im=r_power_n * math.sin(n_phi))


def main() -> None:
    print("Testing functionalities of Complex class: ")
    a = Complex(re=-2, im=-2)
    print("a = " + str(a))


if __name__ == '__main__':
    main()
