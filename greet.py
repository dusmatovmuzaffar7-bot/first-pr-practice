import random


def greet(name="World"):
    return f"Hello, {name}!"


def farewell(name="World"):
    return f"Goodbye, {name}!"


def good_morning(name="World"):
    return f"Good morning, {name}!"


BYE_PHRASES = ["Bye", "See you", "Take care", "Farewell"]


def bye(name="World"):
    phrase = random.choice(BYE_PHRASES)
    return f"{phrase}, {name}!"


if __name__ == "__main__":
    print(greet())
    print(farewell())
    print(good_morning())
    print(bye())
