n = int(input("Nhập số lượng phần tử của mảng: "))
arr = []

print("Nhập các phần tử của mảng: ")
for i in range(n):
    num = int(input(f"Phần tử thứ {i + 1}: "))
    arr.append(num)

tong_chan = 0
tong_le = 0
for num in arr:
    if num % 2 == 0:
        tong_chan += num
    else:
        tong_le += num

print(f"Tổng các số chẵn trong mảng là: {tong_chan}")
print(f"Tổng các số lẻ trong mảng là: {tong_le}")