day_so = input("Nhập dãy số, cách nhau bởi dấu cách: ")
danh_sach = day_so.split()
so = [int(x) for x in danh_sach]

is_arithmetic_progression = True
difference = so[1] - so[0]
for i in range(2, len(so)):
    if so[i] - so[i - 1] != difference:
        is_arithmetic_progression = False
        break

if is_arithmetic_progression:
    print("Dãy số này tạo thành cấp số cộng.")
    print("Dãy số:", so)
else:
    print("Dãy số này không tạo thành cấp số cộng.")