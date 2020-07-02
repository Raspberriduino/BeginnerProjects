#
#
# David Pierre-Louis
# August 11, 2019
# SEC 290 32784.201930 SUMMER 2019 - Block II
# Programming Assignment 5
#
# Create a Python program that will serve as a
# menu-driven interface that manages a dictionary
# of Frequently Asked Questions (FAQ's)
#
# Questions serve as the keys and answers serve as 
# the values.
# 
# 
# 

menu = """

==========================
Frequently Asked Questions
==========================

0: Exit
1: List FAQ's
2: Add FAQ
3: Delete FAQ
"""

faq_dictionary = {}

done = False

while not done:
    print(menu)
    selection = input("Please enter a choice: ")
    print () #Blank line for spacing

    if selection == "0":
        done = True

    elif selection == "1":
        for question, answer in faq_dictionary.items():
          print("Question: {} \nAnswer: {:>6} \n".format(question, answer))
          
                
    elif selection == "2":
        
        while True:
            question = input("Please enter the question: ")
            
            if question in faq_dictionary:
                print("\n{} is already in the notebook. \nPlease rephrase the question.".format(question))
                print()
                continue
            
            else:
                 answer = input("Please enter the answer: ")
                 faq_dictionary[question] = answer
                 print("\nYour question has been added to the notebook.")
                 break

            
    elif selection == "3":
        
        while True:
            del_question = input("Please enter the question to be deleted: ")
            
            if del_question in faq_dictionary:
                del(faq_dictionary[del_question])
                print("\n{} has been removed from the FAQs".format(del_question))
                print()
                break
            
            else:
                 print("\nCould not find {} in the FAQs. \nNo changes made. \n".format(del_question))
                 break
            
    else:
        print("Warning! {} is not a valid entry.".format(selection))
        print()
        leave = input("Would you like to Try Again? [y/n]") # Asking the user if they wanted to continue running the program
        leave = leave.upper()
        if leave == "Y":
            continue
        if leave == "YES":
            continue
        else:
            break
        
print("Thank you for using the Frequently Asked Questions! Your session is now Done!")
