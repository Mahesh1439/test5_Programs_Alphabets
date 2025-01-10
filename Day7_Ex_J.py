'''
        * 
        *
        *
        *
*       *
*       *
*       *
*       *
* * * * *
'''
for i in range(9):
    for j in range(5):
        if (j==0 and i>3) or i==8 or j==4 :
            
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()