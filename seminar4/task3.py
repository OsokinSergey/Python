def unique_elements(sequence):
    unique = []
    for element in sequence:
        if element not in unique:
            unique.append(element)
    return unique

sequence = input("Введите последовательность чисел через пробел: ").split()
unique_elements_list = unique_elements(sequence)
print("Список неповторяющихся элементов:", unique_elements_list)
