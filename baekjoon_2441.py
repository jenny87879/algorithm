star_count = int(input())
for i in range(star_count, 0, -1):
  for j in range(star_count-i):
    print(' ', end='')
  for k in range(i):
    print('*', end='')
  print('')