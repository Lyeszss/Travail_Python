a = int(input("Choisir Premier nombre"))
operation = (input("Chosir opération"))
b = int(input("Choisir Deuxième nombre"))
if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    if b != 0:
        print(a / b)
    else:
        print("Impossible de diviser par zéro")
