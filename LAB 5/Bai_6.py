chuoi = input("Nhập chuỗi từ bàn phím: ")
ky_tu_dac_biet = {}
tong_so_ky_tu_dac_biet = 0

for ky_tu in chuoi:
    if not ky_tu.isalnum():
        ky_tu_dac_biet[ky_tu] = ky_tu_dac_biet.get(ky_tu, 0) + 1
        tong_so_ky_tu_dac_biet += 1

for ky_tu, so_lan_xuat_hien in ky_tu_dac_biet.items():
    print(f"Số lần xuất hiện của ký tự '{ky_tu}': {so_lan_xuat_hien}")

if len(chuoi) > 0:
    for ky_tu, so_lan_xuat_hien in ky_tu_dac_biet.items():
        ty_le = (so_lan_xuat_hien / len(chuoi)) * 100
        print(f"Tỷ lệ phần trăm của ký tự '{ky_tu}': {ty_le:.2f}%")
else:
    print("Chuỗi không có ký tự nào!")

print("Tổng số ký tự đặc biệt trong chuỗi là: ", tong_so_ky_tu_dac_biet)