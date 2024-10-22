# Function with Return Statement


def add(a: int, b: int, c: int) -> int:
    total = a + b + c
    return total


def sub(a, b, c) -> None:
    total = a - b - c
    print(total)


x = add(5, 7, 100)
print(x)
# # print(add(1, 2, 3))
y = sub(4, 5, 6)
print(y)
