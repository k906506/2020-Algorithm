l, m, n = map(int, input().split())
sum_brackets = l+m+n

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num*factorial(num-1)

def bracket_case(bracket, openb, closeb):
    tmp = 0
    if openb == closeb == 0:
        return 1
    if openb > 0:
        tmp += bracket_case(bracket + "(", openb-1, closeb+1)
    if closeb > 0:
        tmp += bracket_case(bracket + ")", openb, closeb-1)
    return tmp

def bracket_position(a,b,c, all):
    return int(factorial(all)/factorial(a)/factorial(b)/factorial(c))

print(bracket_case("", sum_brackets, 0) * bracket_position(l,m,n, sum_brackets))