n = int(input())
arr = [0 for i in range(n+1)]
square = [i * i for i in range(1, 317)]
for i in range(1, n + 1):
  s = []
  for j in square:
    if j > i:
        break
    s.append(arr[i - j])
  arr[i] = min(s) + 1
print(arr[n])