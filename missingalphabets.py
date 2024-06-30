#program to find misisng alphabets in a given input
"""Pangram is a sentence containing every letter in the English alphabet. Given a string, find all
characters that are missing from the string, Le., the characters that can make the string a Pangram
We need to print output in alphabetic order.
For example,
Input: welcome to geeksforgeeks
Output: abdhijnpquvxyz 
"""
str=input()
alpha="abcdefghijklmnopqrstuvwxyz"
str1=""
for i in alpha:
    if i not in str:
        str1=str1+i
print(str1)