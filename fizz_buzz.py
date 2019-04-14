nmr = int(input("Enter number between 1 and 100: "))

for nmr in range (1 + nmr):
    if nmr % 3 == 0 and nmr % 5 == 0:
        print("fizzbuzz")
    elif nmr % 3 == 0:
        print("fizz")
    elif nmr % 5 == 0:
        print("buzz")
    else:
        print(nmr)

# for x in range (1, 100):
#     print
#
#     if int(x%3) and int(x%5)
#         print("fizbuzz")

# User enters a number between 1 and 100
# FizzBuzz program starts to count to that number (it prints them in the Terminal).
# In case the number is divisible with 3, it prints "fizz" instead of the number. If the number is divisible with 5, it prints "buzz".
# If it's divisible with both 3 and 5, it prints "fizzbuzz".