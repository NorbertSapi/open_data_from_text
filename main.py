# This is an exercise to practice how to get data from a text file.

f = open('data_store.txt', 'r+')
lines = [line for line in f.readlines()]
f.close()
print(lines)
