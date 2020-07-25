"""
Given a set of items (from a text file) that have a given weight and value, find
the combination of items of greatest value that fit into a bag of limited space.

Desired output:
> With a given weight of XX, you should take these XX items:
> 1. (value) (weight)
>  ...
>
> Total value: XX

"""

# Initialize variables
max_weight = 56
item_file = 'items.txt'
multiple_uses = False

# 1. Read in items from file
# weights = (5, 1, 13, 2, 1, 13, 5, 5, 1, 15, 12, 3, 3, 15, 13, 12)
# values = (3, 7, 15, 9, 4, 5, 15, 11, 8, 14, 5, 15, 7, 10, 3, 5)

weights = (4,9,15,15,20,4,11,16,20,6,15,5,6,13,4,16,11,11,20,16,6,16,5,18,7,13,7,7,5,9,18,10,7,5,7)
values = (4,4,8,2,6,10,5,8,9,9,1,2,8,10,2,6,1,5,4,8,4,8,5,5,1,8,9,1,3,4,3,2,6,8,1)


# items_left = []

# 2. Solve the backpack problem :)
calculated_value = []
i = 0
# divide the values of each item by its weight to obtain calculated value
for x in values:
    temp_value = (x / weights[i], i)
    calculated_value.append(temp_value)
    # calculated_value.append(x / weights[i])
    i += 1
    # items_left.append(i)

print(calculated_value)

#max weight = 35 find out the best possible way to fill backpack
current_weight = 0
current_value = 0
# Some sort of while loop
while current_weight < max_weight:
    if len(calculated_value) == 0:
        break
    # list the calculated values from highest to lowest in calculated value and choose the most valuable.
    values_remaining = [a[0] for a in calculated_value]  # 'Extracts' the first element of each tuple in the list
    best_value_remaining = max(values_remaining)  # Finds the highest value among what we extracted
    best_value_index = values_remaining.index(best_value_remaining)  # Where in the remaining values is this located
    actual_item_index = calculated_value[best_value_index][1]  # Index location to be used in other places like weights
    if weights[actual_item_index] > max_weight - current_weight:
        calculated_value.pop(best_value_index)
        continue

    # Take the item
    current_value += values[actual_item_index]
    current_weight += weights[actual_item_index]
    # Pop out based on best_value_index
    calculated_value.pop(best_value_index)
    #print("The best choice is in position", actual_item_index)
    print(f"adding item with weight {weights[actual_item_index]} and value {values[actual_item_index]}")


print(f"Bag is full, final weight: {current_weight}\tfinal value: {current_value}")

# End!

