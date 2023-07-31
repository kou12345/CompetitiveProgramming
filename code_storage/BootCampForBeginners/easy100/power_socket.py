a, b = map(int, input().split())
# 切り上げ
count = -(-(b - 1) // (a - 1))

print(count)