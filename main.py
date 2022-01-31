from math import sqrt
from itertools import groupby

# Initial data
point_1 = [0, 2]  # Post office
point_2 = [2, 5]  # Griboedova street
point_3 = [5, 2]  # Backer street
point_4 = [6, 6]  # Bolshaya Sadovaya street
point_5 = [8, 3]  # Evergreen street
# Create lists in list
P = [point_1, point_2, point_3, point_4, point_5, point_1]

rang = lambda x0, y0, x1, y1: sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
"""Calculate one step"""


def gen():
    """Generate and return all possible routes (My algorithm)"""
    L = []
    for i in range(3088):
        i = str(i + 2345)
        for j in range(4):
            if int(i[j]) > 5 or int(i[j]) < 2:
                break
            else:
                if j == 3 and int(i[0]) + int(i[1]) + int(i[2]) + \
                        int(i[3]) == 14 and int(i[0]) * int(i[1]) * \
                        int(i[2]) * int(i[3]) == 120:
                    k = [el for el, _ in groupby(str(i))]
                    if len(k) == 4:
                        L.append(k)

    for i in range(len(L)):
        for j in range(len(L[0])):
            L[i][j] = int(L[i][j])
    return L


sum1 = []
S = []
R = []
L = gen()
for i in range(len(L)):
    P = [point_1, P[L[i][0] - 1], P[L[i][1] - 1],
         P[L[i][2] - 1], P[L[i][3] - 1], point_1]
    for j in range(5):
        R.append(rang(P[j][0], P[j][1], P[j + 1][0], P[j + 1][1]))

sum1 = []

for i in range(0, 120, 5):
    sum1.append(R[i] + R[i + 1] + R[i + 2] + R[i + 3] + R[i + 4])

short_route = min(sum1)
number_short_route = sum1.index(short_route)
P = [point_1, point_3, point_2, point_5, point_4, point_1]

C = 0
P = [point_1, point_3, point_5, point_4, point_2, point_1]
for i in range(5):
    C = C + rang(P[i][0], P[i][1], P[i + 1][0], P[i + 1][1])
    print(f"{P[i]} -> {P[i + 1]} = {C} м ", end='')

print(f"\nThere are {sum1.count(short_route)} shortest route,"
      f" their length = {short_route} m.")
