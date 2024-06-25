#inp n output smallest prime number which is larger than n
def func(n):
    for i in range(2,int(n**0.5)+1):  #sqrt can be written as num**0.5  or we can use n//2 or n as a limit
        if n%i==0:
           return False
    return True
num=int(input())
k=num+1
while True:
    if func(k):
        print(k)
        break
    k+=1