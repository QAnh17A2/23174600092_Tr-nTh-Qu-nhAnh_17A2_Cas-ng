a,b=map(float,input("nhập các số đo : ").split())
import math
# diện tích xung quanh
c=math.sqrt(((a/2)**2)+(b**2))
S_xq=4*(1/2)*c*a
# diện tích toàn phần
S_tp=S_xq+(a**2)
# thể tích 
V=(1/2)*(a**2)*b
print("diện tích xung quanh của hình chóp là: {:.2f}".format(S_xq))
print("diện tích toàn phần của hình chóp là:{:.2f}".format(S_tp))
print("thể tích của hình chóp là: {:.2f}".format(V))
