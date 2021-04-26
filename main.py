# This is an exercise to practice how to get data from a text file.

# opens the txt file
text_file = open('data_store.txt')  # opens the txt file
print(type(text_file))
# assign the values to the list called "store_list"
store_list = []

for line in text_file:
    store_list.append(int(line.rstrip()))
# Close the txt file
text_file.close()  # Close the txt file
print()


# create a function
def decoder(test_list):
    number = 0  # creates variables for the decoding part.
    decoded_list = []
    for x in test_list:  # for loop to decode the store_list
        number += x
        decoded_list.append(number)
    return decoded_list


# assign and display the decoded list
decoded_list_1 = decoder(store_list)  # assign the decoded list
print(decoded_list_1)


f = open("final-1.txt", "a+")  # create a new txt file for the final result
# write the decoded_list_1 in the text file.
for i in decoded_list_1:
    f.write("%s " % i)
f.close()
