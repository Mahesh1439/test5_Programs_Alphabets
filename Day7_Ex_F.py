'''
* * * * * * 
*
*
*
* * * * * *
*
*
*
* 
'''
for i in range(9):
    for j in range(6):
        if j==0 or i==0 or i==4 :
            
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()