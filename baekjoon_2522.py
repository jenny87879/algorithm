star_row = int(input())
for i in range(1, star_row+1,1):
  for j in range(star_row-i):
    print(' ', end='')
  for k in range(i):
    print('*', end='')  
  print('')
for i in range(star_row-1,0,-1):
  for j in range(star_row-i):
    print(' ', end='')
  for k in range(i):
    print('*', end='')  
  print('')