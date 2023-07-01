num_list = list(map(int, input().split()))

output = "Yes"

for i in range(1, len(num_list)):
    if num_list[i] < num_list[i - 1]:
        output = "No"
        break

for i in range(len(num_list)):
    if num_list[i] >= 100 and num_list[i] <= 675:
        continue
    else:
        output = "No"
        break

for i in range(len(num_list)):
    if num_list[i] % 25 != 0:
        output = "No"
        break

print(output)