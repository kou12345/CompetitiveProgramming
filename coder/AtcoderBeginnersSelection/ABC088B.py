N = input()

A = []
A = [int(x) for x in input().split()]

# A を降順にする
A.sort(reverse=True)

Alice = 0
Bob = 0

# 交互に A の値を取得し、Alice or Bob に足していく
for i in range(len(A)):
    if i == 0 or i % 2 == 0:
        Alice += A[i]
    else:
        Bob += A[i]

print(Alice - Bob)
