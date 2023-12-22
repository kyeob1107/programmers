def solution(price, money, count):
    if money>=price*(count*(1+count)/2):
        return 0
    
    return price*(count*(1+count)/2)-money