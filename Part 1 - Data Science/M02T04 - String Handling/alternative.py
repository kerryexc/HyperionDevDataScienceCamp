#Get user to enter a sentence
#Turn sentence into a string
string = input("Enter a short sentence.")
upper_lower = ''.join([string[i].upper() if i % 2 == 0 else string[i].lower() for i in range(len(string))])
print(upper_lower)

