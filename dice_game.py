import random

# class Dice:
#     def roll(self):
#         dice_numbers = (1, 2, 3, 4, 5, 6)
#         output = random.choice(dice_numbers)
#         return output


# dice1 = Dice()
# dice2 = Dice()

# result = f"({dice1.roll()}, {dice2.roll()})"

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1,6)
        return first, second

dice = Dice()
result = dice.roll()
print(result)