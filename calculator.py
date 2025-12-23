def add(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract(a, b):
    """Вычитание двух чисел"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def divide(a, b):
    """Деление двух чисел"""
    if b == 0:
        raise ValueError("Нельзя делить на ноль")
    return a / b

if __name__ == "__main__":
    # Простой пример использования
    print("2 + 2 =", add(2, 2))
    print("5 - 3 =", subtract(5, 3))
    print("4 * 3 =", multiply(4, 3))
    print("10 / 2 =", divide(10, 2))