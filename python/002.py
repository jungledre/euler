def fib(n):
    a, b = 0, 1
    even = 0
    while a < n:
        if a%2==0:
            print a,
            even += a
        a, b = b, a+b
    print ("The sum is " + str(even))

print fib(4000000)

#answer 4613732
