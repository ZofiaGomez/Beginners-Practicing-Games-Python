# First we will define a variable that will hold the value of an input that the user will
# insert to be converted: "fahrenheit", "celsius", or "kelvin" in this case

fahrenheit = float(input()) # "float" meaning that we require the user to write a decimal number
celsius = float(input())
kelvin = float(input())


# We ask for an input from the user with the namesake function "input". And we can also add a text inside the
# brakets like this --> float(input("Write the Fahrenheit degrees with decimals: "))


# Then, for each ecuation we need to define another variable but in reverse

celsius = (fahrenheit-32)/1.8 # To get the equivalent Celsius° of X Fahrenheit°, we use this formula
celsius = kelvin-273.15 # To get the equivalent Celsius° of X Kelvin°, we use this formula

fahrenheit = celsius*1.8+32 # To get the equivalent Fahrenheit° of X Celsius°, we use this formula
fahrenheit = 1.8*(kelvin-273.15) + 32 # To get the equivalent Fahrenheit° of X Kelvin°, we use this formula

kelvin = celsius+273.15 # To get the equivalent Kelvin° of X Celsius°, we use this formula
kelvin = (fahrenheit-32)/1.8 + 273.15 # To get the equivalent Kelvin° of X Fahrenheit°, we use this formula


# Finally we print the variable we want to know; the program will ask the user to input a number; then it will do the 
# operation and print it on the terminal

print(celsius)

print(fahrenheit)

print(kelvin)