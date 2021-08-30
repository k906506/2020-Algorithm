def find_min(people, time):
    min_time = 1
    max_time = people * max(time)

    while min_time <= max_time:
        mid = (max_time + min_time)//2
        total_time = 0
        for i in time:
            total_time += mid//i
            if total_time >= people:  #시간이 남는다. 
                result = mid
                max_time = mid - 1
                break
        if total_time < people:       #시간이 부족하다.
            min_time = mid + 1
    return result

def main():
    people = int(input())
    time = list(map(int, input().split()))
    print(find_min(people, time))

if __name__ == "__main__":
    main()
