num = int(input())

def recursionStar(num):
    multip = num//3
    for i in range(multip):



        for i in range(num):
            for j in range(num):
                print("*", end = " ")