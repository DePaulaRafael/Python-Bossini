lista = []
lista1 = []

a = int(input())
lista = input().split()
lista1 = input().split()

print(max(lista),min(lista),'\n',end="")

if max(lista) == min(lista):
    print('S\n',end="")
else:
    print('N\n',end="")

print(max(lista1),min(lista1),'\n',end="")

if max(lista1) == min(lista1):
    print('S\n',end="")
else:
    print('N\n',end="")
