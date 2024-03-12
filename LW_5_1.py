import random

def is_prime_fermat(n, k=5):
    """
    Проверяет число на простоту с помощью теста Ферма.
    :param n: Число для проверки
    :param k: Количество тестов (по умолчанию 1)
    :return: True, если вероятно простое, False, если составное
    """
    if n <= 1:
        return False
    if n == 2:
        return True

    def power(x, y, p):
        res = 1
        x = x % p
        while y > 0:
            if y % 2 == 1:
                res = (res * x) % p
            y = y // 2
            x = (x * x) % p
        return res

    # Выполняем k тестов
    for _ in range(k):
        a = 2 + (n - 4) * random.random()
        a = int(a)
        if power(a, n - 1, n) != 1:
            return False

    return True

def find_composite_numbers(limit, num_tests):
    """
    Находит составные числа до заданного предела, для которых первый тест дает ответ "простое".
    :param limit: Верхний предел для проверки чисел
    :param num_tests: Количество тестов
    :return: Список составных чисел
    """
    composite_numbers = []
    for num in range(4, limit + 1):
        if is_prime_fermat(num, num_tests):
            composite_numbers.append(num)
    return composite_numbers

# Устанавливаем предел в один миллиард и количество тестов в 100
limit = 10**3
num_tests = 100

# Находим составные числа и выводим результаты
composite_numbers = find_composite_numbers(limit, num_tests)
print(f"Составные числа до {limit}, для которых первый тест дает ответ 'простое':")
print(composite_numbers)
