'''
Write a program to determine whether 'n' is a factorial number or not. Factorial of a number is the product of all positive numbers from 1 to 'n'.
Input format:
The input containing an integer 'n' which denotes the given number.
Output format:
If the given number is factorial, print "Yes". Otherwise, print "No".
Refer the sample output for formatting.
Sample Input:
6
Sample Output:
Yes
'''
factorial=int(input())
fact=1
i=1
while fact<factorial:
    i+=1
    fact*=i
if factorial==0 or factorial==1:
    print('Yes')
elif fact==factorial:
    print("Yes")
else:
    print('No')
