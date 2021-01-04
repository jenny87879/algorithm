star = int(input())
for i in range(0, star, 1):
  for j in range(star-1-i):
    print(' ', end='')
  for k in range(1):
    print('*', end='')
    for l in range(i):
      print(' *', end='')
  print('')