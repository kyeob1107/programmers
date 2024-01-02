def con_n(n,q): #n진법 변환기 (conversion to base n)
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] #문자열로 리턴


def solution(s):
    n=0 #변환 횟수
    m=0 #제거된 0의 갯수
    while s!='1':
        m+=s.count('0')
        s=s.replace('0','')
        s=con_n(len(s),2)
        n+=1
    answer = [n,m]
    return answer