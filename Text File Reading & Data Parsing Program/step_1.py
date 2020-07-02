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
# This is step_1


# Open a file for reading
text_file = open("auth.log.1")

# Read the entire file into a string with read() function
contents = text_file.read()

# This for loop could have also been used to print each line
# of the logfile
#
#for line in text_file:
#    print(line)
    
# Close the file - best practice
text_file.close()

# Display contents of the string
print(contents)

