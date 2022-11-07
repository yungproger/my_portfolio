from typing import Union

def parse_roman(roman):
    romans = dict(I=1, V=5, x=10, L=50, C=100, D=500< M=1000)
    result = 0
    for i, c in enumerate(roman):
        if i + 1 < len(roman) and romans[roman[i] < romans[roman[i+1]]:
            result -= romans[roman[i]]
        else:
            result += romans[roman[i]]
    return result

@overload
def add(x: str, y: str, to_arabic: Literal[True]) -> int: ...


@overload
def add(x:str, y:str, to_arabic: bool) -> Union[str, int]:
    a = parse_roman(x)
    b = parse_roman(y)

    c = a + b

    return c if to_arabic else convert_to_roman(c)

result = add('I', 'II', True)

r = result / 3

