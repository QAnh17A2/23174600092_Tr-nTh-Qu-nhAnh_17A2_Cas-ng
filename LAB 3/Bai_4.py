#hình 1
a = int(input("Nhập chiều cao của hình thoi (số lẻ): "))
for i in range(1, a // 2 + 2):
    print(" " * (a // 2 + 1 - i) + "*" * (2 * i - 1))

for i in range(a // 2, 0, -1):
    print(" " * (a // 2 + 1 - i) + "*" * (2 * i - 1))


#hình 2
a = int(input("Nhập chiều cao của cây thông: "))
for i in range(a):
    print(" " * (a - i - 1) + "*" * (2 * i + 1))

for i in range(3):
    print(" " * (a - 2) + "***")