# cau a
n = int(input("Nhập số lượng số Fibonacci muốn tạo: "))
fibonacci = [0, 1] if n > 1 else [0] if n == 1 else []

while len(fibonacci) < n:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print("Danh sách Fibonacci:", fibonacci)

# cau b
prime_numbers = [num for num in range(2, 100) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))]

print("Danh sách số nguyên tố nhỏ hơn 100:", prime_numbers)