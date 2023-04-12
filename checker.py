import itertools
from itertools import permutations, product
from personalInfo import PersonalInfo


class Checker:

    def passwordGenerator(personalInfo:PersonalInfo):
        # Create a matrix of all options
        passwords=[]
        passwordOptions= []
        results=[]
        end=[]
        passwords.extend(Checker.getPossibleStrings(personalInfo.stringData))
        for optionList in Checker.getPossibleDates(personalInfo.dateData):
            passwords.extend(optionList)
        # Find all possible combinations using up to 5 elements
        for length in range(max(6,len(passwords)+1)):
            passwordOptions.extend(itertools.combinations(passwords, length))
        
        for combination in passwordOptions:
            results.extend(itertools.product(*combination))

        for tuple in results:
            combinations =[]
            combinations=permutations(tuple,len(tuple))
            for option in combinations:
                password = ""
                for element in option:
                    password += element
                end.append(password)
        
        return end

    # Return all the posibilities of each string (list of lists)
    @staticmethod
    def getPossibleStrings(list):
        result = []
        for word in list:
            options = []
            options.extend(Checker.stringOptions(word))
            result.append(options)
        return result

    # Return all the posibilities of each date (list of lists)
    @staticmethod
    def getPossibleDates(list):
        result=[]
        for date in list:
            options=[]
            options.append(Checker.dayConverter(date.day))
            options.append(Checker.monthConverter(date.month))
            options.append(Checker.yearConverter(date.year))
            result.append(options)
        return result

    # All the options of a day
    @staticmethod        
    def dayConverter(day):
        return [*set([str(day),"0" + str(day)])] if day<10 else [*set([str(day),str(day)])]

    # All the numerical and literal options of a month
    @staticmethod
    def monthConverter(month):
        result=[]
        result.extend([*set([str(month),str(month).lstrip("0")])])
        result.extend(Checker.monthToLetter(str(month)))
        return result

    # All the options of a year
    @staticmethod
    # TODO 2k21 bullshit etc
    def yearConverter(year):
        return [*set([str(year),str(year % 100)])]


    # All the litteral options of a month
    @staticmethod
    def monthToLetter(month):
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
        # print("result: " + result)
        # print(Checker.stringOptions(result))
        return Checker.stringOptions(result)
    
    # All the options of a string
    @staticmethod
    def stringOptions(word: str):
        # TODO leet
        return [word.upper(),word.lower(), word.capitalize()]
        
