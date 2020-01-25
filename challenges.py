"""
Challenge questions from coding interviews, etc.
Some from https://www.geeksforgeeks.org/must-do-coding-questions-for-companies-like-amazon-microsoft-adobe/
"""
#QUESTION: Given a string as your input, delete any reoccurring character, and return the new string.

# challenge_phrase = input("What is the string? ")
def enhance():
    final = []
    previous_letter = ""
    for letter in challenge_phrase:
        #if letter == previous letter then erase letter
        if previous_letter != letter:
            final.append(letter)
            previous_letter = letter
    # "".join([])
    print("".join(final))
        #if previous letter is equal to new letter then replace previous letter with new letter.
# enhance()


# Sort a list by numerical value (without special functions)
your_list = [12, 15, 11, 22, 15, 22, 15, 15, 4, 44, 51, 44, 15, 12, 4, 4]


"""Given an array A[] of integers, sort the array according to frequency of elements. That is elements that have 
higher frequency come first. If frequencies of two elements are same, then smaller number comes first."""


def repeat_sort(A):
    unique_nums = []
    frequencies = []
    for i in A:  # Look at each number in the list
        # Check if we have already seen this number
        if i not in unique_nums:
            # If we haven't, add it to our results and note how many there are
            frequency = len([x for x in A if x == i])
            unique_nums.append(i)
            frequencies.append(frequency)
    # Now we have lists of numbers and the number of times each one appears
    final_nums = []
    final_freqs = []
    for i in range(len(unique_nums)):
        current_max_f = max(frequencies)
        # Get location of each number with that frequency
        match_locations = [i for i, val in enumerate(frequencies) if val == current_max_f]
        if len(match_locations) > 1:  # If multiple matches
            matching_nums = [unique_nums[i] for i in match_locations]  # List of all nums with this freq
            selected_index = match_locations[matching_nums.index(min(matching_nums))]  # Get index of the lowest one
            final_freqs.append(frequencies.pop(selected_index))
            current_max_num = unique_nums.pop(selected_index)
            final_nums.append(current_max_num)
        else:  # only one match
            selected_index = match_locations[0]
            final_freqs.append(frequencies.pop(selected_index))
            current_max_num = unique_nums.pop(selected_index)
            final_nums.append(current_max_num)
    for n, f in zip(final_nums, final_freqs):
        print("Num: ", n, "\tAppears:", f)

    return final_nums


#repeat_sort(your_list)
"""
Jarvis is weak in computing palindromes for Alphanumeric characters.
While Ironman is busy fighting Thanos, he needs to activate sonic punch but Jarvis is stuck in computing palindromes.
You are given a string S containing alphanumeric characters. Find out whether the string is a palindrome or not.
If you are unable to solve it then it may result in the death of Iron Man.
"""
S = ["racecar", "butter", "boob", "palindrome"]


def test_palindrome(S):
    for word in S:
        print(word[0:] == word[::-1])
# word[2]
# word[-1]
# word[::-1]  # just means backwards

"""
Challenge: Get user input and save to a file called "settings.txt"
"""
#user_input = input("What to save? ")

#with open("settings.txt", "w") as file:
#    file.write(user_input)

#with open("settings.txt", "r") as file:
#    blank_space = file.read()
#    print(blank_space)


"""
Challenge: Read "essay.txt" and count how many words there are. Bonus for calculating average word length.
"""
def count_words():
    with open("essay.txt", "r") as file:
        written_essay = file.read()
    # create word count
    word_count = 0
    #look at each individual letter and the following character if it is followed by anything other than " " then ignore it.
    for letter in written_essay:
        previous_letter = letter
        if letter == " ":
            word_count += 1

# if it is followed by a  " " add +1 to word count

#print word count
#print(word_count)

# look at each individual letter and the following character if it is followed by anything other than " " then ignore it.
#word_count = 0
#previous_letter = ""
#for letter in written_essay:
#    if letter == " " and previous_letter != " ":
#        word_count += 1

#essay_list = written_essay.split(' ')
#print(len(essay_list))

"""
Challenge: Given a list of numbers, return the lowest number that can be made as a sum of two list items, that is not 
divisible by any other list item.
my_nums = [7, 3, 0, 30, 5, 4, 11, 8, 23]
"""

#my_nums = [6, 3, 7, 4]
my_nums = [7, 3, 30, 5, 4, 11, 8, 23]

def lowest_calc(numbers):
    numbers.sort()
    print(numbers)
    smallest_int = numbers[0] + numbers[1]
    return smallest_int


#result = lowest_calc(my_nums)
#print(result)

def lowest_unique(numbers):
    numbers.sort()
    lowest_list = []
    for x in numbers:
        for y in numbers:
            lowest_sum = x + y
            #print(lowest_sum)
            lowest_list.append(lowest_sum)
    lowest_list.sort()
    lowest_list1 = lowest_list.copy()

    for z in lowest_list1:
        for num in numbers:
            if z % num == 0:
                try:
                    lowest_list.remove(z)
                except:
                    pass

    print(lowest_list[0])
    #print(lowest_list)
lowest_unique(my_nums)


