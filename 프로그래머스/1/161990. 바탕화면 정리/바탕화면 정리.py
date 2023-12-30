def solution(wallpaper):
    rdx=50      #최소 x좌표
    rdy=50      #최소 y좌표
    lux=0       #최대 x좌표
    luy=0       #최대 y좌표
    temp_x=0    
    temp_y=0    
    
    for x in range(len(wallpaper)): #wallaper 갯수가 곧 x(행의 수)
        for y in range(len(wallpaper[0])): #wallaper한 원소의 글자수가 곧 y(열의 수)
            if wallpaper[x][y]=='#': #해당 위치에 있을경우
                if x<rdx:
                    rdx=x
                if y<rdy:
                    rdy=y
                if x+1>lux:
                    lux=x+1
                if y+1>luy:
                    luy=y+1
                            
    answer = [rdx,rdy,lux,luy]
    return answer

