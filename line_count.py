def line_count():
  count = 0 
  file = open('file.txt', 'r')
  lines = file.readlines()
  for line in lines:
    count = count + 1 
  file.close()
  return count