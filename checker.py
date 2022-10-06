import itertools
from personalInfo import PersonalInfo


class Checker:

    def passwordChecker(personalInfo: PersonalInfo, password):
        options=[]
        passwordOptions= []
        options.extend(Checker.checkPossibleString(personalInfo.stringData, password))
        options.extend(Checker.checkPossibleDates(personalInfo.dateData, password))
        for length in range(len(options)+1):
            passwordOptions.extend(itertools.combinations(options, length))
        return passwordOptions


    @staticmethod 
    def checkPossibleString(list, password):
        options = []
        found = []
        for word in list:
           options.extend(Checker.stringOptions(word))
        for option in options:
            if option in password:
                found.append(option)
        return found

    @staticmethod 
    def checkPossibleDates(list, password):
        options = []
        found = []
        for date in list:
            options.extend(Checker.dayConverter(date.day))
            options.extend(Checker.monthConverter(date.month))
            options.extend(Checker.yearConverter(date.year))

        for option in options:
            if option in password:
                found.append(option)
        return found


    @staticmethod        
    def dayConverter(day):
       return [*set([day,str(day).lstrip("0")])]

    @staticmethod
    def monthConverter(month):
        return [*set([month,str(month).lstrip("0")].extend( Checker.monthToLetter(month)))]

    @staticmethod
    def yearConverter(year):
        return [*set(year,year % 100)]


    @staticmethod
    def monthToLetter(month):
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
        return Checker.stringOptions(result)
    

    @staticmethod
    def stringOptions(word):
        # TODO leet
        return [word.upper(),word.lower(), word.capitalize()]
        
