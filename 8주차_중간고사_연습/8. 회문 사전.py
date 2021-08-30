n, m = map(int, input().split())
x = int(input()) - 1

def recu_builer(value, m):
    if value == 0:
        return []
    arr = recu_builer(int(value/m), m)
    arr.append(value%m)
    return arr

ret = recu_builer(x, m)
num_of_a = int(n/2) + n%2 - len(ret)

for i in range(num_of_a):
    print("a", end = "")
for i in ret:
    print(chr(i+97), end = "")

ret.reverse()

for i in ret[n%2:]:
    print(chr(i+97), end = "")
for i in range(num_of_a):
    print("a", end = "")