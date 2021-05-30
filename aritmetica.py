a = int(input())
b = input()
c = int(input())
d = input()
e = int(input())

action1 = str

# d = - 
if b == '+' and d == '-':
    action1 = a + c - e 

elif b == '-' and d == '-':
   action1 = a - c - e 

elif b == '*' and d == '-':
    action1 = a * c - e 

elif b == '/' and d == '-':
    if a ==0 or c == 0 :
        action1 = 'erro'
    else :  
        action1 = a // c - e 

# d  = +
elif b == '+' and d == '+':
    action1 = a + c + e 

elif b == '-' and d == '+':
    action1 = a - c + e 

elif b == '*' and d == '+':
    action1 = a * c + e 

elif b == '/' and d == '+':
    if a ==0 or c == 0 :
        action1 = 'erro'
    else :    
        action1 = a // c + e 

# d  = /
elif b == '+' and d == '/':
    if c == 0 or e == 0:
        action1 = 'erro'
    else :    
        action1 = a + c // e 

elif b == '-' and d == '/':
    if  c == 0 or e == 0:
        action1 = 'erro'
    else :    
        action1 = a - c // e 

elif b == '*' and d == '/':
    if c == 0 or e == 0:
        action1 = 'erro'
    else :    
        action1 = a * c // e 

elif b == '/' and d == '/':
    if a == 0 or c == 0 or e == 0:
        action1 = 'erro'
    else :    
        action1 = a // c // e 

# d  = *
elif b == '+' and d == '*':
    action1 = a + c * e 

elif b == '-' and d == '*':
    action1 = a - c * e 

elif b == '*' and d == '*':
    action1 = a * c * e 

elif b == '/' and d == '*':
    if a == 0 or c == 0 :
        action1 = 'erro'
    else :
        action1 = a // c * e 


# b  = +
elif b == '+' and d == '+':
    action1 = a + c + e 

elif b == '+' and d == '-':
    action1 = a + c - e 

elif b == '+' and d == '*':
    action1 = a + c * e 

elif b == '+' and d == '/':
    if c == 0 or e == 0 :
        action1 = 'erro'
    else :    
        action1 = a + c // e 

# b  = -
elif b == '-' and d == '+':
    action1 = a - c + e 

elif b == '-' and d == '-':
    action1 = a - c - e 

elif b == '-' and d == '*':
    action1 = a - c * e 

elif b == '-' and d == '/':
    if c == 0 or e == 0 :
        action1 = 'erro'
    else :    
        action1 = a - c // e 

# b  = *
elif b == '*' and d == '+':
    action1 = a * c + e 

elif b == '*' and d == '-':
    action1 = a * c - e 

elif b == '*' and d == '*':
    action1 = a * c * e 

elif b == '*' and d == '/':
    if c == 0 or e == 0:
        action1 = 'erro'
    else :
        action1 = a * c // e 

# b  = /
elif b == '/' and d == '+':
    if a == 0 or c == 0:
        action1 = 'erro'
    else :
        action1 = a // c + e 

elif b == '/' and d == '-':
    if a == 0 or c == 0:
        action1 = 'erro'
    else :
        action1 = a // c - e 

elif b == '/' and d == '*':
    if a == 0 or c == 0:
        action1 = 'erro'
    else :
        action1 = a // c * e  

elif b == '/' and d == '/':
    if a == 0 or c == 0 or e == 0:
        action1 = 'erro'
    else :
        action1 = a // c // e  


print(action1, end="")