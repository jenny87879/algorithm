count = int(input())

for i in range(count):
  x, y= map(int, input().split())
  print("Case #%d: %d", %(i+1, x+y))