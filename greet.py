def greet(name="World"):
    return f"Hello, {name}!"


def farewell(name="World"):
    return f"Goodbye, {name}!"


def good_morning(name="World"):
    return f"Good morning, {name}!"


def bye(name="World"):
    return f"Bye, {name}!"


if __name__ == "__main__":
    print(greet())
    print(farewell())
    print(good_morning())
    print(bye())
