# special string
# print(ord("p"))  this is how to get ascii value of any string in the python
"""Alice has a string A consisting of lowercase English letters. Her friend gives her another string S
and asks her to modify string A. and replace its characters with the characters present in string S.
But, to achieve the above task, Alice must follow the below steps:
1. Choose a character from string S that has the minimum ASCII distance from the ith character in
string A
Replace the character in string A with the chosen character in string S
Your task is to find and return an integer value, representing minimum total ASCII distance that is
required to modify string A to the characters in string S. Return 0, if all the characters in string S are
already present in string A
Sample Input:
abcd
xyz
Sample Output:
86 
"""
a=input()
s=input()
min,j,su,i=999,0,0,0
# for i in range(0,len(a)):       this loop also works
while i<len(a):
    # for j in range(0,len(s)):   this loop also works
    if i not in s:
        min=125
    while j<len(s):
        diff=abs(ord(a[i])-ord(s[j]))
        # print(diff)
        if diff<min:
            min=diff
            su+=min
        j+=1
    j=0
    i+=1
print(su)