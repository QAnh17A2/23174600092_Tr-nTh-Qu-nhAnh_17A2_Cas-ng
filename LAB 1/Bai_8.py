import math
x,z=map(float,input("nhập hai số thực: ").split())
f=((((x**2)*math.sin(z))+(math.sqrt(abs(x))))/(math.log(z)+(math.e**(x-1))))+math.atan(x*z)
print("giá trị của biêu thức là: {:.2f}".format(x,z))
