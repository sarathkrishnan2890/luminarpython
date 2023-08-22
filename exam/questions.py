"""
1.to find the sum of n natural numbers using while loop
2.to print full pyramid pattern(*)
3.print separate even and odd numbers from given list
list1=[1,2,3,4,5,6]
4.reverse a number [1,2,3,4,5]
"""
# #1.sum of n natural numbers
# num=int(input("enter the number:"))
# sum=0
# while(num>0):
#     sum=sum+num
#     num=num-1
# print(sum)


#2.pyramid
x=int(input("enter the level you want:"))
for i in range(1,x+1):
    for j in range(x-i):
        print(" ",end=" ")
    for k in range(i):
        print("* ",end="  ")
    print()

# 3.separate even number and odd numbers
list1=[1,2,3,4,5,6]
even=[x for x in list1 if x % 2 ==0]
print("even numbers=",even)
odd=[x for x in list1 if x % 2 !=0]
print("odd numbers=",odd)


#4.reverse a number
number=256
reverse=0
while number>0:
    rem=number%10
    reverse=reverse*10+rem
    number=number//10
    print(reverse)


