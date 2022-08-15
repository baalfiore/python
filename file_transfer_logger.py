# Python code to create a directory for file transfer logging stuff.
# TODO: Create a directory using today's date

# X TODO: String name for directory must contain date, source origin, destination, and requestor
# X TODO: Write a receipt to a file
# Create an interface to select options
# X TODO: Copy content file from a deposit folder to newly created folder.
# TODO: Copy content as long as it is a valid file or directory.


import os
import textwrap
import shutil
from datetime import date

#Globals
YES_INPUT="Y"
NO_INPUT="N"
WRITE_FLAG="w"

#CUSTOMS
parent_dir=r"C:\Users\brand\Documents\Coding_Workspace\python"

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
response.append(valid_poll("Enter the source: ", valid))
response.append(valid_poll("Enter the destination: ", valid))

destination_string=response.pop()
source_string=response.pop()
requestor=response.pop()

# Construct filename string.
filename = f"{date}_{source_string}_{destination_string}"
text_filename = f"{filename}.txt"
print(text_filename)

with open(text_filename, WRITE_FLAG) as receipt_file:
    text_to_write= f"""
                    =======================================
                    ++++ Receipt for {text_filename} ++++
                    =======================================

                    Source: {source_string}
                    Destination: {destination_string}
                    Requestor: {requestor}
                    Date of Transaction: Transfer completed on {date}
                    """
    receipt_file.write(textwrap.dedent(text_to_write))

# Make the directory of interest if it doesnt exist already.
if not os.path.exists(f"{parent_dir}"):
  print(f"Creating new path... {parent_dir}\n")
  os.mkdirs(f"{parent_dir}/{filename}")
else:
  print(f"Creating new path... {parent_dir}/{filename}\n")
  os.mkdir(f"{parent_dir}/{filename}")

user_choice=input(f"Would you like to move the files to the directory of interest, {filename}? \n(Y/N)\n ->>")

# check user input
if user_choice.upper() == YES_INPUT:
  src_for_copy=input(f"Please enter in the path to the directory or file of interest you wish to copy to {filename}\n ->>")
  if os.path.exists(user_choice):
    if os.path.isdir(src_for_copy):
      print(f"Directory detected.\nCopying {src_for_copy} directory to {filename}...")
      shutil.copytree(src_for_copy, filename)
    else:
      print(f"File detected.\nCopying {src_for_copy} fle to {filename}...")
      shutil.copy(src_for_copy,filename)
  else:
    print("Path does not exist!")
elif user_choice.upper() == NO_INPUT:
  exit
else:
  print("Input value not recognized....")
