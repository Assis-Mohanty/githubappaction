from src.math_operations import add, subtract

def test_add():
    assert add(0,0) == 0
    assert add(1,1) == 2
    assert add(2,2) == 4

def test_subtract():
    assert subtract(2,1) == 1
    assert subtract(1,2) == -1
    assert subtract(2,2) == 0
    

