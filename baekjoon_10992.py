star = int(input())
for i in range(0, star, 1):
  if(i<star-1):
    for j in range(star-1-i):
      print(' ', end='')
    for k in range(1):
      print('*', end='')
    for l in range((2*i)-1):
      print(' ', end='')
    if(i>0):
      print('*',end='')
    print('')
  else:
    for n in range((star*2)-1):
      print('*', end='')
    print('')