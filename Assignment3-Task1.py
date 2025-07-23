def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)
x=int(input("Enter a number:"))
result=factorial(x)
print("The factorial of",x,"is:",result)