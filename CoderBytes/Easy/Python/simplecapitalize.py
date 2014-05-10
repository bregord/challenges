def LetterCapitalize(str): 

  words = str.split(' ')
  newwords = []
  newstring = ''
  
  for word in words:
      newword = word[1:]
      capital= word[0].upper()

      newword = capital+newword

      newwords.append(newword)

  for words in newwords:
      newstring = newstring + ' ' + words 


  newstring = newstring[1:]
 
  return newstring
    
    

print LetterCapitalize(raw_input())  
















  
