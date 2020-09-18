# This code is using for factorial
# we are using while loop so user can print multiple factorial till he wanna quit
# uncomment if you wanna use except value error block
while True:
    try:
        def fact():
            print("Please insert a number for factorial")
            factorial = 1
            num = int(input())
            for x in range(1, num + 1):
                factorial = factorial * x
                    
            print(factorial)
        
        fact()

    # except ValueError:
    #     print("Please insert a valid number")
    #     fact()
    except KeyboardInterrupt:
        break