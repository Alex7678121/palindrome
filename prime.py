# n=int(input("Enter the number :"))
# for i in range(2,n+1):
#           if i>=1:
#                     for i in range(2,n):
#                               if i%n==0:
#                                         print(f"{n} is Not a prime number")
#                                         break
#                     else:
#                               print(f"{n} is a prime number")
#           else:
#                     print(f"{n} is not a prime number") 

# def number(n):
          # while n>0:
                    # print(n)
                    # n+=1
                    # if n==11:
                    #         break
          # return n
# number(1)

# n=int(input("Enter the number :"))
# temp=n
# rev=0
# while n>0:
          # sum=n%10
          # rev=rev*10+sum
          # n=n//10
# if temp==rev:
#         print(f"{temp} is a palindrome")
# else:
#         print(f"{temp} is not a palindrome ")

# space=4
# for i in range(1,6):
#         for j in range(space):
          #       print(" ",end=" ")
#         space=space-1 
#         for k in range(i):
          #       print("*",end=" ")  
#         print()  
# 
# def pal(n):
        #   rev=0
        #   while n>0:
                #   digit=n%10
                #   rev=rev*10+digit
                #   n=n//10 
        #   print(rev)
        #   return n
# n=int(input("Enter the number :"))
# pal(n)
# 
# def i (n,a):
        # return n+a
# print(i(4,5))
        # 
# 
# print(i(45,98))

import numpy as np
arr1=np.array([1,2,3,4,5,6])
print(arr1[::-1])