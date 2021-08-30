input_data = list(map(int, input().split()))
plus_data = list(map(int, input().split()))

result_list = [0 for _ in range(len(input_data))]
for i in range(len(input_data)):
    multip = int(input_data[i]//plus_data[i])
    result_list[i] = multip

result = min(result_list)
for i in range(len(plus_data)):
    plus_data[i] *= result

print(*plus_data)