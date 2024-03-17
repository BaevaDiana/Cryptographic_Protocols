import hashlib

def calculate_sha256(text):
    # Преобразуем текст в байтовую строку
    text_bytes = text.encode('utf-8')

    # Создаем объект хеша SHA-256
    sha256_hash = hashlib.sha256()

    # Обновляем хеш с данными из текста
    sha256_hash.update(text_bytes)

    # Получаем хеш в виде шестнадцатеричной строки
    hashed_text = sha256_hash.hexdigest()

    return hashed_text

# Введите текст для хеширования
user_text = input("Введите текст: ")

# Вычисляем SHA-256 хеш
hashed_result = calculate_sha256(user_text)

print(f"SHA-256 хеш для введенного текста: {hashed_result}")
