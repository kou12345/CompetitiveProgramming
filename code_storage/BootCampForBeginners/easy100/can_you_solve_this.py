N, M, C = map(int, input().split())
B = list(map(int, input().split()))

count = 0 # 問題に正答するソースコードの個数

for i in range(N):
    A = list(map(int, input().split()))
    
    tmp = C
    for j in range(M):
        tmp += A[j] * B[j]
    
    if 0 < tmp:
        count += 1

print(count)