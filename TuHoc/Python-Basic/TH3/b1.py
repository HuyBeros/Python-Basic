import myvecto
a = []
a = myvecto.vecinput(5)
print("Tổng các phần tử trong vector a là:", myvecto.vecsum(a))
print("Vector a sau khi chèn phần tử mới:", myvecto.vecinsert(a))
b = []
b = myvecto.vecinput(5)
print("Tổng các phần tử trong vector b là:", myvecto.vecsum(b))
print("Tổng hai vector a và b là:", myvecto.vecadd(a, b))