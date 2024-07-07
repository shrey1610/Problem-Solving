#find the no of unique triplets which gives a product m
"""Input:
7
5 3 20 10 1 4 2
60
Output:
3
Explanation:
Product m:60
Possible triplets for product m:(5,4,3),(20,3,1),(10,3,2)
The count of unique triplets is 3
"""
a=[5,3,20,10,1,4,2]
n=len(a)
t,c=60,0
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            prod=a[i]*a[j]*a[k]
            if prod==t:
                # print(prod)
                # print(a[i],a[j],a[k])
                c+=1
        # print()
print(c)