def solution(park, routes):
    s_pos=[0,0] #[y,x] y:북&남 , x:동&서
    cnt_pos=[] #장애물 있는 위치 can't
    y_size=len(park)
    x_size=len(park[0]) #모든 park[y]의 사이즈가 같을 것이니
    for y in range(y_size):
        for x in range(x_size):
            if park[y][x] =='S': #시작 위치 기억
                s_pos[0],s_pos[1] = y,x
            if park[y][x] =='X': #장애물 위치 기억
                cnt_pos.append([y,x])
    #print(s_pos, cnt_pos)
    now_pos=s_pos #처음 위치 시작위치로 적용
    for move in routes: #굳이 split으로 나눠서 각각 적용 말고 위치 고정(0,2)일테니 이용
        if move[0] =='E':
            for num in range(1,int(move[2])+1):
                if now_pos[1]+num >=x_size: #0~size-1까지 가능 범위이니 넘으면 패스
                    break
                elif [now_pos[0],now_pos[1]+num] in cnt_pos:
                    break
                else:
                    if num==int(move[2]):
                        now_pos[1]+=num
        elif move[0] =='W':
            for num in range(1,int(move[2])+1):
                if now_pos[1]-num <0: #0~size-1까지 가능 범위이니 넘으면 패스
                    break
                elif [now_pos[0],now_pos[1]-num] in cnt_pos:
                    break
                else:
                    if num==int(move[2]):
                        now_pos[1]-=num
        elif move[0] =='S':
            for num in range(1,int(move[2])+1):
                if now_pos[0]+num >=y_size: #0~size-1까지 가능 범위이니 넘으면 패스
                    break
                elif [now_pos[0]+num,now_pos[1]] in cnt_pos:
                    break
                else:
                    if num==int(move[2]):
                        now_pos[0]+=num
        elif move[0] =='N':
            for num in range(1,int(move[2])+1):
                if now_pos[0]-num <0: #0~size-1까지 가능 범위이니 넘으면 패스
                    break
                elif [now_pos[0]-num,now_pos[1]] in cnt_pos:
                    break
                else:
                    if num==int(move[2]):
                        now_pos[0]-=num
        else:
            print("혹시 모를 오류잡기용")
        
    return now_pos

#가상 범위 하나 더 넣을까하다가 굳이 안넣어도 괜찮지 않을까해서 if로 미리 막으면 되니
#일단 없이 해봄