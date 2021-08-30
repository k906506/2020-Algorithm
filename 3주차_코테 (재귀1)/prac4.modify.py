def fact(n):
    if n <= 1:
        return 1
    else :
        return n*fact(n-1)

def catalan(n):
    return fact(2*n) // (fact(n)*fact(n+1))

input_list = list(map(int, input().split()))
l = int(input_list[0])
m = int(input_list[1])
n = int(input_list[2])
x = l + m + n
deno = fact(x)//(fact(l)*fact(m)*fact(n))
result = catalan(x)*deno
print(result)