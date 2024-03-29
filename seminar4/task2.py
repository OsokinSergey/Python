def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

N = int(input("Введите натуральное число: "))
factors = prime_factors(N)
print("Простые множители числа", N, ":", factors)
