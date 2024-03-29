#a      
n = int(input("Nhập vào một số nguyên dương: "))
if n <= 0:
    print("Vui lòng nhập lại số: ")

sum_a = 0
for i in range(1, n + 1):
    sum_a += i
print("Tổng của dãy 1 + 2 + 3 + ... +", n, "là:", sum_a)