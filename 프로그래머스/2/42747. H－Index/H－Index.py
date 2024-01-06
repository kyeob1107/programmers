def solution(citations):
    #answer = 0
    citations.sort() #정렬
    cnt={}
    check_list=list(set(citations))
    check_list.sort(reverse=True)
    for key in citations:
        if key in cnt:
            cnt[key] += 1
        else:
            cnt[key] = 1
    for h in range(max(cnt),-1,-1):
        check=0
        for j in [i for i in check_list if i>=h]:
            check += cnt[j]
        #print("ch",check,h)
        if check >= h:
            return h
        #print("안맞아서 하나 작은걸로")