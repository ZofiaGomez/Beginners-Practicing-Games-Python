# This code works to enter only one value (check "1st example" for a code to enter multiple values)

# First we create a variable that will hold the values inputted by the user
# In this case: the loop 'for' iterates 'z', which are the indexes belonging to the values inside the list created by the

y = int(input())

# We create the 'if' loop that will check the item inside our 'y' list, and if it meets the first condition, it will print the body of
# the 'if' and excecute its statements. If not, it will pass and print the body of the 'else' and excecute its statements
if y%2==0:
    print("%d is an even number" %y)
else:
    print("%d is an odd number" %y)

# The program will ask the user to input a value; then it will check if it's even or odd and print the proper text