import random


def is_prime_fermat(n, k):
    """
    Выполняет тест Ферма для заданного числа.
    :param n: Число, которое нужно проверить
    :param k: Количество итераций (тестов)
    :return: True, если n вероятно простое, иначе False
    """
    if n <= 1:
        return False
    if n == 2:
        return False

    for _ in range(k):
        a = random.randint(2, n - 1)
        if pow(a, n - 1, n) != 1:
            return False

    return True



# Выполняем тесты Ферма для чисел от 1 до 100
print("Введите количество тестов:")
k = int(input())
print("Введите количество чисел:")
num_numbers = int(input())
# Выполняем тесты Ферма для чисел от 1 до 100
for num in range(2, num_numbers):
    is_prime = is_prime_fermat(num, k)
    if is_prime:
        print(f"{num} вероятно простое")
    else:
        print(f"{num} вероятно составное")


