num = int(input("Nhập vào một số nguyên: "))
so_chu_so = 0

while num != 0:
    num //= 10
    so_chu_so += 1

print("Số chữ số của số nguyên là:", so_chu_so)