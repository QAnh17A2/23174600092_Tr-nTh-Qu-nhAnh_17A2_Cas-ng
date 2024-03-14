import math
a1,a2=map(int,input("nhập các tọa độ của vecto a: ").split())
b1,b2=map(int,input("nhập các tọa độ của vecto b: ").split())
#1.
phep_cong=(a1+b1),(a2+b2)
phep_tru=(abs(a1-b1)),(abs(a2-b2))
print("tổng của hai vecto là: ",phep_cong)
print("hiệu của hai vecto là: ",phep_tru)
#2.
do_dai_vecto_a=math.sqrt((a1**2)+(a2**2))
do_dai_vecto_b=math.sqrt((b1**2)+(b2**2))
print("độ dài của vecto a là: ",do_dai_vecto_a)
print("độ dài của vecto b là: ",do_dai_vecto_b)
#3.
cos=((a1*a2)+(b1*b2))/((math.sqrt((a1**2)+(b1**2)))*(math.sqrt((a2**2)+(b2**2))))
print("góc giữa hai vecto của a và b là: {:.2f} ".format(cos))