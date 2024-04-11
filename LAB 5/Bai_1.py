so_thap_phan = int(input("Nhập 1 số nguyên dương là số thập phân: "))

if so_thap_phan < 0:
    print("Số đã nhập phải là số nguyên dương!")
else:
    if so_thap_phan == 0:
        print("Số nhị phân tương ứng: 0")
    else:
        chuoi_nhi_phan = ''
        while so_thap_phan > 0:
            chuoi_nhi_phan = str(so_thap_phan % 2) + chuoi_nhi_phan
            so_thap_phan //= 2
        print("Số nhị phân tương ứng:", chuoi_nhi_phan)