import random

dice_roll = 2
dice_sum = 0
for i in range(0, dice_roll):
  roll = random.randint(1, 6)
  dice_sum += roll
  
print(f'You rolled a {roll}')
print(f'You have rolled a sum of {dice_sum}')

if __name__== "__main__":
  main()
