'''
* * * * *   
*         *
*         *
*         *
*         *
*         *
*         *
*         *
* * * * *
'''
for i in range(9):
    for j in range(6):
        if j==0 or (i==0 and j<5) or (j==5 and i>0 and i<8) or (i==8 and j<5):
            
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()