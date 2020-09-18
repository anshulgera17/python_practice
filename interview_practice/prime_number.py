# This code is for prime number from 1 to 50
import math as m
n = int(input())
if n > 1:
    for i in range(2, int(m.sqrt(n))):
        if (n % i) == 0:
            print(n, "is not a prime")
            break
    else:
        print(n, "Number is prime")
else:
    print(n, "Number is not prime")


