import random

dice_roll = int(input('How many dice would you like?'))
dice_size = int(input('How many sizes should the dice have?'))
dice_sum = 0
for i in range(0, dice_roll):
  roll = random.randint(1, dice_size)
  dice_sum += roll
  if roll = 1:
    print(f'You rolled a {roll}! Critical Failure')
  elif roll = dice_size:
    print(f'You rolled a {roll}! Critical Success!')
  else:
  print(f'You rolled a {roll}')
print(f'You have rolled a sum of {dice_sum}')

if __name__== "__main__":
  main()
