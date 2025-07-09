def add(a: int | float, b: int | float) -> int | float:
    return a + b


def add_multiple(*args: int | float) -> int | float:
    return sum(args)
