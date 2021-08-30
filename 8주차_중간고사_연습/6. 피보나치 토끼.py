def find_rabbit(num):
    rabbit = [0]*num
    rabbit[0] = 2
    rabbit[1] = 2
    for i in range(2, num):
        rabbit[i] = rabbit[i-1] + int((rabbit[i-2]/2))
    return rabbit[num-1]

def main():
    print(find_rabbit(int(input())))

if __name__ == "__main__":
    main()