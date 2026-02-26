#Check if a number is Even or Odd
#Take an integer input from the user

number = int(input("Enter a number: "))

#Check whether the number is even or odd using an if-else statement

if number % 2 == 0:
    #dispiay the result using f-string
    print(f"{number} is an even number")
else:
    print(f"{number} is  an odd number")