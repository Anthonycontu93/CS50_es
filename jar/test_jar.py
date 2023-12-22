import pytest
from jar import Jar


def test_init():
    jar = Jar(100, 50)
    assert jar.capacity == 100
    assert jar.size == 50

    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.deposit(25)


def test_withdraw():

    jar = Jar(4)
    jar.deposit(3)
    jar.withdraw(2)
    assert jar.size == 1

    jar2 = Jar(12, 11)
    with pytest.raises(ValueError):
        jar2.withdraw(50)