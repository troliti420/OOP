
from personalInfo import PersonalInfo
from checker import Checker

import datetime



# Defining main function
def main():
   print("Welcome to Password Checker")
   personalInfo = PersonalInfo(["test","dan"],[datetime.date.today()])
   # ,datetime.date(1998, 11, 8)
   print(Checker.passwordGenerator(personalInfo)) 
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()