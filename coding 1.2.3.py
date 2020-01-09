
# Create a function that takes in a list of numbers
def pwn(numbers=None, art=None):
    # default set to none
    # If no list provided, ask the user
    if numbers == None:
        numbers = input("What are your numbers (without spaces)? ")
        #numbers = list(numbers)
        numbers = [int(x) for x in numbers]
    if art == None:
        art = input("What symbol would you like to use? ")

    for each_number in numbers:
        # print(art * each_number)
        for i in range(each_number):
            print(art, end="")
        print("\n", end="")
# F = 52422
# U =


# Use case 1 (give a list):
#my_list = [5, 2, 5, 2, 2]
#pwn(my_list)

# Use case 2 (user input):
pwn()