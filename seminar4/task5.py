def read_polynomial(filename):
    with open(filename, "r") as file:
        polynomial = file.read()
    return polynomial

def sum_polynomials(polynomial1, polynomial2):
    # Разбиваем строки многочленов на слагаемые
    terms1 = polynomial1.split(" + ")
    terms2 = polynomial2.split(" + ")

    # Создаем словари для хранения коэффициентов многочленов
    coefficients1 = {}
    coefficients2 = {}

    # Заполняем словари коэффициентами многочленов
    for term in terms1:
        if "*" in term:
            coefficient, power = term.split("*x^")
            coefficients1[int(power)] = int(coefficient)
        elif "*x" in term:
            coefficient, _ = term.split("*x")
            coefficients1[1] = int(coefficient)
        else:
            coefficients1[0] = int(term)

    for term in terms2:
        if "*" in term:
            coefficient, power = term.split("*x^")
            coefficients2[int(power)] = int(coefficient)
        elif "*x" in term:
            coefficient, _ = term.split("*x")
            coefficients2[1] = int(coefficient)
        else:
            coefficients2[0] = int(term)

    # Вычисляем сумму коэффициентов для каждой степени
    sum_coefficients = {}
    for power in coefficients1.keys():
        sum_coefficients[power] = coefficients1[power]
    for power in coefficients2.keys():
        if power in sum_coefficients:
            sum_coefficients[power] += coefficients2[power]
        else:
            sum_coefficients[power] = coefficients2[power]

    # Формируем строку суммы многочленов
    sum_polynomial = ""
    for power in sorted(sum_coefficients.keys(), reverse=True):
        coefficient = sum_coefficients[power]
        if power == 0:
            sum_polynomial += str(coefficient)
        elif power == 1:
            sum_polynomial += f" + {coefficient}*x"
        else:
            sum_polynomial += f" + {coefficient}*x^{power}"

    return sum_polynomial

filename1 = "polynomial1.txt"
filename2 = "polynomial2.txt"

polynomial1 = read_polynomial(filename1)
polynomial2 = read_polynomial(filename2)

sum_polynomial = sum_polynomials(polynomial1, polynomial2)

filename_sum = "sum_polynomial.txt"
with open(filename_sum, "w") as file:
    file.write(sum_polynomial)

print(f"Сумма многочленов записана в файл {filename_sum}")