# ABC085C - Otoshidama

N, Y = map(int, input().split())

# f = True

# for i in range(N):
#     for j in range(N - i):
#         for k in range(N - i - j):
#             if Y == 10000 * i + 5000 * j + 1000 * k:
#                 print(f"{i} {j} {k}")
#                 f = False
#                 break
#         else:
#             continue
#         break
#     else:
#         continue
#     break

# if f:
#     print("-1 -1 -1")

# 上記のコードは計算量が多くなり、ダメ

K10 = K5 = K = -1

for i in range(N + 1): # なぜ N + 1 をするのか
    for j in range(N - i + 1):
        k = N - i - j
        if i * 10000 + j * 5000 + k * 1000 == Y:
            K10 = i
            K5 = j
            K = k
            break

print(K10, K5, K)
