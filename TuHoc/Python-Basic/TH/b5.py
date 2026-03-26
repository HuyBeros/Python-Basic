n = int(input("Nhập vào số nguyên n: "))
a = [int(input(f"Nhập vào phần tử thứ {i+1}: ")) for i in range(n)]
a.sort()
print(a)
