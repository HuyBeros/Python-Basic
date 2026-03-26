a = [1, 2, 3, 4, 5]
k = a.reverse()
print(k)
b = int(input("Nhập vào một số nguyên: "))
c = int(input("Nhập vào một số nguyên: "))
a.insert(b, c)

# Loại bỏ tất cả phần tử chẵn trong danh sách (không sửa đổi khi đang lặp)
a = [x for x in a if x % 2 != 0]

print(a)
