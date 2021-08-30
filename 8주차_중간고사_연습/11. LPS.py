def find_lps(input):
    p_list = []
    for i in range(len(input)):
        for j in range(i, len(input) + 1):
            s = input[i:j]
            ps = s[::-1]
            if s == ps:
                p_list.append(len(s))
    return max(p_list)       

def main():
    input_string = input().lower().strip().replace(" ", "")
    print(find_lps(input_string))

if __name__ == "__main__":
    main()