# https://atcoder.jp/contests/agc014/tasks/agc014_a

a, b, c = map(int, input().split())

# クッキーを交換した回数
count = 0

# 全て同じ数字且つ偶数の場合は、break
if (a == b == c) and (a % 2 == 0):
    count = -1
else:
    while True:
        # 全てが2で割り切れる時
        if (a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0):
            tmp_a = a / 2
            tmp_b = b / 2
            tmp_c = c / 2

            a = tmp_b + tmp_c
            b = tmp_a + tmp_c
            c = tmp_a + tmp_b

            count += 1
        else:
            break

if count == 0:
    print(-1)
else:
    print(count)

"""
半分に分けて、二人に渡す。
このとき、自分のクッキーは0枚になっている

無限に続く場合はどういう場合？

"""
