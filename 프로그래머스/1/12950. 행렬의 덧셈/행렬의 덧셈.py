def solution(arr1, arr2):
    a=[]
    for i in range(len(arr1)):
        a.append([x+y for x, y in zip(arr1[i],arr2[i])])
    return a