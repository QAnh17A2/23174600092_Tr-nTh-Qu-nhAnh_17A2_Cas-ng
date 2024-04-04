#cau a
print("Các số nguyên tố nhỏ hơn 100 là:")
num = 2
while num < 100:
    la_so_nguyen_to = True
    uoc_so = 2
    while uoc_so * uoc_so <= num:
        if num % uoc_so == 0:
            la_so_nguyen_to = False
            break
        uoc_so += 1
    if la_so_nguyen_to:
        print(num, end=" ")
    num += 1

#cau b
print("Các số chính phương nhỏ hơn 100 là:")
num = 1
while num < 100:
    can_bac_hai = int(num ** 0.5)
    if can_bac_hai * can_bac_hai == num:
        print(num, end=" ")
    num += 1

#cau c
print("Các số Fibonacci nhỏ hơn 1000 là:")
a, b = 0, 1
while a < 1000:
    print(a, end=" ")
    a, b = b, a + b
    