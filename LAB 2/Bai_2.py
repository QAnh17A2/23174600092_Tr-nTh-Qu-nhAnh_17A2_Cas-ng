So_nguyen = int(input("Nhập một số nguyên: "))

if So_nguyen >= 1000:
    so_hang_nghin = (So_nguyen // 1000) % 10
    print("Chữ số hàng nghìn của số đã nhập là: ", so_hang_nghin)
else:
    print("0")