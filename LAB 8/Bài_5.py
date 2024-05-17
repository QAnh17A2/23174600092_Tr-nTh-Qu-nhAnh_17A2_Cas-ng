def sumPdivisors(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors)

def is_amicable(a, b):
    return sumPdivisors(a) == b and sumPdivisors(b) == a

a = 220
b = 284

if is_amicable(a, b):
    print(f"{a} và {b} là cặp số amicable.")
else:
    print(f"{a} và {b} không phải là cặp số amicable.")