# find the largest number in this list
    # numbers = [5, 4, 2, 6, 9, 1]

    # for num in numbers:
    #     if num == max(numbers):
    #         print(num)



#2D lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(matrix[0][2])
# for row in matrix:
#     for item in row:
#         print(item)

#list METHODS
numbers = [5, 6, 3, 9, 6, 1, 5, 6, 3]
# print(numbers.count(1))
# numbers.append(21) # adds an item to the end of the list
# numbers.insert(0, 10) # insterts a new item to the list at a specified position
# numbers.remove(6) # removes the specified item
# # numbers.clear()
# numbers.pop() # removes the last item in a list

# # numbers.reverse()
# numbers2 = numbers.copy()
# numbers.sort()
# print(numbers)
# print(numbers2)
# print(30 in numbers) # checks is a number exists in a list

#PROGRAM TO REMOVE DUPLICATES IN A LIST
sorted_numbers = []
for num in numbers:
    if num not in sorted_numbers:
        sorted_numbers.append(num)
print(sorted_numbers)