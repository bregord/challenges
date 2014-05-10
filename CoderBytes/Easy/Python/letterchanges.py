def LetterChanges(str):

    newstr =''

    for letter in str:

        if letter != ' ' and  'a' <= letter <= 'z' or 'A' <= letter <= 'Z':
            letter = chr(ord(letter)+1)

            if letter in ('a', 'e', 'i', 'o', 'u'):
                letter = letter.upper()

            

            newstr= newstr+letter


            
        elif letter == ' ':
          newstr = newstr + ' '

        else:
            newstr = newstr + letter

    return newstr
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print LetterChanges(raw_input())
