a = int(input())

n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
n1 = 0

while a >= 100:
    a -= 100
    n100 += 1

while a >= 50:
    a -= 50
    n50 += 1

while a >= 20:
    a -= 20
    n20 += 1
    
while a >= 10:
    a -= 10
    n100 += 1

while a >= 5:
    a -= 5
    n5 += 1

while a >= 2:
    a -= 2
    n2 += 1

while a >= 1:
    a -= 1
    n1 += 1

print(f'{n100} nota(s) de R$ 100''\n',end="")
print(f'{n50} nota(s) de R$ 50''\n',end="")
print(f'{n20} nota(s) de R$ 20''\n',end="")
print(f'{n10} nota(s) de R$ 10''\n',end="")
print(f'{n5} nota(s) de R$ 5''\n',end="")
print(f'{n2} nota(s) de R$ 2''\n',end="")
print(f'{n1} nota(s) de R$ 1''\n',end="")

#'\n'f'{n50} nota(s) de R$ 50''\n'f'{n20} nota(s) de R$ 20''\n'f'{n10} nota(s) de R$ 10''\n'f'{n5} nota(s) de R$ 5''\n'f'{n2} nota(s) de R$ 2''\n'f'{n1} nota(s) de R$ 1',end="")
