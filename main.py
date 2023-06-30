
from optionDate import OptionDate
from optionWord import OptionWord
from passwordGenerator import PasswordGenerator
from personalInfo import PersonalInfo
from checker import Checker

import datetime



# Defining main function
def main():
   print("Welcome to Password Checker")
   optionWord = OptionWord(True,True,True,True,True)
   optionDate = OptionDate(True,True,True,True,True)
   personalInfo = PersonalInfo(["dan","elias"],[datetime.date.today()])
   # ,datetime.date(1998, 11, 8)
   checker = Checker( personalInfo, optionWord, optionDate)
   passwordGenerator=PasswordGenerator(checker)
   print(passwordGenerator.all_combinations)
   # print(str(len(passwordGenerator.all_combinations)))
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()