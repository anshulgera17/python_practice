# Print tables till user quit
while True:
    try:
        def table():
            print("Please insert a number for table")
            num = int(input())
            for x in range(1, 13):
                tab = num * x
                print("{} * {} = {} ".format(num, x, tab))

        table()
    except KeyboardInterrupt:
        break