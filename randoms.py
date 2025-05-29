import random

number = [random.randint(1, 5) for _ in range(5)]
print("Números aleatórios:", number)

number2 = list(range(1, 6))
print("Lista fixa:", number2)

for j in number2:
    print("True" if j + 1 in number else "False")