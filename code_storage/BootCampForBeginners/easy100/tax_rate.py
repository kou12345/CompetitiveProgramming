def main():
    n = int(input())

    for i in range(1, n + 1):
        x = int(i * 1.08)
        if (x == n):
            print(i)
            return
    print(":(")

main()