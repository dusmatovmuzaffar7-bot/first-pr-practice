from greet import greet, farewell, good_morning, bye


def test_greet_default():
    assert greet() == "Hello, World!"


def test_greet_with_name():
    assert greet("Alice") == "Hello, Alice!"


def test_farewell_default():
    assert farewell() == "Goodbye, World!"


def test_farewell_with_name():
    assert farewell("Alice") == "Goodbye, Alice!"


def test_good_morning_default():
    assert good_morning() == "Good morning, World!"


def test_good_morning_with_name():
    assert good_morning("Alice") == "Good morning, Alice!"


def test_bye_default():
    assert bye() == "Bye, World!"


def test_bye_with_name():
    assert bye("Alice") == "Bye, Alice!"
