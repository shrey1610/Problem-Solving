# minimum key presses problem
"""George has a setup which includes a special keyboard and a monitor, that initially displays 0. The
special keyboard has 11 numeric keys (0,1,2,3,4,5,6,7,8,9,00). If he presses 00, the previously
displayed value will be multiplied by 100. Whereas, if he presses any other numeric key, the
previously displayed value will be firstly multiplied by 10 and then the number on the key will be
added to it
• You are given a numeric string S. Your task is to help George find and return an Integer value,
representing the minimum number of key presses to reach the number.
Input Specification:
Input: A numeric string s. representing the final number,
Output Specification:
Return an integer value, representing the minimum number of key presses to reach the number.
Sample Input:
 100
Sample Output:
2 
"""
s=input()
count=0
i=0
while i<len(s)-1 :
    if s[i]=="0" and s[i+1]=="0":
        count+=1
        i+=2
    else:
        count+=1
        i+=1
if i<len(s):
    count +=1
print(count)