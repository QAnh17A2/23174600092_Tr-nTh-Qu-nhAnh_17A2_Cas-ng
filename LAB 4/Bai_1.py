#cau a:
total = 0
a = []
while total <= 1000:
    b = int(input("Nhập 1 số nguyên dương:"))
    if b > 0:
        total += b
        if b % 2 != 0:
            a.append(b)
print("Các số lẻ đã nhập:",a)

#cau b
total = 0
a = []
while total <= 1000:
    b = int(input("Nhập 1 số nguyên dương:"))
    if b > 0:
        total += b
        if b % 2 == 0:
            a.append(b)
print("Các số chẵn đã nhập:",a)

#cau c
total = 0
count = 0
while total <= 1000:
    a = int(input("Nhập 1 số nguyên dương:"))
    total += a
    count += 1
print("Số lượng số nguyên đã nhập là: ",count)