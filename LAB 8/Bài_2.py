from math import factorial

def hoan_vi(n, r):
    if n < 0 or r < 0 or r > n:
        return "Giá trị không hợp lệ"
    return factorial(n) // factorial(n - r)

def to_hop(n, r):
    if n < 0 or r < 0 or r > n:
        return "Giá trị không hợp lệ"
    return hoan_vi(n, r) // factorial(r)

# Ví dụ sử dụng
n = 5
r = 3

print(f"Số hoán vị của {n} phần tử lấy {r} phần tử mỗi lần là: P({n}, {r}) = {hoan_vi(n, r)}")
print(f"Số tổ hợp của {n} phần tử lấy {r} phần tử mỗi lần là: C({n}, {r}) = {to_hop(n, r)}")