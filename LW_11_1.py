# построение SHA-256 для введённого текста (алгоритмическая реализация)

# таблица констант
K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
]

# вычисление хэша SHA-256
def generate_hash(message: bytearray) -> bytearray:

    # проверка типа сообщения и преобразование в байтовый массив
    if isinstance(message, str):
        message = bytearray(message, 'utf-8')
    elif isinstance(message, bytes):
        message = bytearray(message)
    elif not isinstance(message, bytearray):
        raise TypeError

    # Padding
    length = len(message) * 8
    # добавление бита 0х80 (конец сообщения)
    message.append(0x80)
    # добавление нулей пока длина сообщения не кратна 512 бит (необходимая длина для обработки)
    while (len(message) * 8 + 64) % 512 != 0:
        message.append(0x00)

    # добавление длины сообщения в битах
    message += length.to_bytes(8, 'big')
    # проверка завершения дополнения
    assert (len(message) * 8) % 512 == 0, "Дополнение(padding) не выполнено должным образом!"

    # Parsing
    blocks = []
    # разбиение на блоки по 64 байта (512 бита)
    for i in range(0, len(message), 64):
        blocks.append(message[i:i+64])

    # начальные значения хеш-функции
    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h5 = 0x9b05688c
    h4 = 0x510e527f
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19

    # вычисление хэша
    for message_block in blocks:
        message_schedule = []
        # 64 раунда
        for t in range(0, 64):
            if t <= 15:
                # копирование первых 16 слов из блока сообщения
                message_schedule.append(bytes(message_block[t*4:(t*4)+4]))
            else:
                # вычисление остальных сообщения (48) на основе предыдущих
                term1 = _sigma1(int.from_bytes(message_schedule[t-2], 'big'))
                term2 = int.from_bytes(message_schedule[t-7], 'big')
                term3 = _sigma0(int.from_bytes(message_schedule[t-15], 'big'))
                term4 = int.from_bytes(message_schedule[t-16], 'big')

                # представление в виде 4-х байтового сообщения
                schedule = ((term1 + term2 + term3 + term4) % 2**32).to_bytes(4, 'big')
                message_schedule.append(schedule)

        # проверка длины блока сообщения
        assert len(message_schedule) == 64

        # рабочие переменные
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4
        f = h5
        g = h6
        h = h7

        # преобразование переменных на итерациях от t=0 до 63
        for t in range(64):
            t1 = ((h + _capsigma1(e) + _ch(e, f, g) + K[t] +
                   int.from_bytes(message_schedule[t], 'big')) % 2**32)
            t2 = (_capsigma0(a) + _maj(a, b, c)) % 2**32

            # обновление переменных
            h = g
            g = f
            f = e
            e = (d + t1) % 2**32
            d = c
            c = b
            b = a
            a = (t1 + t2) % 2**32

        # вычисление промежуточного кеша
        h0 = (h0 + a) % 2**32
        h1 = (h1 + b) % 2**32
        h2 = (h2 + c) % 2**32
        h3 = (h3 + d) % 2**32
        h4 = (h4 + e) % 2**32
        h5 = (h5 + f) % 2**32
        h6 = (h6 + g) % 2**32
        h7 = (h7 + h) % 2**32

    # итоговый хэш сообщения - сумма элементов последнего блока сообщения
    return ((h0).to_bytes(4, 'big') + (h1).to_bytes(4, 'big') +
            (h2).to_bytes(4, 'big') + (h3).to_bytes(4, 'big') +
            (h4).to_bytes(4, 'big') + (h5).to_bytes(4, 'big') +
            (h6).to_bytes(4, 'big') + (h7).to_bytes(4, 'big'))

# вспомогательные функции

# операция циклического сдвига
def _rotate_right(num: int, shift: int, size: int = 32):
    return (num >> shift) | (num << size - shift)

# циклический сдвиг вправо: 7-18
def _sigma0(num: int):
    num = (_rotate_right(num, 7) ^
           _rotate_right(num, 18) ^
           (num >> 3))
    return num

# циклический сдвиг вправо: 17-19
def _sigma1(num: int):
    num = (_rotate_right(num, 17) ^
           _rotate_right(num, 19) ^
           (num >> 10))
    return num

# циклический сдвиг вправо: 2-13-22
def _capsigma0(num: int):
    num = (_rotate_right(num, 2) ^
           _rotate_right(num, 13) ^
           _rotate_right(num, 22))
    return num

# циклический сдвиг вправо: 6-11-25
def _capsigma1(num: int):
    num = (_rotate_right(num, 6) ^
           _rotate_right(num, 11) ^
           _rotate_right(num, 25))
    return num

# функция choice
def _ch(x: int, y: int, z: int):
    return (x & y) ^ (~x & z)

# функция majority
def _maj(x: int, y: int, z: int):
    return (x & y) ^ (x & z) ^ (y & z)

# вызов функций
if __name__ == "__main__":
    user_input = input("Введите текст: ")
    print(f"SHA-256 хэш для введенного текста: {generate_hash(user_input).hex()}")
