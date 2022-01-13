numbers = [5, 2, 5, 2, 2]
# for num in numbers:
#     i = 1
#     while i<=num:
#         print('*' * num)
#         i=i+1
#         break
# print('Done...')

for num in numbers:
    output = ''
    for count in range(num):
        output += 'x'
    print(output)
