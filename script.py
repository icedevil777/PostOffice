from itertools import groupby

L = []
for i in range(3088):
    i = str(i + 2345)
    for j in range(4):
        if int(i[j]) > 5 or int(i[j]) < 2:
            break
        else:
            if j == 3 and int(i[0]) + int(i[1]) + int(i[2]) + int(i[3]) == 14 \
                    and int(i[0]) * int(i[1]) * int(i[2]) * int(i[3]) == 120:
                k = [el for el, _ in groupby(i)]
                if len(k) == 4:
                    L.append(int(''.join(k)))

print(L)
