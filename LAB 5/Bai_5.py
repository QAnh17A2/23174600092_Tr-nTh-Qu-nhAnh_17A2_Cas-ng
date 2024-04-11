chuoi1 = input("Nhập chuỗi ký tự thứ nhất: ")
chuoi2 = input("Nhập chuỗi ký tự thứ hai: ")
chuoi_tron = ''
do_dai_chuoi_ngan_nhat = min(len(chuoi1), len(chuoi2))

for i in range(do_dai_chuoi_ngan_nhat):
    chuoi_tron += chuoi1[i] + '-' + chuoi2[i] + '-'

chuoi_tron += chuoi1[do_dai_chuoi_ngan_nhat:] + '-' + chuoi2[do_dai_chuoi_ngan_nhat:]

chuoi_tron = chuoi_tron.rstrip('-')  

print("Chuỗi sau khi trộn:", chuoi_tron)