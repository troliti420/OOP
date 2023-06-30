from personalInfo import PersonalInfo
from optionDate import OptionDate
from workOnStrings import WorkOnStrings

class WorkOnDates(WorkOnStrings):
    
    # All the options of a day      
    def dayConverter(self, day ):
        return [*set([str(day),"0" + str(day)])] if day<10 else [*set([str(day),str(day)])]
    
    # All the numerical and literal options of a month
    def monthConverter( self, month):
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
        # workOnStrings =WorkOnStrings()
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
        return WorkOnStrings.stringOptions(result)
    
    #Print dans la console du travail effectué
    def printMessage(self):
        print("je modifie des dates")