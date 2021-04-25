# This is an exercise to practice how to get data from a text file.

# opens the txt file
text_file = open('data_store.txt')    # opens the txt file

# assign the values to the list called "store_list"
store_list = []
for line in text_file:
    store_list.append(int(line.rstrip()))
text_file.close()                     # Close the txt file
print(store_list)

number = 0                          # creates variables for the decoding part.
decoded_list = []

for x in store_list:                # for loop to decode the store_list
    number += x
    decoded_list.append(number)

print(decoded_list)                 # for loop to decode the store_list
