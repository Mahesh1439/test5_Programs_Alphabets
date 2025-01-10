'''
* * * * * * * 
      *
      *
      *
      *
      *
      *
      *
      *
'''
for r in range(9):
    for c in range(7):
        if r==0 or c==3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()