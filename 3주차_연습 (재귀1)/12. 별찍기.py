def star(n, num, old_nlst):
    
    # 첫줄의 별갯수는 항상 n과 같으므로 같아지면 리턴
    if len(old_nlst[0]) == num:
        return old_nlst
    
    # n이 3일때는 그냥 리스트 리턴
    if n == 3:

        return old_nlst

    else:

        old_nlst = old_nlst * 3

        old_nlst = [x * 3 for x in old_nlst]

        for i in range(len(old_nlst)):

            if i >= int(n/3) and i < int(n/3)*2:

                index_s = int(n/3)

                index_e = int(n/3)*2

                newstring = ""

                for alp in range(n):

                    if alp >= index_s and alp < index_e:

                        newstring += " "

                    else:

                        newstring += old_nlst[i][alp]

                old_nlst[i] = newstring

    return star(n*3, num, old_nlst)

num = int(input())

old_nlst = ["***","* *","***"]

a = star(9, num, old_nlst)

for i in a:
    print(i)