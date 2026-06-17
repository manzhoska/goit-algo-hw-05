
def caching_fibonacci():
    cache = {}

    # реалізую замикання для збереження обчислених значень чисел Фібоначчі
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache: 
            return cache[n]
        
        # Якщо значення не обчислено раніше, обчислюємо його рекурсивно та зберігаємо в cache
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
    
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10)) 
print(fib(15))  # Виведе 610
