N = int(input())
S = input()

has_a = False
has_b = False
has_c = False

count = 0

for i in range(N):
    if not has_a:
        has_a = "A" in S[i]
    if not has_b:
        has_b = "B" in S[i]
    if not has_c:
        has_c = "C" in S[i]
    if has_a and has_b and has_c:
        print(i + 1)
        break
