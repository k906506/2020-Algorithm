import re

def dart(input_string):
    input_list = []
    score_list = [0, 0, 0]
    p = re.compile("(\\d+)([a-zA-Z])([*|#]?)")
    input_list = p.findall(input_string)
    print(input_list)

    for i in range(3):
        if input_list[i][1] == "S":
            score_list[i] = int(input_list[i][0])
        elif input_list[i][1] == "D":
            score_list[i] = int(input_list[i][0])**2
        elif input_list[i][1] == "T":
            score_list[i] = int(input_list[i][0])**3

    for i in range(3):
        if input_list[i][2] == "*":
            if i < 2:
                score_list[i] *= 2
                score_list[i+1] *= 2
            else:
                score_list[i] *= 2
        elif input_list[i][2] == "#":
            score_list[i] == score_list[i]
    
    result = 0
    for i in range(3):
        result += score_list[i]
    
    return result
    

def main():
    string = input()
    print(dart(string))

if __name__ == "__main__":
    main()


#\d - 숫자와 매치, [0-9]와 동일한 표현식이다.
#\D - 숫자가 아닌 것과 매치, [^0-9]와 동일한 표현식이다.
#\s - whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미한다.
#\S - whitespace 문자가 아닌 것과 매치, [^ \t\n\r\f\v]와 동일한 표현식이다.
#\w - 문자+숫자(alphanumeric)와 매치, [a-zA-Z0-9_]와 동일한 표현식이다.
#\W - 문자+숫자(alphanumeric)가 아닌 문자와 매치, [^a-zA-Z0-9_]와 동일한 표현식이다.


#a-z : 97-122
#A-Z : 65-90