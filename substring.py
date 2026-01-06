
def getSubstring(input):
  max_substring = ''
  curr_substring = input[0]


  for i in range(1, len(input)):

    if input[i] != input[i-1]:
      curr_substring += input[i]
    else: 
      curr_substring = input[i]
    
    if len(curr_substring) > len(max_substring):
      max_substring = curr_substring
  
  return max_substring

print(getSubstring('ABCDDDEFGHI'))