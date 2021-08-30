import re
point = []
score = [0, 0, 0]

point = input()

pattern = '(\\d+)([SDT])([*#]?)'
p = re.compile(pattern)
m = p.findall(point)

for i in range(3):
    if m[i][1] == 'S':
        score[i] = int(m[i][0])
    elif m[i][1] == 'D':
        score[i] = int(m[i][0])**2
    elif m[i][1] == 'T':
        score[i] = int(m[i][0])**3

for i in range(3):
    if m[i][2] == '*':
        if i < 2:
            score[i] = score[i]*2
            score[i+1] = score[i+1]*2
        else:
            score[i] = score[i]*2
    elif m[i][2] == '#':
            score[i] = score[i]*(-1)

result = 0
for i in range(3):
    result += score[i]
print(result)
