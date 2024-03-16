from random import randint

class KeyPair:
    def __init__(self, n=128):
        self.public_key, self.private_key = self.Generate(n)

    @staticmethod
    def Generate(n):
        sequence = [randint(1, 1000) for _ in range(n)]
        public_key = [2 ** x for x in sequence]
        private_key = sum(public_key)
        return public_key, private_key

    def GetPublicKey(self):
        return self.public_key

    def GetPrivateKey(self):
        return self.private_key

class CipherText:
    def __init__(self, message, public_key):
        self.cipher_text = self.Encrypt(message, public_key)

    @staticmethod
    def Encrypt(message, public_key):
        cipher_text = []
        for char in message:
            cipher_text.append(ord(char) * public_key[len(cipher_text) % len(public_key)])
        return cipher_text

    def Get(self):
        return self.cipher_text

class PrivateKey:
    def __init__(self, private_key):
        self.private_key = private_key

    def DecipherString(self, cipher_text):
        original_message = ""
        for encrypted_char in cipher_text:
            char_code = encrypted_char // self.private_key  # Используем операцию модуля
            original_message += chr(char_code)
        return original_message


def SavePrivateKeyToFile(private_key, filename="private_key.txt"):
    with open(filename, "w") as file:
        file.write(str(private_key))
    print(f"Приватный ключ сохранен в файл {filename}")

def SaveDecryptedMessageToFile(decrypted_message, filename="./decrypted_message.txt"):
    with open(filename, "w") as file:
        file.write(message)
    print(f"Расшифрованное сообщение сохранено в файл {filename}")


# Пример использования:
key_pair = KeyPair()
print("Публичный ключ:", key_pair.GetPublicKey())

message = "Hello, World!!!"
cipher_text = CipherText(message, key_pair.GetPublicKey()).Get()
private_key = PrivateKey(key_pair.GetPrivateKey())
decrypted_message = private_key.DecipherString(cipher_text)
# print("Зашифрованное сообщение:", cipher_text)
print("Расшифрованное сообщение:", decrypted_message)


SavePrivateKeyToFile(key_pair.GetPrivateKey())
SaveDecryptedMessageToFile(decrypted_message)