x, y, z = map(int, input().split())
num = int(input())
result_list = []
z = max(x, y, z)
if x >= y:
    temp = x
    x = y
    y = temp

check = 0
for i in range(0, 31):
    for j in range(0, 31):
        for k in range(0, 31):
            if x*i + y*j + z*k == num:
                result_list.append(i+j+k)
                check += 1
                break

if check != 0:
    print(min(result_list))
else:
    print(-1)