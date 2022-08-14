# Python code to create a directory for file transfer logging stuff.
# TODO: Create a directory using today's date

# X TODO: String name for directory must contain date, source origin, destination, and requestor
# X TODO: Write a receipt to a file
# TODO: Allow to get values from a config file.
# TODO: Copy content file from a deposit folder to newly created folder.

#import os
import textwrap
#import shutil
from datetime import date

# Definition to check if the string is empty
def check_valid_string(str):
    if(str is None or str == ""):
      print("Value cannot be empty")
      return False
    else:
      return True

# Definition to propmt user to input values for fields.
def valid_poll(prompt, validity):
    validity = False
    while validity is False:
        prompt_input=input(prompt)
        valid = check_valid_string(prompt_input)
        if valid:
            valid = True
            return prompt_input

# Variables
response = []
valid = False
date = date.today().strftime("%m-%d-%y")
config_filename="logger_config.txt"

# Prompt user for input.
response.append(valid_poll("Enter the requestor: ", valid))
response.append(valid_poll("Enter the source origin: ", valid))
response.append(valid_poll("Enter the destination: ", valid))


destination_string=response.pop()
source_string=response.pop()
requestor=response.pop()

# Construct filename string.
filename = f"{date}_{source_string}_{destination_string}"
text_filename = f"{filename}.txt"
print(text_filename)

with open(text_filename, 'w') as dto_file:
    #read(text_filename)
    text_to_write= f"""
                    =======================================
                    ++++ Receipt for {text_filename} ++++
                    =======================================

                    Source: {source_string}
                    Destination: {destination_string}
                    Requestor: {requestor}
                    Date of Transaction: Transfer completed on {date}
                    """
    dto_file.write( textwrap.dedent(text_to_write))

