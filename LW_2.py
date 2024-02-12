# решение квадратичных сравнений вида ax^2 ≡ b (mod m)

import math

def is_prime(number):
    """
    Проверяет, является ли число простым.
    """
    if number <= 1:
        return False

    sqrt_num = int(math.sqrt(number))
    for count in range(2, sqrt_num + 1):
        if number % count == 0:
            return False
    return True

def factorize(n):
    """
    Разлагает число n на простые множители.
    """
    factors = []
    p = 2
    while True:
        while n % p == 0 and n > 0:
            factors.append(p)
            n = n // p
        p += 1
        if p > n // p:
            break
    if n > 1:
        factors.append(n)
    return factors

def legendre_symbol(a, p):
    """
    Вычисляет символ Лежандра (a|p).
    """
    if a % p == 0:
        legendre_symbol = 0
    elif not is_prime(p):
        # если p не является простым числом, выполняется разложение его на простые множители
        factors = factorize(p)
        legendre_symbol = 1
        for factor in factors:
            exponent = (p - 1) // factor
            legendre_symbol *= pow(a, exponent, p)
            legendre_symbol %= p
    else:
        # если p - простое число, вычислим символ Лежандра напрямую
        legendre_symbol = pow(a, (p - 1) // 2, p)

    return legendre_symbol

def solve_quadratic_congruence(a, b, m):
    """
    Решает квадратичное сравнение ax^2 ≡ b (mod m).
    :param a: Коэффициент a
    :param b: Коэффициент b
    :param m: Модуль m
    :return: Список решений (если они есть)
    """
    # список решений
    solutions = []
    # вычисление символа Лежандра
    legendre = legendre_symbol(a, m)

    # решений нет
    if legendre == 0:
        return solutions
    # решения есть
    elif legendre == 1:
        for x in range(m):
            if (a * x**2) % m == b:
                solutions.append(x)
        return solutions
    # решений нет
    else:
        return solutions

a = int(input("Введите коэффициент а: "))
b = int(input("Введите коэффициент b: "))
m = int(input("Введите коэффициент m: "))

# получение списка решений
solutions = solve_quadratic_congruence(a, b, m)

if solutions:
    print(f"Решения сравнения {a}x^2 ≡ {b} (mod {m}): {solutions}")
else:
    print(f"Сравнение {a}x^2 ≡ {b} (mod {m}) не имеет решений.")
