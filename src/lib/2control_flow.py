number = 23
guess = int(input('Enter an integer : '))
if guess == number:
  print('Congratulations, you guessed it.')
  print('(but you do not win any prizes!)')
elif guess < number:
  print('No, it is a little higher than that')
else:
  print('No, it is a little lower than that')
print('Done')

b=iter(list(range(6)))
#for i in b:
 #print(i)
for i in b:
  print(next(b))

