def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


class Fraction:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator
        self._normalize()

    def _normalize(self):
        divider = gcd(self.__denominator, self.__numerator)
        self.__denominator //= divider
        self.__numerator //= divider

    def _get_numerator(self):
        return self.__numerator

    def _get_denominator(self):
        return self.__denominator

    def __str__(self):
        return str(self.__numerator) + '/' + str(self.__denominator)

    def __add__(self, other):
        numerator = (
                self.__numerator * other._get_denominator()
                + self.__denominator * other._get_numerator()
        )
        denominator = self.__denominator * other._get_denominator()
        return Fraction(numerator, denominator)

    def __radd__(self, other):
        if other._get_numerator == 0:
            return self
        return self + other

    def __lt__(self, other):
        return self.__numerator * other._get_denominator() < self.__denominator * other._get_numerator()


x = Fraction(4, 2)
y = Fraction(3, 2)

print(x + y)

z = x + y

print(x, y, z)
print(x < y)

fraction = [Fraction(1, 2), Fraction(5, 2), Fraction(12, 3), Fraction(0, 2)]
print(*fraction)
print(*sorted(fraction))
