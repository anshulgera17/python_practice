# This code is checking whether number is odd or even 
# we are using foo function and try except block 
# if ValueError came then we are trying to take input again
def foo():
    try:
        num = int(input())

        if (num % 2) == 0:
            print("number is even - {}".format(num))
        else:
            print("number is odd - {}".format(num)) 
    except ValueError:
        print("Please insert a number ")
        foo()
    except:
        print("we can't proceed with this input or something wrong")

foo()