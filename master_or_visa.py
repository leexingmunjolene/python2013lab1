# Filename: master_or_visa.py
# Author: Lee Xing Mun Jolene
# Index No: 5
# Description: categorize if a user input credit card number belongs to
# MasterCard or VISA.

import re

def master_or_visa(card):
    # length and number check to determine card type
    if len(card) == 13:    
        return "The number belongs to a VISA."
    elif len(card) == 16:
        if card[0] == '4':
            return "The number belongs to a VISA."
        elif card[0] == '5':
            return "The number belongs to a MasterCard."
        else:
            return "This is not a VISA or MasterCard number."
    else:
        return "This is not a VISA or MasterCard number."

# main
ccnumber = input("Please enter your credit card number: ")
ccnumber = re.sub("\D", "", ccnumber) # remove non-numerical user inputs
print(master_or_visa(ccnumber))
