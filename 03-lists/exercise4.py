# Create a list and add 100 random numbers to it
# In the list, can you find if the list contains duplicates?

import random

data = []
for i in range(100):
    data.append(random.randint(1, 400))
print(data)
for i in range(len(data)):
    remaining_data = data[i+1:]
    if data[i] in remaining_data:
        print(data[i])