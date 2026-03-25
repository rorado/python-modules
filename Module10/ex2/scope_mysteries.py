count = 2
def test():
    x = 1
    def inner():
        nonlocal x
        x += 1
        return x
    return inner

x = test()
print(x())
print(x())


