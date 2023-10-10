# Программирование на языке высокого уровня (Python).
# Задание №4.3.5
#
# Выполнил: Погосянц Р.М.
# Группа: ПИН-б-о-22-1
# E-mail: ruspogosyants@bk.ru

class FractionCollection:
    def __init__(self, *args: 'Fraction') -> None:
        self._data: List['Fraction'] = list(args)

    def __str__(self) -> str:
        return '\n'.join(str(fraction) for fraction in self._data)

    def __getitem__(self, index: Union[int, slice]) -> Union['Fraction', List['Fraction']]:
        return self._data[index]

    def add(self, value: 'Fraction') -> None:
        self._data.append(value)

    def remove(self, index: int) -> None:
        del self._data[index]

    def save(self, filename: str) -> None:
        import json
        with open(filename, 'w') as f:
            json.dump([str(fraction) for fraction in self._data], f)

    def load(self, filename: str) -> None:
        import json
        with open(filename) as f:
            data = json.load(f)
            self._data = [Fraction.from_string(str_value) for str_value in data]
