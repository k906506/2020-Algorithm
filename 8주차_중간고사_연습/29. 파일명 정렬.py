import re

def file_name_sort(file_list):
    p = re.compile('(\\D+)(\\d+)')
    file_list.sort(key = lambda x : (p.match(x).group(1).lower(), int(p.match(x).group(2))))
    return file_list

num = int(input())
for i in range(num):
    file_list = []
    file_list = list(x.strip() for x in input().split(','))
    result = file_name_sort(file_list)
    print(*result)