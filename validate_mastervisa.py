# Filename: validate_mastervisa.py
# Author: Lee Xing Mun Jolene
# Index No: 5
# Description: validates a user input MasterCard or VISA credit card number

import re

def master_or_visa(card):
    # length and number check to determine card type
    if len(card) == 13:    
        return "VISA"
    elif len(card) == 16:
        if card[0] == '4':
            return "VISA"
        elif card[0] == '5':
            return "MasterCard"
        else:
            return "This is not a VISA or MasterCard number."
    else:
        return "This is not a VISA or MasterCard number."
    
def validate(card):
    check = 0
    if master_or_visa(card) == "This is not a VISA or MasterCard number.":
        return "This is not a valid card number."   
    else:
        for odd in range(1, len(card), 2): # add odd number to checksum
            check += int(card[odd])
        for even in range(0, len(card) ,2): # add even number to checksum
            if (int(card[even]) * 2) > 9:   
                check += (int(card[even]) * 2) - 9
            else:
                check += int(card[even]) * 2
        if check % 10 == 0: 
            return "This is a valid " + master_or_visa(card) + " number."
        else:
            return "This is not a valid card number."

# main
ccnumber = input("Please enter your credit card number: ")
ccnumber = re.sub("\D", "", ccnumber) # remove non-numerical user inputs
print(validate(ccnumber))
