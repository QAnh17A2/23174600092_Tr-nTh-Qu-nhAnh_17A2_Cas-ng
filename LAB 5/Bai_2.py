str1 = input("Nhập chuỗi ký tự thứ nhất: ")
str2 = input("Nhập chuỗi ký tự thứ hai: ")

do_dai_str1 = len(str1)
do_dai_str2 = len(str2)

chuoi_ngan_nhat = ''
do_dai_chuoi_ngan_nhat = min(do_dai_str1, do_dai_str2)

for i in range(do_dai_chuoi_ngan_nhat):
    if str1[i] == str2[i]:
        chuoi_ngan_nhat += str1[i]
    else:
        break

if chuoi_ngan_nhat:
    print("Chuỗi con chung ngắn nhất:", chuoi_ngan_nhat)
else:
    print("Không có chuỗi con chung nào.")
    