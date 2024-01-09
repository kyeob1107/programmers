def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant,completion):
        if p!=c: #다르면 그 사람이 완주 못한 것
            return p
        
    return participant[-1]
#다 비교했는데 아직 안끝났으면 마지막 남은 참가자가 미완주자