def find_number(input_dict, target):
    for i in input_dict.keys():
        for j in input_dict.keys():
            print(i.values())
            if i.values()*j.values() == target:
                print(i.values + " " + j.values)
                print(j.values + " " + i.values)

def main():
    target = int(input())
    input_value= input().strip().split()
    input_key = []
    for i in range(len(input_value)):
        input_key.append(str(i))
    input_dict = dict(zip(input_key, input_value))
    print(input_dict)
    find_number(input_dict, target)

if __name__ == "__main__":
    main()