#A function named hello() that prints a greeting to the user.
#This function should accept no arguments and returns nothing.
def hello():
    print("Ohh, Hello I didn't see you there.")

#A function named pack() that accepts three arguments, and returns
# a single list with the three arguments inside as list elements.
def pack(x,y,z):
    return [x,y,z]

#A function called eat_lunch(). This function should accept a list
# of any length, and print out a series of strings that say
# "First I eat __" (the first element of the list), and "Next I eat ___"
# (for the following elements in the list). If the list is empty,
# print "My lunchbox is empty!". The function should not return anything.
def eat_lunch(lunch_food):
    if len(lunch_food) == 0:
        print("Mylunchbox is empty!")
    else:
        for i in range(len(lunch_food)):
            if i == 0:
                print(f"First I eat {lunch_food[0]}")
            else:
                print(f"Next I eat {lunch_food[i]}")

#tests via "python3 .\functions_practice.py" in terminal
hello()
print(pack("apple","pickle","banana"))
eat_lunch([])
eat_lunch(["apple","pickle","peanutbutter","cheese"])