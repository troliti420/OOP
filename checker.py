import itertools
from itertools import permutations, product

from optionDate import OptionDate
from optionWord import OptionWord
from personalInfo import PersonalInfo
from workOnStrings import WorkOnStrings
from workOnDates import WorkOnDates



class Checker:

    def __init__(self, personalInfo:PersonalInfo, optionWord:OptionWord, optionDate:OptionDate):
        self._personalInfo = personalInfo
        self._optionWord = optionWord
        self._optionDate = optionDate
        self.workOnDates = WorkOnDates()
        self.workOnStrings =WorkOnStrings()


    # Return all the posibilities of each string (list of lists)
    def getPossibleStrings(self):
        result = []
        for word in self._personalInfo.stringData:
            options = []

            # Apply no accent
            if self._optionWord.noAccent :
                options.append(self.workOnStrings.removeAccents( word ))

            # Apply lower
            if self._optionWord.allMin :
                options.append( word.lower())

            # Apply maj
            if self._optionWord.allMaj :
                options.append( word.upper())
                
            #Apply capital letter
            if self._optionWord.capital:
                options.append( word.capitalize()) 

            # options.extend(self.stringOptions( word ))

            # Apply leet 
            if self._optionWord.leet :
                options.extend(self.workOnStrings.leetOptions(  word ))
            
            result.append(options)
        return result

    # Return all the posibilities of each date (list of lists)
    def getPossibleDates(self):
        result=[]
        for date in self._personalInfo.dateData:
            options=[]
            print(date.day)
            # Apply day converter
            options.append(self.workOnDates.dayConverter(date.day))

            # Apply month converter
            options.append(self.workOnDates.monthConverter( date.month))
            
            # Apply year converter
            options.append(self.workOnDates.yearConverter(date.year))

            result.append(options)
        return result

    
    