#equilibrium problem
"""You are given an array A of N integers. An equilibrium position is a position where the sum of all
integers on its left is equal to the sum of all integers on its right in the array A. Print the index of the
equilibrium position.
Note:For any given array there is only a single equilibrium position, if no equilibrium position is
found then print "NOT FOUND" without quotes.
• The array is 1 indexed.
Input Format:
The input consists of two lines:
The first line contains an integer denoting N.
The second line contains N space-separated integers denoting the elements of the array A
Input will be read from the STDIN by the candidate
Output Format:
Print the index of the equilibrium position. If no index is found, print "NOT FOUND
"""
a=list(map(int,input().split()))
sl,sr,f=0,0,0
n=len(a)
#print(n)
for i in range(0,n): 
    #print(a[i])
    for j in range(0,i+1):
        sl+=a[j] 
        #print(sl)
    for k in range(i+1,n):
        sr+=a[k]
        #print(sr)
    if sl==sr:
        print(i+1)
        f=1
        break
    sl,sr=0,0
if f==0:
    print(n//2)