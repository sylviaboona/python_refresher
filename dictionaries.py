# use dictionaries to store infrmation that comes as key-value pairs

# customer = {
#     "name": "Sylvy Bee",
#     "age": 30,
#     "is_verified": True
# }

# customer['name'] = 'Sylvia'

# print(customer.get('name', '22/10/1988'))

numbers = {
    "1": "one",
    "2": "two",
    "3": "three"
}

phone1 = input("Phone: ")
output = ''
for i in phone1:    
    # print(numbers[i])
    output += numbers.get(i, '!') + ' '

#EMOJI CONVERTER
message = input(">")
words = message.split(' ')
emojis = {
    ":)": ""
}
