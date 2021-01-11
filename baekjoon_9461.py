count = int(input())
seq = [0 for _ in range(101)]
for i in range(count):
  n = int(input())
  seq[1], seq[2], seq[3] = 1, 1, 1
  seq[4], seq[5] = 2, 2
  for j in range(6, n+1):
    seq[j] = seq[j-1] + seq[j-5];
  print(seq[n])