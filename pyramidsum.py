# pyramid sum
"""Adam has a pyramid of numbers. The pyramid structure is formed by arranging the numbers in the
following pattern
     1
    212
   32123
  4321234
 543212345
N__212__N
• The first row contains the number 1. The second row contains the numbers 2, 1, and 2. The third
row contains the numbers 3, 2, 1, 2, and 3. This pattern continues for subsequent rows, until it
reaches N, which represents the height of the pyramid.
• Given height of pyramid N find the sum of the numbers in the pyramid and return the sum as the
output.
Sample input:
3
Sample output:
17 
"""
n=int(input())
s=0
for i in range(2,n+1):
    m=i
    while m>1:
        s+=(2*m)
        m-=1
s+=n*1 #for adding all 1 at a time
print(s)