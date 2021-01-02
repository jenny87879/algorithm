try:
  while True:
    a, b = map(int, input().split())
    if(a == 0 & b == 0):
      exit()
    else:
      print(a + b)
except:
  exit()