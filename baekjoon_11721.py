input_text = input()
for i in range(0, len(input_text), 10):
  try:
    print(input_text[i:i+10])
  except:
    print(input_text[i:])
