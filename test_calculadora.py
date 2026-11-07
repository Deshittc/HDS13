
from calculadora import sumar, restar, multiplicar

def test_sumar():
    assert sumar(5, 3) == 8

def test_restar():
    assert restar(10, 5) == 5

def test_multiplicar():
    assert multiplicar(4, 3) == 12
