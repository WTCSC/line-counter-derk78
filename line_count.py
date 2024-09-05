def line_count():
  count = 0 
# Start "count" at 0 since we'll be adding a value to it for each line in the .txt file.            
  file = open('file.txt', 'r')
# Open the file and use the mode 'r' to read the file without making any changes.
  lines = file.readlines()
# Iterate over each line in the file.
  for line in lines:
    count = count + 1 
# For each new line update the variable "count" by 1.
  file.close()
  return count
# When returning variable "count" make sure the variable is outside the loop to return the last value (the total amount of lines in the file).