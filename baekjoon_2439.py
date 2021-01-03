star_count = int(input())
for i in range(1, star_count+1):
  for j in range(star_count-i):
    print(' ',end='')
  for k in range(i):
    print('*',end='')
  print('')