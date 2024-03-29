#a
a = 0
for num in range(2000, 4001):
    if num % 7 == 0 and num % 5 != 0:
        a += num

print("Tổng các số chia hết cho 7 nhưng không chia hết cho 5 trong khoảng từ 2000 đến 4000 là:", a)

#b
a = 0
for num in range(500, 1001):
    if num % 4 == 0 and num % 6 != 0:
        a += num

print("Tổng các số chia hết cho 4 nhưng không chia hết cho 6 trong khoảng từ 500 đến 1000 là:", a)