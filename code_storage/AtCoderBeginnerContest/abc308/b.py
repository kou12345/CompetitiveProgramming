n, m = map(int, input().split())

inputs = [list(input().split()) for _ in range(n)]

output = 0

c = inputs[0][:] # 皿の色

d = input[1][:]

p = inputs[2][:] # 値段

for d in inputs[1][:]:
    for c_idx in range(len(c)):
        if d == c[c_idx]:
            idx = m - c_idx
            print(p[idx])
            output += int(p[idx])

for i in range(n):
    for d in range

print(output)