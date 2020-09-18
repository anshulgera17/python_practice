# To check number is palindrome or not

while True:
    try:
        def palindrome():
            print("Please insert a number to check palindrome")
            number = int(input())
            original = number
            reversed = 0 
            while (number != 0) :
                remainder = int(number % 10)
                reversed = int ((reversed * 10) + remainder)
                number = int(number / 10)            
            if (original == reversed):
                print("number is palindrome")
            else: 
                print("number is not palindrome")  
        palindrome()       
    except KeyboardInterrupt:
        break
    