def grouping(N,num): #N:총명수,num:첫 번호, 쭉 이길시 배정될 그룹 리스트
    powers_of_two=[i for i in range(21) if 2**i<=N]#2의 몇승인지 파악하기 위해서
    n=powers_of_two[-1]
    group_list=[num]
    for i in range(1,n+1):
        if group_list[i-1]%2==0:
            group_list.append(group_list[i-1]//2)
        else:
            group_list.append((group_list[i-1]+1)//2)
    return group_list
    
def solution(n,a,b):
    a_group=grouping(n,a) #a가 속하게 될 그룹
    b_group=grouping(n,b) #b가 속하게 될 그룹
    for i in range(len(a_group)):
        if a_group[i]==b_group[i]:
            return i