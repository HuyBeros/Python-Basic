def vecinput(n):
    v = []
    for i in range(n):
        x = int(input(f"Nhap phan tu thu {i + 1}: "))
        v.append(x)
    return v


def vecsum(a):
    return sum(a)


def vecinsert(a):
    k = int(input("Nhap vao vi tri can chen: "))
    n = int(input("Nhap vao so can chen: "))
    a.insert(k, n)
    return a


def vecadd(a, b):
    if len(a) != len(b):
        print("Hai vector phai co cung so phan tu.")
        return None
    return [a[i] + b[i] for i in range(len(a))]


def list_to_matrix(a, n, m):
    if len(a) != n * m:
        print("Khong the tao ma tran vi so phan tu khong phu hop.")
        return []

    x = []
    idx = 0
    for i in range(n):
        row = []
        for j in range(m):
            row.append(a[idx])
            idx += 1
        x.append(row)
    return x

def merge_list(a,b):
    v = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        v.append(a[i])
        v.append(b[j])
        i += 1
        j+=1
    
    while i < len(a) :
        v.append(a[i])
        i += 1

    while j < len(b) :
        v.append(b[j])
        j += 1

    return v