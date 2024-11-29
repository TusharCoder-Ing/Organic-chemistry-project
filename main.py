print("Welcome to the Chemistry Translator")
userMode = int(input("Choose a mode 1: Nomenclature, 2: Formula, 3: Number of bonds>>> "))


#defining the category of the hydrocarbon
def hydrocarbonCategory(c, h):
    if userMode != 2:
        if c!=0 and h==(2*c)+2 :
            return "alkane"
        elif c!=0 and h==(2*c) :
            return "alkene"
        elif c!=0 and h==(2*c)-2 :
            return "alkyne"
        else:
            exit("Try again with number of C atoms <= 10 and with atmost one single and double bond between C and H!")


#defining certain variable based on the mode
if userMode == 1 or userMode == 3:
    userC = int(input("Enter the number of C atoms>>> "))
    userH = int(input("Enter the number of H atoms>>> "))
    category= hydrocarbonCategory(userC, userH)
elif userMode == 2:
    userHC = str(input("Enter the name of a SIMPLE hydrocarbon>>> ")).lower()
    userHCslcRW= userHC[:-3]
    userHCslcS = userHC[-3:] 
else:
    exit("Invalid mode")

#defining the root word wrt the no of C atoms only when the nomenclature mode is selected
if userMode == 1: 
    def hcrootWord(c):
        match(c):
            case 1:
                return "meth"
            case 2:
                return "eth"
            case 3:
                return "prop"
            case 4:
                return "but"
            case 5:
                return "pent"
            case 6:
                return "hex"
            case 7:
                return "hept"
            case 8:
                return "oct"
            case 9: 
                return "non"
            case 10:
                return "dec"
            case _ :
                exit("Try again with number of c atoms <= 10!")
    #get the primary suffix with the help of the category function only when the nomenclature mode is selected
    def hcPrimarySufifix():
            return category[3:]
    primarySuffix = hcPrimarySufifix()
    rootWord = hcrootWord(userC)
        





if userMode==3:
    #Calculate the bonds with the help of the category func only if the bond mode is selected
    def hcBondCalculator(category, c, h):
            if category.lower()=="alkane":
                return c+h-1
            if category.lower()=="alkene":
                return c+h
            if category.lower()=="alkyne":
                return c+h+1
        

if userMode == 2:
#define the number of C atoms with the help of slicing the user's input only if the formula mode is selected
    def hcCAtom(c):
        match(c):
            case "meth":
                return 1
            case "eth":
                return 2
            case "prop":
                return 3
            case "but":
                return 4
            case "pent":
                return 5
            case "hex":
                return 6
            case "hept":
                return 7
            case "oct":
                return 8
            case "non": 
                return 9
            case "dec":
                return 10
            case _ :
                exit("Try again with number of c atoms <= 10!")
    #define the number of H atoms with the help of slicing the user's input only if the formula mode is selected
    def hcHAtom(c, noc):
        if c == "ane":
            return int(noc*2+2)
        elif c == "ene":
            return int(noc*2)
        elif c == "yne":
            return int(noc*2-2)
        else:
            exit("Either you messed up or I messed up!")
    numberAtomsC = hcCAtom(userHCslcRW) 
    numberAtomsH = hcHAtom(userHCslcS, numberAtomsC)

if userMode == 1:
    def modeNomenclature():
        print("Name: ", hcrootWord(userC), primarySuffix, sep="")
    modeNomenclature()
elif userMode == 2:
    def modeFormula():
        print("Formula: ","C",numberAtomsC,"H",numberAtomsH, sep="")
    modeFormula()
elif userMode == 3:
    def modeBond():
        print("Number of bonds: ",int(hcBondCalculator(category, userC, userH)))
    modeBond()

