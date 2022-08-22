# A - Apple

import math

"""

X円を払うとリンゴを1個手に入れる
Y円を払うとリンゴを3個手に入れる

ちょうどN個手に入れるには最低何円？

リンゴ一個当たりの値段がXの方が安いならXを個数分買う
そうでなければ
N / 3 個Yを買う
N / 3 の余り分Xを買う


"""

X, Y, N = map(int, input().split())
ans = 0

if X < math.floor(Y / 3):
    # Xの方が安い
    ans = X * N
else:
    buy_x = X * math.floor(N % 3)
    # print(buy_x)
    buy_y = Y * math.floor(N / 3)
    # print(buy_y)
    ans = buy_x + buy_y

print(ans)
