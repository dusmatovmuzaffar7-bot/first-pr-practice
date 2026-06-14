from greet import greet, farewell


def test_greet_default():
    assert greet() == "Hello, World!"


def test_greet_with_name():
    assert greet("Alice") == "Hello, Alice!"


def test_farewell_default():
    assert farewell() == "Goodbye, World!"


def test_farewell_with_name():
    assert farewell("Alice") == "Goodbye, Alice!"
