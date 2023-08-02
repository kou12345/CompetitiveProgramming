def main():
    a, b = input().split()

    num = int(a + b)

    for i in range(1, 1000):
        if i * i == num:
            print("Yes")
            return
        
    print("No")

main()
