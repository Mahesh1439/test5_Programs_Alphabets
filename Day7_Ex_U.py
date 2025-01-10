'''
*           * 
*           *
*           *
*           *
*           *
*           *
*           *
*           *
  * * * * *
'''
for r in range(9):
    for c in range(7):
        if (c==0 and r!=8) or (r==8 and c!=0 and c!=6) or (c==6 and r!=8):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()