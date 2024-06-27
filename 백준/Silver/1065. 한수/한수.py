# 1등 코드 비교확인용
def func(a):
    if(a<100):
        return a
    else:
        x = 99
        for i in range(100,a+1):
            
            if((i//100)+i%10==2*((i//10)%10)):
                x = x+1
        return x

x = int(input())
print(func(x))