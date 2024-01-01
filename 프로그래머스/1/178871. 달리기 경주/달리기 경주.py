def solution(players, callings):
    player_dict={players[i]:i+1 for i in range(len(players))} #name:rank
    for name in callings:
        rank=player_dict[name]-1
        player_dict[players[rank-1]]+=1 #앞에 있던사람 등수 하나 늘린다
        player_dict[name]-=1 #불린 사람 등수 하나 줄여준다
        players[rank-1],players[rank]=players[rank],players[rank-1]
        
    return players

'''#시간초과
def solution(players, callings):
    #answer = []
    for i in callings:
        rank=players.index(i)
        players[rank-1],players[rank]=players[rank],players[rank-1]
    return players'''
