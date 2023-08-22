"""1.To create a fibanocci series using python function
2.To check a number is palindrome or not
3.print following pattern
    * * * * * * * * *
      * * * * * * *
       * * * * *
         * * *
           *
4.Write a Python program to calculate the area of a triangle using function

5.How do I get the last element of a list in Python?
listitems = ["apple","orange","banana",67,90]

"""
"""
1.1.To create a fibanocci series using python function
"""
# def fibanocci(num):
#     if num==0:
#         return 0
#     elif num==1:
#         return 1
#     else:
#         return (fibanocci(num-1))+(fibanocci(num-2))
# num=int(input("enter the number:"))
# for num in range(0,num+1):
#
#  print(fibanocci(num))



# """
# 2.To check a number is palindrome or not
# """
# num=int(input("enter the number:"))
# reverse=0
# temp=num
# while num>0:
#     reminder=num%10
#     reverse=(reverse*10)+reminder
#     num=num//10
# if temp==reverse:
#     print("is palindrome")
# else:
#     print("is palindrome")
#
# #


# """
# 3.print following pattern
#     * * * * * * * * *
#       * * * * * * *
#        * * * * *
#          * * *
#            *
# """
#
# n=int(input("enter the level:"))
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(2*(n-i)-1):
#         print("*",end=" ")
#     print()





# """
# 4.Write a Python program to calculate the area of a triangle using function
# """
# def triangle_area(h,b):
#     area=(h*b)*.5
#     return area
# h=float(input("enter the height:"))
# b=float(input("enter the base:"))
# print("area of triangle =",triangle_area(h,b))
#





"""
5.How do I get the last element of a list in Python?
listitems = ["apple","orange","banana",67,90]
"""
listitems = ["apple","orange","banana",67,90]
print(listitems[-1])


