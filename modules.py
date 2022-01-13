# # import converter_module
# from converter_module import kgs_to_lbs

# # print(converter_module.kgs_to_lbs(70))
# kgs_to_lbs(70)


#----------------------


# import utils_module
# numbers = [1,4, 2,3]
# print(utils_module.find_max(numbers))

#-----------------------------

import random
for i in range(3):
    print(random.random())
    print(random.randint(10, 20))

members = ['John', 'Mary', 'Sylvy']
leader = random.choice(members)
print(leader)

#WRITE A PROGRAM TO RANDOMLY SELECT TWO NUMBERS WHEN YOU ROLL A DICE
dice_numbers = (1, 2, 3, 4, 5, 6)
first_number = random.choice(dice_numbers)
second_number = random.choice(dice_numbers)
output = f"({first_number}, {second_number})"
print(output)