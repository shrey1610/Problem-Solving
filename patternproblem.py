# pattern problem
"""Print the given pattern
You are given a number n and you have to print the given pattern:
For n=3
3 3 3 2 2 2 1 1 1
3 3 2 2 1 1
3 2 1
"""
n=int(input())
for i in range(3,0,-1):
    for j in range(3,0,-1):
        k=i
        while k>0:
            print(j,end="")
            k-=1
    print()