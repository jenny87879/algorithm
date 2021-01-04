star_row = int(input())
for i in range(0, star_row,1):
  for k in range(i):
    print(' ', end='')
  for j in range((star_row-i)*2-1):
    print('*', end='')
  print('')
for i in range(star_row-2,-1,-1):
  for k in range(i):
    print(' ', end='')
  for j in range((star_row-i)*2-1):
    print('*', end='')
  print('')