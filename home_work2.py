import re


def generator_numbers(text: str):
    list_of_word = text.split(" ")
    pattern = r"\d+"  # pattern for numbers
    for i in list_of_word:
        if re.match(pattern, i) is not None:
            yield i


def sum_profit(text: str, func: callable):
    sum = 0
    for i in func(text):
        sum += float(i)
    return sum


text = ("Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід,"
        " доповнений додатковими надходженнями 27.45 і 324.00 доларів.")
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")







"""Варіант 2"""


"""import re

def generator_numbers(text: str):
    # Використання регулярного виразу для пошуку дійсних чисел
    pattern = r'-?\b\d+(\.\d+)?\b'
    for match in re.finditer(pattern, text):
        # Повернення чисел як чисел з плаваючою точкою
        yield float(match.group())

def sum_profit(text: str, func):
    # Ініціалізація загальної суми
    total_sum = 0
    # Ітерація по генератору та сумування чисел
    for number in func(text):
        total_sum += number
    return total_sum

# Використання функцій
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
"""