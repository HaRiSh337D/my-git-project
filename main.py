def add(a, b):
    return a + b

def subtract(a, b):
    return a - b



def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

if __name__ == "__main__":
    x = 10
    y = 5

    print(f"{x} + {y} = {add(x, y)}")
    print(f"{x} - {y} = {subtract(x, y)}")
    print(f"{x} / {y} = {divide(x, y)}")
