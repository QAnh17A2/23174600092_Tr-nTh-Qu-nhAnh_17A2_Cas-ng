chuoi = input("Nhập chuỗi có độ dài hơn 10 ký tự: ")

if len(chuoi) > 10:
    # a
    chuoi_a = chuoi[1:8]
    print("a, Chuỗi ký tự con từ vị trí thứ 2 đến vị trí thứ 8:", chuoi_a)
    # b
    chuoi_b = chuoi[4:9]
    print("b, Chuỗi ký tự con gồm 5 ký tự kể từ vị trí thứ 5:", chuoi_b)
    # c
    chuoi_c = chuoi[-3:]
    print("c, Chuỗi ký tự con từ cuối chuỗi gồm 3 ký tự:", chuoi_c)
    # d
    chuoi_d = chuoi.lower()
    print("d, Chuỗi sau khi chuyển đổi thành chữ thường:", chuoi_d)
    # e
    chuoi_e = chuoi.upper()
    print("e, Chuỗi sau khi chuyển đổi thành chữ hoa:", chuoi_e)
    # f
    chuoi_f = chuoi[::-1]
    print("f, Chuỗi sau khi đảo ngược:", chuoi_f)
else:
    print("Chuỗi không có độ dài hơn 10 ký tự.")