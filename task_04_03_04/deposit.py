# Программирование на языке высокого уровня (Python).
# Задание №4.3.4
#
# Выполнил: Погосянц Р.М.
# Группа: ПИН-б-о-22-1
# E-mail: ruspogosyants@bk.ru

class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        self.__numerator: int = numerator
        self.__denominator: int = denominator

    def __str__(self) -> str:
        return f"{self.__numerator}/{self.__denominator}"

    def __add__(self, other: 'Fraction') -> 'Fraction':
        return Fraction(self.__numerator * other.__denominator + other.__numerator * self.__denominator,
                        self.__denominator * other.__denominator)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        return Fraction(self.__numerator * other.__denominator - other.__numerator * self.__denominator,
                        self.__denominator * other.__denominator)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        return Fraction(self.__numerator * other.__numerator, self.__denominator * other.__denominator)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        return Fraction(self.__numerator * other.__denominator, self.__denominator * other.__numerator)

    @classmethod
    def from_string(cls, str_value: str) -> 'Fraction':
        numerator, denominator = map(int, str_value.split('/'))
        return cls(numerator, denominator)

    def save(self, filename: str) -> None:
        import json
        with open(filename, 'w') as f:
            json.dump({'numerator': self.__numerator, 'denominator': self.__denominator}, f)

    @classmethod
    def load(cls, filename: str) -> 'Fraction':
        import json
        with open(filename) as f:
            data = json.load(f)
            return cls(data['numerator'], data['denominator'])

    @property
    def numerator(self) -> int:
        return self.__numerator

    @property
    def denominator(self) -> int:
        return self.__denominator

    def simplify(self) -> 'Fraction':
        gcd = self.__gcd(self.__numerator, self.__denominator)
        return Fraction(self.__numerator // gcd, self.__denominator // gcd)

    def __gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a
)