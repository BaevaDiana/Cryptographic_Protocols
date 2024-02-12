
def legendre_symbol(a, p):
    """
    Символ Лежандра для числа a по модулю p.
    Возвращает:
    - 1, если a является квадратичным вычетом по модулю p
    - 0, если a равно 0 по модулю p
    - -1, если a является квадратичным невычетом по модулю p
    """
    if a % p == 0:
        return 0
    return pow(a, (p - 1) // 2, p)

def solve_quadratic_congruence(a, b, m):
    """
    Решает квадратичное сравнение ax^2 ≡ b (mod m).
    :param a: Коэффициент a
    :param b: Коэффициент b
    :param m: Модуль m
    :return: Список решений (если они есть)
    """
    solutions = []
    legendre = legendre_symbol(a, m)

    if legendre == 0:
        # a делится на m, решений нет
        return solutions
    elif legendre == 1:
        # a — квадратичный вычет
        for x in range(m):
            if (a * x**2) % m == b:
                solutions.append(x)
    else:
        # a — квадратичный невычет
        return solutions  # Решений нет

    return solutions

a = int(input("Введите коэффициент а: "))
b = int(input("Введите коэффициент b: "))
m = int(input("Введите коэффициент m: "))

solutions = solve_quadratic_congruence(a, b, m)

if solutions:
    print(f"Решения сравнения {a}x^2 ≡ {b} (mod {m}): {solutions}")
else:
    print(f"Сравнение {a}x^2 ≡ {b} (mod {m}) не имеет решений.")
