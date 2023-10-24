import random

def generate_polynomial(k):
    coefficients = [random.randint(0, 100) for _ in range(k+1)]
    polynomial = ""
    for i in range(k+1):
        if coefficients[i] != 0:
            if i == 0:
                polynomial += str(coefficients[i])
            elif i == 1:
                polynomial += f" + {coefficients[i]}*x"
            else:
                polynomial += f" + {coefficients[i]}*x^{i}"
    return polynomial

k = int(input("Введите степень многочлена: "))
polynomial = generate_polynomial(k)
print("Многочлен:", polynomial)

filename = "polynomial.txt"
with open(filename, "w") as file:
    file.write(polynomial)

print(f"Многочлен записан в файл {filename}")
