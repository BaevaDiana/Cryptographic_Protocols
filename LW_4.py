# # выделить циклотомические классы
# # найти соответствующие им минимальные многочлены
# # для поля GF(16) для образующего многочлена 11001

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_primitive_elements():
    # поиск примитивных элементов в поле GF(16)
    # примитивные элементы в конечном поле — это такие элементы, которые образуют циклическую группу порядка, равного размеру поля минус 1
    primitive_elements = []
    for i in range(1, 16):
        # примитивный элемент имеет НОД с порядком циклической группы равным 1
        if gcd(i, 15) == 1:
            # добавляем примитив в список
            primitive_elements.append(i)
    return primitive_elements

 # находим циклотомические классы
 # циклотомический класс — это множество элементов, образованных умножением примитивного элемента на себя
def find_cyclotomic_classes(primitive_elements):
    # пустой список циклотомических классов
    cyclotomic_classes = []
    for alpha in primitive_elements:
        # альфа - примитивный элемент из списка примитивных элементов
        class_elements = [alpha]
        beta = alpha
        while beta != 1:
            # умножаем beta на alpha и берем остаток от деления на 15
            beta = (beta * alpha) % 15
            # добавляем полученный элемент в циклотомический класс
            class_elements.append(beta)
        cyclotomic_classes.append(class_elements)
    return cyclotomic_classes

# нахождение минимального многочлена для каждого циклотомического класса
def find_minimal_polynomials(cyclotomic_classes):
    # пустой список минимальных многочленов
    minimal_polynomials = []
    for class_elements in cyclotomic_classes:
        # создание списка coefficients длиной 16, заполненного нуля - коэффициенты минимального многочлена
        coefficients = [0] * 16
        for element in class_elements:
            # элемент присутствует в минимальном многочлене
            coefficients[element] = 1
            # нормализация степени многочлена
        while len(coefficients) > 5:
            coefficients.pop()
        # добавляем коэффициент в минимальный многочлен
        minimal_polynomials.append(coefficients)
    return minimal_polynomials

def main():
    print("Введите коэффициенты образующего многочлена (1 и 0 через пробел):")
    coefficients = list(map(int, input().split()))

    primitive_elements = find_primitive_elements()
    cyclotomic_classes = find_cyclotomic_classes(primitive_elements)
    minimal_polynomials = find_minimal_polynomials(cyclotomic_classes)

    print("\nЦиклотомические классы:")
    for i, class_elements in enumerate(cyclotomic_classes):
        print(f"Класс {i + 1}: {class_elements}")

    print("\nСоответствующие минимальные многочлены:")
    for i, coefficients in enumerate(minimal_polynomials):
        print(f"Класс {i + 1}: {coefficients}")

    # проверка деления на образующий многочлен
    alpha = coefficients.index(1)  # Индекс единичного коэффициента
    if gcd(alpha, 15) == 1:
        print("\nМинимальные многочлены делятся на образующий многочлен.")
    else:
        print("\nМинимальные многочлены не делятся на образующий многочлен.")

if __name__ == "__main__":
    main()

