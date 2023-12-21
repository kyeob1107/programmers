def solution(a, b):
    return sum([x*y for x,y in list(zip(a,b))])
    
    
    
    #numpy의 함수 이용해서 날먹할려했었는데 왜인지 모르겠지만 안됨
    #TypeError: Object of type int64 is not JSON serializable
    #import numpy as np
    #return np.dot(a,b)