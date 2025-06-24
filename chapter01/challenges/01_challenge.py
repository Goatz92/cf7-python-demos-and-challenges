str = "FACTORY"

for i in range(len(str)):
    print((str[i] * (i + 1)), end=" ")
    print()

for i in range(len(str)):
    print((str[i] * (i + 1)), end=("*" * (7 - i)))
    print()
