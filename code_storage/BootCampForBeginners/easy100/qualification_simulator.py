n, a, b = map(int, input().split())
s = input()

passed = 0
b_count = 0

for i in range(n):
    # 国内の学生
    if s[i] == "a":
        if passed < a + b:
            print("Yes")
            passed += 1
        else:
            print("No")
    # 海外の学生
    elif s[i] == "b":
        b_count += 1
        if passed < a + b and b_count <= b:
            print("Yes")
            passed += 1
        else:
            print("No")
    else:
        print("No")
