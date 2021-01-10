test_case = int(input())

arr = [0 for _ in range(11)]
for i in range(test_case):
  n = int(input())
  arr[1] = 1
  arr[2] = 2
  arr[3] = 4
  for i in range(4, n+1):
    arr[i] = arr[i-3] + arr[i-2] + arr[i-1]
  print(arr[n])