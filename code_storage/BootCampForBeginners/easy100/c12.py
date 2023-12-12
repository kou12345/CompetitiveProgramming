# https://atcoder.jp/contests/abc160/tasks/abc160_c

k, n = map(int, input().split())
a = list(map(int, input().split()))

# 1番目とN番目の家の距離
# 湖の周り - (N番目 - 1番目)
longest = k - (a[-1] - a[0])

# longestで距離を一つすでに計算しているため、range(n-1)
for i in range(n - 1):
    if a[i + 1] - a[i] > longest:
        longest = a[i + 1] - a[i]

# 湖の周り - 最大距離
# 最大距離を通らないもの = 最短距離だから
print(k - longest)

"""
20 3
5 10 15

普通に1, 2, 3の順番で最短


20 3
0 5 15

2, 1, 3が最短

全探索？

0がminの時は二番にminの値で計算してみる
ダメだった

https://tamlog.hateblo.jp/entry/2021/07/20/011357

巡回セールスマン問題らしい
"""
