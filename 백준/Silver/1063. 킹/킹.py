import sys
input = sys.stdin.readline

def move(pos_king, pos_stone, string):
    # print("디버깅: ", pos_king, pos_stone, string, end=':::')
    # 숫자로 변환 부분
    col = col_encoding.index(pos_king[0]) + 1
    row = int(pos_king[1])
    col_s = col_encoding.index(pos_stone[0]) + 1
    row_s = int(pos_stone[1])
    
    # 이동 해석 및 반영 부분
    mc, mr = 0, 0
    if 'R' in string:
        mc += 1
    if 'L' in string:
        mc -= 1
    if 'T' in string:
        mr += 1
    if 'B' in string:
        mr -= 1
    
    col += mc
    row += mr
    
    # print(col, row, col_s, row_s)
    if row > 8 or row < 1  or col > 8 or col < 1:
        # print("응 아니야 돌아가:", col, row)
        return pos_king, pos_stone
    
    if col == col_s and row == row_s:
        col_s += mc
        row_s += mr
        if row_s > 8 or row_s < 1  or col_s > 8 or col_s < 1:
            # print("응 아니야 돌아가2:", col_s, row_s)
            return pos_king, pos_stone
    
    # 문자로 변환 부분
    return col_encoding[col - 1] + str(row), col_encoding[col_s - 1] + str(row_s)

king, stone, N = input().split()
N = int(N)
col_encoding = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# 벽 만들어서 -1로 할까하다가 효율이 없을 것 같아서 일단 보류

for _ in range(N):
    king, stone = move(king, stone, input().strip())
    # print("디버깅2: ", king, stone)

print(king, stone, sep='\n')