# print("hello","world",sep="--")
# print("java","python","c++",end="-\n")

# #hello--world
# """hello"""
# a = 100
# print(type(a))

# b=3.1111128317
# print('%.2f' %b)

# a = float(input("nhap vao 1 so: "))
# print(a)

#cơ bản
# #bước 1 : nhập 
# s = input("nhap vao 3 so: ")
# #buoc 2 : tach cac so
# a = s.split()
# #buoc 3 : su dung map de ep cac phan tu trong list
# x,y,z = map(int,a)
# b = x + y + z
# print(b)

#nâng cao
x,y,z = map(int,input("nhap vao 3 so: ").split())
s  = x + y + z
print(s)
print(x,y,z)