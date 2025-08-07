float_list = []

for i in range (10):
    while True:
        numbers = float(input("Enter a number. It can have decimals: "))
        float_list.append(numbers)
        break
            
print(f"You entered: {float_list}")

import statistics

print(sum(float_list))

print(min(float_list))
print(max(float_list))

median = statistics.median(float_list)
print(median)

average = statistics.mean(float_list)
print(average)