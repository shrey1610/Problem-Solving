#message encoding   i,e 167 --> 13649 without using string

"""You work in the message encoding department of a national security agency. Every message that is
sent from or received in your office is encoded. You have an integer N, and each digit of N is
squared and the squares are concatenated together to encode the original number. Your task is to
find and return an integer value representing the encoded value of the number.
Input format
Input1:An integer value N representing the number to be encoded
Output :
Return an integer value representing the encoded value of the number """


# n=int(input())
# temp=n
# ans=0
# while n>0:
#     temp=n%10
#     ans=temp**2
#     print(ans)
#     n=n//10




#167--> 16394
n=167
#sod
def sod(n):
    c=0
    while n>0:
        c+=1
        n=n//10
    return c
def rev(n):
    ans=0
    while n>0:
        digit=n%10
        sq=digit**2
        sod_sq=sod(sq)
        ans=ans*(10**sod_sq)+sq
        n=n//10
    return ans
ans=rev(n)
def rev2(n):
    ans2=0
    while n>0:
        digit=n%10
        ans2=ans2*10+digit
        n=n//10
    return ans2
print(rev2(ans))