N = int(input())

ans = -1
max_count = -1

for i in range(1, N + 1):
    count = 0
    num = i
    while num % 2 == 0:
        num /= 2
        count += 1
    if max_count < count:
        max_count = count
        ans = i

print(ans)
