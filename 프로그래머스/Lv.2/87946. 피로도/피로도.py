from itertools import permutations

def posible_num(k,dungeons):
    count=0
    for dungeon in dungeons:
        if dungeon[0]>k:
            continue
        else:
            k-=dungeon[1]
            count+=1
    return count

def solution(k, dungeons):
    all_number_of_cases=[]
    count_list=[]
    for case in permutations(dungeons,len(dungeons)):
        all_number_of_cases.append(case)

    for case in all_number_of_cases:
        count=posible_num(k,case)
        count_list.append(count)
    answer=max(count_list)
    return answer