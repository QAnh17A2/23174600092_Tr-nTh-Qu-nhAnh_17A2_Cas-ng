N = int(input("Nhập vào số nguyên N: "))

quynh_anh = [{x: x**3} for x in range(1, N+1)]

for qa in quynh_anh:
    print(qa)