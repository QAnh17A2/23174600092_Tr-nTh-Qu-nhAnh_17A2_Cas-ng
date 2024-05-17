def sumPdivisors(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors)

n = 36
print(f"Tổng các ước số chính của {n} là: {sumPdivisors(n)}")