num = int(input())
if num>=1 & num<=9:
  for i in range(1, 10):
    print(num, ' * ', i, ' = ', num*i, sep='')