'''
* * * * * * 
*
*
*
*       * *
*         *
*         *
*         *
* * * * * *
'''
for i in range(9):
    for j in range(6):
        if j==0 or i==0 or i==8 or (j==5 and i>3) or (j==4 and i==4) :
            
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()