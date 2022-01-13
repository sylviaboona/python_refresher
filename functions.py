def greet_user():
    print('Hi there')
greet_user()

#PARAMETERS
def greet_user(firstname, lastname):
    print(f"Hi {firstname} {lastname}")
greet_user('Sylvy', 'Bee') #positional arguments,


#KEYWORD ARGUMENTS - come handy in improving readability of code esp with numeric values
# when passing both positional and keyword arguments, start with positional arguments
greet_user(lastname='Sylvy', firstname='Bee') 


#RETURN STATEMENT
def square(number):
    return number * number
print(square(6))

#CREATING A REUSABLE FUNCTION
# def map_digits():

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