monthly = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekly = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
month, day = map(int, input().split())
count = day+monthly[0]
if month>1:
  for i in range(1, month-1):
    count += monthly[i]
  date = count%7
  print(weekly[date])
else:
  date = day%7
  print(weekly[date])