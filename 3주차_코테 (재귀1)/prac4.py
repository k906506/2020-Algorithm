import math
def catalan(n):
    return math.factorial(2*n) // (math.factorial(n) * math.factorial(n+1))

l, m, n = map(int, input().split())
deno = math.factorial(l+m+n)//(math.factorial(l)*math.factorial(m)*math.factorial(n))
result = catalan(l+m+n)*deno
print(result)