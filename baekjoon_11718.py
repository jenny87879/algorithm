while True:
  try:  
    input_text = input()
    print(input_text)
  except EOFError:
    exit()