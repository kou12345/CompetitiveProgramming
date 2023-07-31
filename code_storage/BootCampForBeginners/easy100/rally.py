n = int(input())
x = list(map(int, input().split()))

min_x = min(x)
max_x = max(x)

sums = []

for p in range(min_x, max_x + 1):
    sum = 0
    for i in range(len(x)):
        sum += (x[i] - p) ** 2
    sums.append(sum)

print(min(sums))
