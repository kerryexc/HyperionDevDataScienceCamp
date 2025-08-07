# these are one dimensional lists
# fruits = ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats = ["chicken", "fish", "turkey"]

# each individual list represents a row
# each element represents a column
# these are two dimensional lists
# groceries = [fruits, vegetables, meats]

# this is another way to write out the rows
groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrots", "potatoes"],
             ["chicken", "fish", "turkey"]]

# groceries [] returns an entire row. index [0] is the fruits list...
# groceries[][] returns row [] column []
# print(groceries[0][1])

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    # this will print out rows and columns
    # a tuple has parenthesis in the list with each list sep. by culry braces
    print()