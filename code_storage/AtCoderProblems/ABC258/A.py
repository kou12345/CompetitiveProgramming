# A - When

import math

# 入力を受け取り、intにする
K = int(input())

HH = 21 # 時
MM = "" # 分

h = m = 0

# 時間と分の値を決める
# Kが60以上ならHHを変更する　HHの値が1増える
if K >= 60:
    # h = math.floor(K / 60)
    h = 1
    m = K % 60
# Kが60未満
else:
    m = K % 60

HH += h
MM = m

# h m が一桁の場合は先頭に0を足す
if len(str(HH)) == 1:
    # 先頭に0を足す
    HH = "0" + HH

if len(str(MM)) == 1:
    # 先頭に0を足す
    MM = "0" + str(MM)

print(f"{HH}:{MM}")