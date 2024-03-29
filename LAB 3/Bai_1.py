n=int(input("nhập vào một số nguyên:"))

#cau a
S = 0
if n<=0:
    print("Vui lòng nhập lại!")
else:
    for i in range(1,n+1):
        S+=i
print("Biểu thức S1 = ",S)

#cau b
S = 0
if n<=0:
    print("Vui lòng nhập lại!")
else:
    for i in range(1,n+1):
        S+= 1/i
print("Biểu thức S2 = ",S)

#cau c
import math
S = 1
if n<=0:
    print("Vui lòng nhập lại!")
else:
    for i in range(1,n+1):
        S = S + 1/(math.sqrt(2*i))
print("Biểu thức S3 = ",S)

#cau d
sum = 0
if n<0:
    print("vui lòng nhập lại!")
else:
    for i in range(1,n+1):
        sum+= ((-1)**(i+1))/i
print("Biểu thức S4 = ",sum)
    

