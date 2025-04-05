numeros_romanos = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def decimal_to_roman(num: int) -> str:
    if isinstance(num, int) and (num >= 1) and (num <= 3999):
        resultado = ""
        for entero, simbolo in numeros_romanos:
            while num >= entero:
                resultado = resultado + simbolo
                num = num - entero
        return resultado


if __name__ == "__main__":
    print(decimal_to_roman(int(input("Ingrese numero"))))
