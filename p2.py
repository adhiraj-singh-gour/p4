# n= int(input("Enter no"))
# x=0
# y=1
# z=0

# while z<=n:
#     print(x)
#     x=y
#     y=x+y
#     z=z+1




# # Python program to find the factorial of a number provided by the user.

# # change the value for a different result
# num = 7

# # To take input from the user
# #num = int(input("Enter a number: "))

# factorial = 1

# # check if the number is negative, positive or zero
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)



num = int(input('enter no:'))

sum=0
temp=num

while temp>0:
    digit=temp%10
    cube=digit**3
    sum=sum+cube
    temp //=10
if sum == num:
    print('it is armstront no')
else:
    print('it is not armstront no')         