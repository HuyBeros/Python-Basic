#tổng ước của số nguyên dương n

#cách 1
# n = int(input("nhap vao so nguyen n: "))
# tong = 0
# for i in range(1, n+1):
#     if n%i == 0:
#         tong += i
# print("tong cac uoc cua n la: ", tong)
n = int(input("nhap vao so nguyen duong n: "))
if n%2==0:
    print("n la so chan")
else:
    print("n la so le")

if n%5==0 and n%3==0:
    print("n chia het cho 5 va 3")

if n%3==0 and n%7!=0:
    print("n chia het cho 3 va khong chia het cho 7")

if n>30 and n<50:
    print("n nam trong khoang tu 30 den 50")

r=n%10
if n<30 and (n%2==0 or n%3==0 or n%5==0):
    print("n nho hon 30 va chia het cho 2 hoac 3 hoac 5")

if n%10!=0 and (r==2 or r==3 or r==5 or r==7):
    print("n khong chia het cho 10 va co chu so cuoi la so nguyen to")

if n <=100 and n%23==0:
    print("n nho hon hoac bang 100 va chia het cho 23")

if n<10 and n>20:
    print("n nho hon 10 va lon hon 20")
