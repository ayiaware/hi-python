n = 12
k = 4

def factorial(x):
    factorial = 1
    if x >= 1:
        for i in range (1, int(x) + 1):
            factorial = factorial * i
    return factorial

combination = factorial(n) / (factorial((n-k)) * factorial(k))

print(combination)

