n = int(input("Nhập số lượng phần tử của mảng: "))
arr = []

print("Nhập các phần tử của mảng:")
for i in range(n):
    num = int(input(f"Phần tử thứ {i + 1}: "))
    arr.append(num)

print("Các số nguyên tố trong mảng là:")
for num in arr:
    if num > 1:
        nguyen_to = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                nguyen_to = False
                break
        if nguyen_to:
            print(num)

print("Các số hoàn hảo trong mảng là:")
for num in arr:
    hoan_hao = 0
    for i in range(1, num):
        if num % i == 0:
            hoan_hao += i
    if hoan_hao == num:
        print(num)