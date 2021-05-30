lst = []
lista = []

quanti = int(input())

while quanti > 0 :
    num = input('How many numbers: ')
    num += '/'
    quanti -1

lst = num.split('/')
lista = lst[0]

  
print("Maximum element in the list is :", max(lista),
 "\nMinimum element in the list is :", min(lista))