# To find sum of the numbers 
while True:
    try:
        print("Please insert the number for sum from  1 to number")
        num = int(input())
        def sum():
            for x in range(1, num + 1):
                number = int(x * (x + 1))/2 

            print(number)    

        sum()
    except KeyboardInterrupt:
        break