# this code is used for find the largest number among n numbers inserted by user

print("In how many numbers you wanna check the largest one")
number = int(input())
store = []

for x in range(1, number + 1):
    element = int(input())
    store.append(element)


print(store)
print ("Maximum number is {} out of many intergers in List".format(max(store)))

