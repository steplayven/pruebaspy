import pytest
from numerosAmigos import numeros_amigos

def test_numerosamigo():
    assert numeros_amigos(4,8) == "4 y 8 son amigos"
    print("Esta bien")
    
def test_numerosamigo2():
    assert numeros_amigos(4,8) == '4 y 8 son amigos'
    print("Esta bien")

def test_numerosamigo3():
    assert numeros_amigos(4,8) == '4 y 8 son amigos'
    print("Esta bien")

def test_numerosamigo4():
    assert numeros_amigos(4,8) == '4 y 8 son amigos'
    print("Esta bien")
    
def test_numerosamigo5():
    assert numeros_amigos(4,8) == '4 y 8 son amigos'
    print("Esta bien")

def test_numerosamigo6():
    assert numeros_amigos(4,8) == '4 y 8 no son amigos'
    print("Esta bien")

def test_numerosamigo7():
    assert numeros_amigos(4,8) == '4 y 8 no son amigos'
    print("Esta bien")

def test_numerosamigo8():
    assert numeros_amigos(4,8) == '4 y 8 no son amigos'
    print("Esta bien")
    
def test_numerosamigo9():
    assert numeros_amigos(4,8) == '4 y 8 no son amigos'
    print("Esta bien")
    
def test_numerosamigo10():
    assert numeros_amigos(4,8) == '4 y 8 no son amigos'
    print("Esta bien")

if __name__ == '__main__':
    test_numerosamigo()
    test_numerosamigo2()
    test_numerosamigo3()
    test_numerosamigo4()
    test_numerosamigo5()
    test_numerosamigo6()  
    test_numerosamigo7()
    test_numerosamigo8()
    test_numerosamigo9()  
    test_numerosamigo10()   