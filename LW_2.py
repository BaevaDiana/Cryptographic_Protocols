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
    elif pow(a, (p - 1) // 2, p) == 1:
        legendre_symbol = 1
    else:
        legendre_symbol = -1
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

    if legendre == 1:
        if is_prime(m):
            print("Сравнение с простым модулем")
            # случай, когда m - простое число
            if m > 2:
            # a имеет квадратный корень по модулю m
                sqrt_a = pow(a, (m + 1) // 4, m)
                x1 = (sqrt_a * b) % m
                x2 = m - x1
                solutions.append(x1)
                solutions.append(x2)
                return solutions
            else:
                return solutions
        # случай, когда m - степень простого числа:
        elif not is_prime(m) and len(factorize(m)) == 1:
            print("Сравнение с составным модулем - степень простого числа")
            for x in range(m):
                if (a * x**2) % m == b:
                    solutions.append(x)
            return solutions

        # случай, когда m - составное число, которое раскладывается на простые множители
        else:
            print("Сравнение с составным модулем - множители простого числа")
            for x in range(m):
                if (a * x ** 2) % m == b:
                    solutions.append(x)
            return solutions
    else:
        return solutions


a = int(input("Введите коэффициент а: "))
b = int(input("Введите коэффициент b: "))
m = int(input("Введите коэффициент m: "))

# получение списка решений
solutions = solve_quadratic_congruence(a, b, m)

if solutions :
    print(f"Решения сравнения {a}*x^2 ≡ {b} (mod {m}): {solutions}")
else:
    print(f"Сравнение {a}*x^2 ≡ {b} (mod {m}) не имеет решений.")
