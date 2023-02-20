# This code works to enter multiple values (check "2nd example" for a code to enter only one value)

# First we create a variable that will hold the values inputted by the user. We have to use list comprehension to make multiple
# values input possible 

# In this case: the loop 'for' iterates 'z', which are the indexes belonging to the values inside the list created by the
# 'input' function, and then int(z) will add that list (or its values) to 'C' one by one

C = [int(z) for z in input("Enter multiple values: ").split(',')] # This is called "List comprehension", find material about it on the Repository README file


# Then we create an empty list and we call the 'extend' method to link 'my_list' and 'C'
my_list = []
my_list.extend(C) #The difference between methods 'extend' and 'append' is that 'append' accepts only one value and it adds it at the end of the list

# Next step is to create a text for the user to see what is happening. In this case only the even numbers will be printed on the screen
# We make this outside the for loop because otherwise it will be printing the text every time the loop iterates itself
print("Following numbers are even: ", end='\n') 

# Finally we create the 'for' loop that will go through every index in our 'my_list' and check them. If it's an even number it
# will print it, if not it will pass and iterates itself again until there is no more items to check
for n in my_list: # For 'n' in 'my_list' (meaning for every item inside that object)
    if n%2==0: # if that item, after is divided by 2, gives us a remainder of 0, then it means it's even. We make this operation with the syntax "n%2 == 0"
        print(n) # if the previous condition is met then it will print the item on the terminal
print() # We call the 'print' function once more so the next item is printed on the next line

# The program will ask the user to input multiple values; then it will iterate through them and print just the even numbers