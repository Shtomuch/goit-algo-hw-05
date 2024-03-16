def caching_fibonacci():
    cache = {}

    def fibonachi(n):
        if n in cache:
            return cache[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        cache[n] = fibonachi(n-1) + fibonachi(n-2)
        return cache[n]
    return fibonachi


# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
