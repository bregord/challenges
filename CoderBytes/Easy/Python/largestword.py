
"""
def LongestWord(sen): 

  words = sen.split()
  largest = ''
  
  for word in words:
    if len(word) >= len(largest):
      largest = word
  
  return largest
  
  
  # code goes here
  text = "Code must be properly"
  more = " indented in Python!"
  return text + more 
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LongestWord(raw_input())           


#looks like I only handled words, and not strings per se
"""
def LongestWord(sen): 

  words = sen.split(' ')
  largest = ''
  
  for word in words:
    if len(word) > len(largest):
      largest = word
  
  return largest
  
  
  # code goes here
  text = "Code must be properly"
  more = " indented in Python!"
  return text + more 
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LongestWord(raw_input())           


#This is better
