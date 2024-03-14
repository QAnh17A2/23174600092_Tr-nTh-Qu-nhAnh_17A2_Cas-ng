a1,b1,c1,a2,b2,c2=map(float,input("nhập các hệ số: ").split())
x=((c1*b1)-(c2*b2))/((a1*b2)-(a2*b1))
y=((a1*c2)-(a2*c1))/((a1*b2)-(a2*b1))
print("giá trị của x là {:.2f}".format(x))
print("giá trị của y là {:.2f}".format(y))
                      