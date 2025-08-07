#Store the names of three friends in a list of strings. 
#Create a list variable called "friends_names"

friends_names = ["Alice", "Jose", "Alana"]

#Type the the first friend's name.
print(friends_names[0])

#Type the last friend's name.
print(friends_names[2])

#Get the length of the list.
number_names = len(friends_names)
print(number_names)

#Define a list called with the friends' ages
friends_ages = ["34","25", "27"]

#Print each friends' name and age in a sentence.
sentence_alice = f"{friends_names[0]} is {friends_ages[0]} years old."
print(sentence_alice)

sentence_Jose = f"{friends_names[1]} is {friends_ages[1]} years old."
print(sentence_Jose)

sentence_alana = f"{friends_names[2]} is {friends_ages[2]} years old."
print(sentence_alana)