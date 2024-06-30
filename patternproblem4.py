# pattern problem
"""sample input:
4
sample output:
   *
  ***
 *****
*******
"""
n=int(input())
m=n
for i in range(0,n):
    for j in range(0,m):
        print(" ",end="")
    m=m-1
    for j in range(0,i*2+1):
        print("*",end="")
    print()