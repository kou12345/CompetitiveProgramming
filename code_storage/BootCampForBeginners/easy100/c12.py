# https://atcoder.jp/contests/abc160/tasks/abc160_c

k, n = map(int, input().split())
a = list(map(int, input().split()))

if a[0] == 0:
    print(abs(a[1] - max(a)))
else:
    print(abs(min(a) - max(a)))

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

"""
