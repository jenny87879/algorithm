count = int(input())
arr = [0 for _ in range(91)]
arr[1], arr[2]  = 1, 1
for i in range(3, count+1):
  arr[i] = arr[i-1] +arr[i-2]
print(arr[count])
