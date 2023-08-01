def main():
    H, W = map(int, input().split())

    if (H == 1 or W == 1):
        print(1)
        return

    output = -(-(H * W) // 2) # 切り上げ
    print(output)

main()
