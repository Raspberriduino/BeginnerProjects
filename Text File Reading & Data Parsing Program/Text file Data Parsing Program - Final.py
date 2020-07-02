#
# David Pierre-Louis
# August 14, 2019
# SEC 290 32784.201930 SUMMER 2019 - Block II
# Programming Assignment 6
#
# The objective of this homework assignment is to 
# demonstrate proficiency with reading files, and 
# using string methods to slice strings, working 
# with dictionaries and using-step wise development 
# to complete your program. 
# 
# Your assignment is to write a Python program in 
# four steps that reads a Linux authentication log 
# file, identifies the user names used in failed
# password attempts and counts the times each user
# name is used.
#
# You need to complete this assignment in four
# separate steps and will be submitting four separate
# programs.
#
# This is hwk6.py

    
#Created empty dictionary    
dictionary = {}

#Opening logfile with "with" to automatically close when done
with open("auth.log.1") as text_file:

#Searching each line in logfile
    for line in text_file:

#Slicing string to show only username in lines containing "Failed Password"
        if 'Failed password' in line:
            start = line.find("invalid user")
            end = line.find(" from")
            user_name = line[start+13 : end]

# Adding the username to the dictionary and assigning a value of 1            
            if user_name not in dictionary:
                dictionary[user_name] = 1

# Adding 1 to the value of the username (key) if it is already in the dictionary               
            else:
                count = dictionary.get(user_name)
                dictionary[user_name] = (count + 1)
                
# Using a for loop to print out all the user names (keys) and their no. of occurences
# in the log file

for user, occurence in dictionary.items():
    print("Attackers tried {} times to log in as {}".format(occurence, user))

