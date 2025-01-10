'''
* * * * * 
    *
    *
    *
    *
    *
    *
    *
* * * * *
'''
for i in range(9):
    for j in range(5):
        if j==2 or i==0 or i==8 :
            
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()