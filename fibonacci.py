def fib(n):

     a=0
     b=1

     if (n == 1):
        print(a)

     else:
         print(a)
         print(b)

         for i in range (1,n-1):
            x=a+b
            a=b
            b=x
            print(x)

fib(10)