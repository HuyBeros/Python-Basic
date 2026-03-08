a,b = map(int, input("Nhập 2 số nguyên: ").split())
res1 = a//b * b
print(res1)
res2 = (a//b) * b + b
if a%b == 0:
    print(a)
else:
    print(res2)
