row=4
col=7
for i in range(4):
        print(" ___",end="")
        print("    ",end="")
print()
for i in range(1,row*2+1):
    for j in range(4):#
        if i%2!=0:
            print('/   ',end='')
            print('\\___',end='')
    
    
        elif i%2==0:
            print('\\___',end='')
            print('/   ',end='')    
    print("")


row=3
col=5
for i in range(3):
        print(" ___",end="")
        print("    ",end="")
print()
for i in range(1,row*2+1):
    for j in range(5):#
        if i%2!=0:
            print('/   ',end='')
            print('\\___',end='')
    
    
        elif i%2==0:
            print('\\___',end='')
            print('/   ',end='')    
    print("")