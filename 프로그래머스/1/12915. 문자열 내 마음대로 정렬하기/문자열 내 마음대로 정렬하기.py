def solution(strings, n):
    #보기 편하게 바꾸자면
    strings=[strings[i][n]+strings[i] for i in range(len(strings))]
    strings=sorted(strings)
    return [s[1:] for s in strings]
    #보기 불편하지만 한줄로 줄이면
    #return[s[1:] for s in sorted([strings[i][n]+strings[i] \
    #                              for i in range(len(strings))])]