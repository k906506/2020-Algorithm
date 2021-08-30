input_data = int(input())
if input_data == 1:
    print(2)
elif input_data == 2:
    print(2)
else:
    rabbit = [0 for _ in range(input_data+1)]
    rabbit[0] = 2
    rabbit[1] = 2
    for i in range(2, input_data+1):
        rabbit[i] = rabbit[i-1]+(int)(rabbit[i-2]/2)
    print(rabbit[input_data-1])