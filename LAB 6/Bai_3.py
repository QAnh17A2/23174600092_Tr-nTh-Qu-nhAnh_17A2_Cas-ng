day_so = input("Nhập 1 dãy số, cách nhau bởi dấu cách: ")
danh_sach = day_so.split()
so = [float(x) for x in danh_sach]

if len(so) > 0:
    min_number = max_number = so[0]
    for num in so:
        if num < min_number:
            min_number = num
        if num > max_number:
            max_number = num

    print(f"Số lớn nhất trong dãy là: {max_number}")
    print(f"Số nhỏ nhất trong dãy là: {min_number}")
else:
    print("Dãy số rỗng, không có số nào để xử lý.")