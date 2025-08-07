#ask the user to enter a sentence
str_manip = input("Enter a sentence.")
print(str_manip)
#To get the total number of characters.
print(len(str_manip))

#Find the last letter of every word in str_manip sentence. Replace ever occurence with @
new_char = '@'
new_string = str_manip.replace(str_manip[-1],new_char)
print(new_string)

#Print the last three characters in the sentence backwards
words = str_manip.split()
last_word = words [-1]
print(last_word)
#something about positioning; this concept isn't the clearest to me about the numbers. It isn't clicking completely...
reverse_word = print(last_word[5:1:-1])

#Create a five letter word made up of the first three characters and the last two characters in string_manip.

first_word = words[0]
print(first_word)
#This format extracts x number words
first_five = print(first_word[:3])

last = words[5]
print(last)
last_two = print(last[5:1:-1])

#combine these into one word

result = first_word[:3] + last[5:1:-1]
print(result)