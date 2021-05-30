a,b = input().split()


a = int(a)
b = int(b)

if a >= 0 and b >= 0:
    if a ==0 and b ==0:
        print('NO ALVO!', end="")
    else :
        print('R1')

elif a < 0 and b > 0 :
    print('R2', end="")

elif a < 0 and b < 0:
    print('R3', end="")

elif a > 0 and b < 0:
    print('R4', end="")

