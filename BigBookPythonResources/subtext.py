#! /usr/local/bin/python3

phrase = input('Write a phrase:\n')
file1 = open("subtext.txt", "a")  # append mode
file1.write("\n")
file1.write(phrase)
file1.close()