chuoi_ban_dau = input("Nhập chuỗi ban đầu:")
chuoi_moi = input("Nhập chuỗi mới:")

if len(chuoi_ban_dau) != len(chuoi_moi):
    print("Không thể thay đổi chuỗi!")
else:
    so_ky_tu_khac_nhau = 0
    for i in range(len(chuoi_ban_dau)):
        if chuoi_ban_dau[i] != chuoi_moi[i]:
            so_ky_tu_khac_nhau += 1
    if so_ky_tu_khac_nhau <= 1:
        print("Có thể thay đổi chuỗi ban đầu thành 1 chuỗi mới!")
    else:
        print("Không thể thay đổi chuỗi ban đầu thành 1 chuỗi mới!")