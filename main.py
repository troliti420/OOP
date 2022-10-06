
from personalInfo import PersonalInfo
from checker import Checker

import datetime



# Defining main function
def main():
   print("Welcome to Password Checker")
   password = "Dan08"
   p = PersonalInfo(["test","dan","poo"],[datetime.date.today()])

   print(Checker.passwordChecker(p, password))

   print(datetime.date.today().year)
  
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()