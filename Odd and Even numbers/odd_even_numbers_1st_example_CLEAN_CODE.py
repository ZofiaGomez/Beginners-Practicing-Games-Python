# "CLEAN CODE" (you can copy any of these codes into your code editor 
# and run it to see how it works)

# Be sure to check the README file for this program

C = [int(z) for z in input("Enter multiple values: ").split(',')] 

my_list = []
my_list.extend(C) 
print("Following numbers are even: ", end='\n') 

for n in my_list: 
    if n%2==0: 
        print(n) 

print()