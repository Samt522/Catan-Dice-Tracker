# This is just to be used to calculate the frequency of numbers rolled in a game of catan
# Importing pandas and matplotlib
import pandas as pd
import matplotlib as plt


exit_code = "0"
num_array = []
# Used a dictionary for frequency because its better
frequency = {}

outfile = open("catandice.txt","w")
               
print("Catan Dice Thingy V0.1")
print("To use, simply enter a number from 2-12")
print("When done type 00")
while exit_code != 1:
    # Simply takes input until user types "00"
    try: 
        dicenum = int(input("Enter dice number: "))
        if dicenum < 2 or dicenum > 12:
            raise "Impossible Dice rolls"
    except:
        print("Invalid number and/or string")
    num_array.append(dicenum)
    
    if dicenum == 00:
        # need to convert list to string to output
        string_list = "".join(map(str,num_array))
        with open("catandice.txt","w") as f:
            for num in string_list:
                f.write(num + "\n")
        # For finding the frequency of rolls
        for num in num_array:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        most_rolled = None
        max_count = 0
        for num, count in frequency.items():
            if count > max_count:
                max_count = count
                most_rolled = num
        # Final note, if im going to show the other numbers, i'm better off using pandas or a library for the math
        print(f"The most rolled number was {most_rolled} it was rolled {max_count} times")
        exit_code = 1