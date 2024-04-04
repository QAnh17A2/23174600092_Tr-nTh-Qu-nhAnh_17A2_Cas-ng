while True:
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))

    print("Kết quả các phép tính:")
    print("Tổng:", a + b)
    print("Hiệu:", a - b)
    print("Tích:", a * b)
    if b != 0:
        print("Thương:", a / b)
    else:
        print("Không thể chia cho số 0")
    print("Lũy thừa:", a ** b)
    if a >= 0:
        print("Căn bậc hai của số thứ nhất:", a ** 0.5)
    else:
        print("Không thể tính căn bậc hai của số âm")

    tiep_tuc = input("Bạn có muốn tiếp tục không? (có/không): ")
    if tiep_tuc.lower() != "có":
        break