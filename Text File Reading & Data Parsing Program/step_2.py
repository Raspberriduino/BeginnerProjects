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
# This is step_2



count = 0

with open("auth.log.1") as text_file:  
    for line in text_file:
        if 'Failed password' in line:
            print(line)
            count += 1

# This is a large logfile and I just wanted to count the number of instances
# of "Failed password" for fun

print("{} instances found!".format(count))
