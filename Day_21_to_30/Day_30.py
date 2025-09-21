def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
        

print(factorial(5))

# f0=0
# f1=1

# f2=f1+f0
# f(n)=f(n-1)-1+f(n-1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)



print(fibonacci(4))