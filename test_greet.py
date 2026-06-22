from greet import greet, farewell, good_morning, bye, BYE_PHRASES


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
    result = bye()
    assert result.endswith(", World!")
    assert result.split(",")[0] in BYE_PHRASES


def test_bye_with_name():
    result = bye("Alice")
    assert result.endswith(", Alice!")
    assert result.split(",")[0] in BYE_PHRASES
