so_nguyen = int(input("Nhập một số nguyên có ba chữ số: "))
if 100 <= so_nguyen <= 999:
    hang_tram = so_nguyen // 100
    hang_chuc = (so_nguyen % 100) // 10
    hang_don_vi = so_nguyen % 10

    print("Cách đọc số nguyên bằng Tiếng Anh là: ")

    # Hàng trăm
    if hang_tram == 1:
        print("One hundred", end=" ")
    elif hang_tram == 2:
        print("Two hundred", end=" ")
    elif hang_tram == 3:
        print("Three hundred", end=" ")
    elif hang_tram == 4:
        print("Four hundred", end=" ")
    elif hang_tram == 5:
        print("Five hundred", end=" ")
    elif hang_tram == 6:
        print("Six hundred", end=" ")
    elif hang_tram == 7:
        print("Seven hundred", end=" ")
    elif hang_tram == 8:
        print("Eight hundred", end=" ")
    elif hang_tram == 9:
        print("Nine hundred", end=" ")

    # Hàng chục
    if hang_chuc == 2:
        print("twenty", end=" ")
    elif hang_chuc == 3:
        print("thirty", end=" ")
    elif hang_chuc == 4:
        print("forty", end=" ")
    elif hang_chuc == 5:
        print("fifty", end=" ")
    elif hang_chuc == 6:
        print("sixty", end=" ")
    elif hang_chuc == 7:
        print("seventy", end=" ")
    elif hang_chuc == 8:
        print("eighty", end=" ")
    elif hang_chuc == 9:
        print("ninety", end=" ")

    # Hàng đơn vị
    if hang_don_vi == 1:
        print("one")
    elif hang_don_vi == 2:
        print("two")
    elif hang_don_vi == 3:
        print("three")
    elif hang_don_vi == 4:
        print("four")
    elif hang_don_vi == 5:
        print("five")
    elif hang_don_vi == 6:
        print("six")
    elif hang_don_vi == 7:
        print("seven")
    elif hang_don_vi == 8:
        print("eight")
    elif hang_don_vi == 9:
        print("nine")
