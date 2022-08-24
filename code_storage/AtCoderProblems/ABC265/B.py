# B - Explore

"""

N: 部屋の数
M: ボーナス部屋の数
T: 待ち時間
A: 消費する時間
X: ボーナス部屋の場所
Y: 増加する待ち時間

持ち時間が 0 以下になるような移動は行うことができません。
最初は部屋 1 にいる

"""

# 入力を受け取る


N, M, T = map(int, input().split())
A = list(map(int, input().split()))
# M の数入力を受け取る
bonus = [0]*N

# X Y の入力を受け取る
for _ in range(M):
    X, Y = list(map(int, input().split()))
    # print(f"X:{X}")
    # print(f"Y:{Y}")
    bonus[X - 1] = Y

# print(bonus)

# 処理
# N 回（部屋の数）ループする
# もし次の部屋に移動できるなら
    # T - A 待ち時間から消費時間を引く
    # もしその部屋がボーナス部屋なら
        # T + Y 待ち時間にボーナス時間を足す
# そうでない場合は、フラグを false にして処理を終了する（ループを抜ける、break）
# もしフラグが true なら
    # "Yes" と出力
# そうでない場合
    # "No" と出力

success = True

# N = 4 T = 10
for i in range(1, N - 1):
    if T > A[i - 1]:
        T -= A[i]
        T += bonus[i]
        # print(f"T:{T}")
    else:
        success = False
        break

if success:
    print("Yes")
else:
    print("No")


# 詰み
# 