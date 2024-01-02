# Exercise: Write a program to read through a file and print the contents of the file (line by line) all in upper case. 
file = open('mbox-short.txt')

for line in file:
    characters = line.rstrip()
    print(characters.upper())