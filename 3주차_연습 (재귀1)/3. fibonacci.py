input_data = int(input())
if input_data == 1:
    print(2)
elif input_data == 1:
    print(2)
else:
    rabbit = [0 for _ in range(input_data+1)]
    rabbit[0] = 2
    rabbit[1] = 2
    for j in range(2, input_data+1):
        rabbit[j] = rabbit[j-1]+(int)(rabbit[j-2]/2)
    print(rabbit[input_data-1])