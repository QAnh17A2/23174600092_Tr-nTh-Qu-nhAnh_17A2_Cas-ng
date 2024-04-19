#bai 6.1
m = int(input("Nhập số hàng của ma trận: "))
n = int(input("Nhập số cột của ma trận: "))

matran = []
print("Nhập các phần tử của ma trận:")
for i in range(m):
    row = []
    for j in range(n):
        yeu_to = int(input(f"Phần tử [{i+1}][{j+1}]: "))
        row.append(yeu_to)
    matran.append(row)

tong_matran = 0
for row in matran:
    tong_matran += sum(row)

print("Tổng của các phần tử trong ma trận là:", tong_matran)

print("Nhập ma trận thứ hai:")
matran2 = []
for i in range(m):
    row = []
    for j in range(n):
        yeu_to = int(input(f"Phần tử [{i+1}][{j+1}]: "))
        row.append(yeu_to)
    matran2.append(row)

sp_matran = []
if len(matran[0]) == len(matran2):
    for i in range(m):
        row = []
        for j in range(len(matran2[0])):
            yeu_to = 0
            for k in range(len(matran2)):
                yeu_to += matran[i][k] * matran[k][j]
            row.append(yeu_to)
        sp_matran.append(row)
    print("Tích của hai ma trận là:")
    for row in sp_matran:
        print(row)
else:
    print("Hai ma trận không thể nhân với nhau vì số cột của ma trận thứ nhất không bằng số hàng của ma trận thứ hai.")

chuyendoi_matran = [[matran[j][i] for j in range(m)] for i in range(n)]
print("Ma trận chuyển vị của ma trận ban đầu là:")
for row in chuyendoi_matran:
    print(row)





#bai 6.2
n = int(input("Nhập kích thước của ma trận vuông: "))

print("Nhập các phần tử của ma trận vuông:")
matran = []
for i in range(n):
    row = []
    for j in range(n):
        yeu_to = float(input(f"Phần tử [{i+1}][{j+1}]: "))
        row.append(yeu_to)
    matran.append(row)

dinh_thuc = matran[0][0] * matran[1][1] - matran[0][1] * matran[1][0]
if dinh_thuc == 0:
    print("Ma trận này không có ma trận nghịch đảo vì định thức bằng 0!")
else:
    nghichdao_matran = [[matran[1][1] / dinh_thuc, -matran[0][1] / dinh_thuc],
                      [-matran[1][0] / dinh_thuc, matran[0][0] / dinh_thuc]]
    print("Ma trận nghịch đảo của ma trận đã nhập là:")
    for row in nghichdao_matran:
        print(row)

doi_xung = True
for i in range(n):
    for j in range(i + 1, n):
        if matran[i][j] != matran[j][i]:
            doi_xung = False
            break
    if not doi_xung:
        break

if doi_xung:
    print("Ma trận đã nhập là ma trận đối xứng.")
else:
    print("Ma trận đã nhập không phải là ma trận đối xứng.")