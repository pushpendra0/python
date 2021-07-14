#To find the square root of the number
import math
n=float(input("Enter the number : "))
if n>0:
    result=math.sqrt(n)
    print(" square root of {} is {} ".format(n, result))
else:
    print("Square root is not define of {}".format(n))
