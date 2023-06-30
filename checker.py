import itertools
from itertools import permutations, product
import unicodedata
from optionDate import OptionDate
from optionWord import OptionWord
from personalInfo import PersonalInfo
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
            if self.optionWord.noAccent :
                options.append(self.removeAccents(self, word))
            
            options.extend(self.stringOptions( word ))
            if self.optionWord.leet :
                options.extend(self.leetOptions( word ))
            result.append(options)
        return result

    # Return all the posibilities of each date (list of lists)
    def getPossibleDates(self):
        result=[]
        for date in self.personalInfo.dateData:
            options=[]
            options.append(WorkOnDates.dayConverter(date.day))
            options.append(self.monthConverter(date.month))
            options.append(self.yearConverter(date.year))
            result.append(options)
        return result

    # All the numerical and literal options of a month
    def monthConverter(self, month):
        result=[]
        result.extend([*set([str(month),str(month).lstrip("0")])])
        result.extend(self.monthToLetter(str(month)))
        return result

    # All the options of a year
    # TODO 2k21 bullshit etc
    def yearConverter(self, year):
        return [*set([str(year),str(year % 100)])]


    # All the litteral options of a month
    def monthToLetter(self, month):
        result =''
        match month:
            case "01":
                result= "janvier"
            case "02":
                result ="fevrier"
            case "03":
                result= "mars"
            case "04":
                result ="avril"
            case "05":
                result= "mai"
            case "06":
                result ="juin"
            case "07":
                result= "juillet"
            case "08":
                result ="aout"
            case "09":
                result= "septembre"
            case "10":
                result ="octobre"
            case "11":
                result= "novembre"
            case "12":
                result ="decembre"
        return self.stringOptions(result)
    
    # All the options of a string
    def stringOptions(self, word: str):
        return [word.upper(),word.lower(), word.capitalize()]
    


    # All the leet bullshit
    def leetOptions(self, word: str):
        result=[]
        stringOptionResult=[]
        result.append(word)
        index=0
        while index < len(result):
            for character in result[index]:
                match character.lower():
                    case "a":
                        result.append(result[index].replace("A","4",1))
                        result.append(result[index].replace("a","4",1))
                    case "e":
                        result.append(result[index].replace("E","3",1))
                        result.append(result[index].replace("e","3",1))
                    case "i":
                        result.append(result[index].replace("I","1",1))
                        result.append(result[index].replace("i","1",1))
                    case "o":
                        result.append(result[index].replace("O","0",1))
                        result.append(result[index].replace("o","0",1))
                    case "l":
                        result.append(result[index].replace("L","1",1))
                        result.append(result[index].replace("l","1",1))
                    case "s":
                        result.append(result[index].replace("S","5",1))
                        result.append(result[index].replace("s","5",1))
                    case "b":
                        result.append(result[index].replace("B","8",1))
                        result.append(result[index].replace("b","8",1))
                    case "t":
                        result.append(result[index].replace("T","7",1))
                        result.append(result[index].replace("t","7",1))
                    case "z":
                        result.append(result[index].replace("Z","2",1))
                        result.append(result[index].replace("z","2",1))
                    case "g":
                        result.append(result[index].replace("G","6",1))
                        result.append(result[index].replace("g","6",1))  
            result = list(dict.fromkeys(result))
            index +=1
        # Apply upper case lower case capitalize for all the options
        for option in result:
            stringOptionResult.extend(self.stringOptions(option))
            
        return stringOptionResult
    
    # Remove accents from words
    @staticmethod
    def removeAccents(self, word: str):
        result = unicodedata.normalize('NFKD', word).encode('ASCII', 'ignore').decode()
        return result
