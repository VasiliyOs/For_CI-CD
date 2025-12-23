import pytest
from calculator import add, subtract, multiply, divide


def test_add():
    """Тест сложения"""
    assert add(2, 2) == 4
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(2.5, 2.5) == 5.0


def test_subtract():
    """Тест вычитания"""
    assert subtract(5, 3) == 2
    assert subtract(10, -5) == 15
    assert subtract(0, 0) == 0


def test_multiply():
    """Тест умножения"""
    assert multiply(4, 3) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0


def test_divide():
    """Тест деления"""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(5, 2) == 2.5


def test_divide_by_zero():
    """Тест деления на ноль"""
    with pytest.raises(ValueError, match="Нельзя делить на ноль"):
        divide(10, 0)


def test_all_operations():
    """Комплексный тест"""
    result = add(multiply(2, 3), subtract(10, divide(8, 2)))
    assert result == 12


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
