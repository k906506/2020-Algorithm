num = int(input())

def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num*factorial(num-1)

result = factorial(num)
print(result)