import random
import string
from dataclasses import dataclass


def generate_password(password_len=10):
    """Генерирует случайный пароль заданной длины."""

    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join([random.choice(chars) for _ in range(password_len)])

    return password


def generate_password2(password_len=12):
    """
    Генерирует пароль заданной длины, который содержит хотя бы
    одну заглавную букву, одну цифру и один специальный символ.
    """

    chars = string.ascii_letters + string.digits + string.punctuation

    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    for _ in range(password_len - 3):
        password.append(random.choice(chars))

    random.shuffle(password)

    return ''.join(password)


@dataclass
class GeneratePassword:
    """
    Класс, который генерирует случайный пароль заданной длины.

    :param password_len: длина пароля
    """

    password_len: int
    password: str = None
    chars: str = string.ascii_letters + string.digits + string.punctuation

    def __post_init__(self):
        if any(
            [
                self.chars
                != string.ascii_letters + string.digits + string.punctuation,
                self.password is not None,
            ]
        ):
            raise ValueError('Нельзя передавать аргументы, кроме password_len')

    def generate_password(self):
        """Генерирует случайный пароль заданной длины."""

        self.password = ''.join(
            [random.choice(self.chars) for _ in range(self.password_len)]
        )

    def get_password(self):
        """Возвращает сгенерированный пароль."""

        print(f'Ваш сгенерированный пароль: {self.password}')


if __name__ == '__main__':
    pass1 = GeneratePassword(100)
    pass1.generate_password()
    pass1.get_password()

    # print(generate_password2(10))
    # print(generate_password1(10))
