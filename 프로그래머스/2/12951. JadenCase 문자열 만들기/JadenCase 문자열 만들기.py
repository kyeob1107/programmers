def solution(s):
    s=s.replace(' ','#')
    pos=[]
    s=s.lower()
    answer=''
    for i in range(len(s)):
        if (s[i] !='#' and s[i-1]=='#') or i==0:
            answer+=s[i].upper()
            #pos.append(i)
        else:
            answer+=s[i]
    answer=answer.replace('#',' ')
        
    return answer