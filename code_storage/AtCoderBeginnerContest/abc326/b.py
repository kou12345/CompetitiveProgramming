n = input()

while True:
    if (int(n[0]) * int(n[1]) == int(n[2])):
        print(n)
        break
    else:
        n = str(int(n) + 1)
