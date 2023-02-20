# First we will define a variable that will hold the value of an input that the user will
# insert to be converted: input_minutes or input_seconds in this case

input_minutes = int(input()) # "int" meaning that we require the user to write an integer number (a number without decimals; a whole number)

input_seconds = int(input())


# We ask for an input from the user with the namesake function "input". And we can also add a text inside the
# brakets like this --> int(input("Write the minutes in whole numbers: "))
# If we need to input the minutes with seconds included, instead of using the function "int", we rather use "float"


# Then, for each ecuation we need to define another variable but in reverse. These variables have a really long name with the
# intention of being more understandable, but it is best if you choose a short and easy name e.g. --> "conv_sec" or "conv_min"

converted_into_seconds = input_minutes*60 # To get how many seconds are in X minutes, we multiply those minutes by 60

converted_into_minutes = input_seconds/60 # To get how many minutes are in X seconds, we devide those seconds by 60


# Finally we print the variable we want to know; the program will ask the user to input a number; then it will do the 
# operation and print it on the terminal

print(converted_into_seconds)

print(converted_into_minutes)