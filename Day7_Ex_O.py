'''
  * * * *   
*         *
*         *
*         *
*         *
*         *
*         *
*         *
  * * * *
'''
for r in range(9):
    for c in range(6):
        if ((c==0 or c==5) and r!=0 and r!=8) or ((r==0 or r==8) and c!=0 and c!=5) :
            
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()