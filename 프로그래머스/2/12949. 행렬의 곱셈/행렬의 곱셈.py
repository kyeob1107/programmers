def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)): #arr1의 a*b일때 a
        row_val=[]
        for j in range(len(arr2[0])): #arr2의 a*b일때 b
            value=0
            for cal in range(len(arr2)): #arr1의 b이자 arr2의 a
                 value+=arr1[i][cal]*arr2[cal][j]
            row_val.append(value)
        answer.append(row_val)
    return answer