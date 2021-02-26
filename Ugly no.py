# 15
# 0 2 3 4 5 6 8 9 10 12 15 16 18 20 24


def ugly(n):
    u = [0]
    i2, i3, i5 = 0, 0, 0
    nm2, nm3, nm5 = 2, 3, 5
    for i in range(1, n):
        u.append(min(nm2, nm3, nm5))
        if u[i] == nm2:
            i2 += 1
            nm2 = u[i2]*2
        if u[i] == nm3:
            i3 += 1
            nm3 = u[i3]*3
        if u[i] == nm5:
            i5 += 1
            nm5 = u[i5]*5

    return u



n = int(input())
print(' '.join(str(i) for i in ugly(n)))   # print(*ugly(n))