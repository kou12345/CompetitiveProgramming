def main():
    A = [list(map(int, input().split())) for _ in range(3)]
    N = int(input())

    punched = [[False]*3 for _ in range(3)] # 穴が開いたカード
    is_bingo = False

    for i in range(N):
        b = int(input())

        x, y = find_value_in_2d_array(A, b)
        if x is not None and y is not None:
            punched[x][y] = True

    # ビンゴか確認する
    # 縦のビンゴになっているか
    for i in range(3):
        if punched[0][i] and punched[1][i] and punched[2][i]:
            is_bingo = True
    
    # 横のビンゴになっているか
    for i in range(3):
        if punched[i][0] and punched[i][1] and punched[i][2]:
            is_bingo = True
            
    # 斜めのビンゴになっているか
    if punched[0][0] and punched[1][1] and punched[2][2]:
        is_bingo = True

    if punched[0][2] and punched[1][1] and punched[2][0]:
        is_bingo = True
    
    if is_bingo:
        print("Yes")
    else:
        print("No")

def find_value_in_2d_array(arr, target_value):
    for i, row in enumerate(arr):
        for j, value in enumerate(row):
            if value == target_value:
                return i, j
    return None, None

main()
