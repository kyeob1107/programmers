def solution(cards1, cards2, goal):
    for i in goal:
            if cards1[0] == i:
                del cards1[0]
                #cards1.remove(i)
                #cards1.pop(0)
                if len(cards1)==0:
                    cards1.append("end")                               
            elif cards2[0] == i:
                del cards2[0]
                #cards2.remove(i)
                #cards2.pop(0)
                if len(cards2)==0:
                    cards2.append("end")
        
            else:
                return "No"
            
    return "Yes"