def calculate_pi(d):
    pi = 0
    i = 0
    while True:
        denominator = 2 * i + 1
        if i % 2 == 0:
            pi += 4 / denominator
        else:
            pi -= 4 / denominator
        i += 1
        if abs(4 / denominator) < d:
            break
    return pi

d = 0.001
pi = calculate_pi(d)
print(pi)
