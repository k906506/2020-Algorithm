n, m = map(int, input().split())
x_th = int(input())

if n%2 == 0:    #짝수
    x = 1
    i = 0
    half = int(n/2)
    string_list = ["a"]*half
    copy_list = []
    while x < x_th:
        x *= m
        i += 1
    ### 첫번째 문자
    if x_th%m == 0:
        string_list[0] = chr(96+m)
    else:
        string_list[0] = chr(96+(x_th%m))
    ### 이후 나머지 문자
    y = 1
    for j in range(1,i):
        for k in range(1,j+1):
            y *= m
        string_list[j] = chr(97+((x_th//y)%m))
        y = 1
    copy_list = string_list.copy()
    copy_list.reverse()
    for i in range(half):
        print(copy_list[i], end = "")
    for i in range(half):
        print(string_list[i], end = "")
else:       #홀수
    x = 1
    i = 0
    half = int(n/2)+1
    string_list = ["a"]*half
    copy_list = []
    while x < x_th:
        x *= m
        i += 1
    ### 첫번째 문자
    if x_th%m == 0:
        string_list[0] = chr(96+m)
    else:
        string_list[0] = chr(96+(x_th%m))
    ### 이후 나머지 문자
    y = 1
    for j in range(1,i):
        for k in range(1,j+1):
            y *= m
        string_list[j] = chr(97+((x_th//y)%m))
        y = 1
    copy_list = string_list.copy()
    copy_list.reverse()
    for i in range(half-1):
        print(copy_list[i], end = "")
    for i in range(half):
        print(string_list[i], end = "")
