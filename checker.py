import itertools
from itertools import permutations, product

from optionDate import OptionDate
from optionWord import OptionWord
from personalInfo import PersonalInfo
from workOnStrings import WorkOnStrings
from workOnDates import WorkOnDates



class Checker:

    def __init__(self, personalInfo:PersonalInfo, optionWord:OptionWord, optionDate:OptionDate):
        self.personalInfo = personalInfo
        self.optionWord = optionWord
        self.optionDate = optionDate


    # Return all the posibilities of each string (list of lists)
    def getPossibleStrings(self):
        result = []
        for word in self.personalInfo.stringData:
            options = []

            # Apply no accent
            if self.optionWord.noAccent :
                options.append(WorkOnStrings.removeAccents( word ))

            # Apply lower
            if self.optionWord.allMin :
                options.append( word.lower())

            # Apply maj
            if self.optionWord.allMaj :
                options.append( word.upper())
                
            #Apply capital letter
            if self.optionWord.capital:
                options.append( word.capitalize()) 

            # options.extend(self.stringOptions( word ))

            # Apply leet 
            if self.optionWord.leet :
                options.extend(WorkOnStrings.leetOptions( self, word ))
            
            result.append(options)
        return result

    # Return all the posibilities of each date (list of lists)
    def getPossibleDates(self):
        result=[]
        wo =WorkOnDates()
        for date in self.personalInfo.dateData:
            options=[]
            print(date.day)
            # Apply day converter
            options.append(wo.dayConverter(date.day))

            # Apply month converter
            options.append(wo.monthConverter( date.month))
            
            # Apply year converter
            options.append(wo.yearConverter(date.year))

            result.append(options)
        return result

    
    # All the options of a string
    def stringOptions(self, word: str):
        return [word.upper(),word.lower(), word.capitalize()]
    