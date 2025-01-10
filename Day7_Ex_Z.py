'''
* * * * * 
      *
    *
  *
* * * * *
'''
for r in range(5):
    for c in range(5):
        if r==0 or c+r==4 or r==4 :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()