# B - Number Box

"""

配列の中から一番大きな値を見つける

進む方向を決める
隣接する上下左右斜めの中で最大値がある方向を選ぶ
最大値が複数ある場合は？
次の値の最大値で方向を決める

全探索する

最初に決めた方向にしか移動できない


"""

# 配列の行と列の長さ
# N = int(input())

# array = []

# for _ in range(N):
#     array.append(list(map(int, input())))

# print(array)


"""
ユーザー:kj9の解答
20220822
分からんから飛ばす
"""

def resolve():
    # 行と列の長さ
    N = int(input())

    # 入力を受け取り、配列を作成
    A = [list(map(int, list(input())))  for _ in range(N)]

    ans = 0

    for i in range(N):
        for j in range(N):

            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    # x:0 y:0 は自分を指すためcontinueで飛ばす 
                    if (di == 0 and dj == 0):
                        continue
                        
                    num = ""

                    for k in range(N):
                        i = (i + di) % N
                        j = (j + dj) % N

                        num += str(A[i][j])

                    ans = max(ans, int(num))

    print(ans)

resolve()