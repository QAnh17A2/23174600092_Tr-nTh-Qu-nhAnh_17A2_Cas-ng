chuoi_ky_tu = input("Nhập chuỗi ký tự: ")
chuoi_so = ''.join(ky_tu for ky_tu in chuoi_ky_tu if ky_tu.isdigit())

if chuoi_so:
    so_nguyen = int(chuoi_so)
    if so_nguyen > 1:
        for i in range(2, so_nguyen):
            if (so_nguyen % i) == 0:
                print(f"Chuỗi '{chuoi_so}' không phải là số nguyên tố.")
                break
        else:
            print(f"Chuỗi '{chuoi_so}' là số nguyên tố.")
    else:
        print(f"Chuỗi '{chuoi_so}' không phải là số nguyên tố.")
else:
    print("Không có số nào trong chuỗi.")