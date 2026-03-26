
a = [4,5,6,7,8]
print(min(a))
print(max(a))

for i in range(5):
    if a[i] % 2 == 0:
        print(i)
        break
if 3 in a:
    print("Có số 3 trong a")
else:
    print("Không có số 3 trong a")
