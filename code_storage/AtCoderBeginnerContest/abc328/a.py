n, x = map(int, input().split())
s = list(map(int, input().split()))

output = 0

for i in s:
    if i <= x:
        output += i

print(output)
