#Cho 4 số x,y,z,t. Nhập vào 4 số này từ bàn phím, In ra 3 dòng 1 lần lượt 4 số Y,Z,X,T, mỗi số cách nhau
#1 dấu phẩy, dòng 2 in ra tổng 4 số dòng 3 in ra giá trị của biểu thức x -y + z * t và giá trị của tổng 4 số có thể tràn dữ liệu kiểu int

x,y,z,t = map(int, input("Nhap vao 4 so nguyen: ").split())

print(y,z,x,t,sep=",")
print(x+y+z+t)
print(x-y+(z*t))
