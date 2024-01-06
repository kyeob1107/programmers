def solution(elements):
    answer=0
    result=set([])
    d_list=elements*2
    for scope in range(1,len(elements)+1):
        for i in range(len(elements)):
            result.add(sum(d_list[i:i+scope]))
            
    return len(result)