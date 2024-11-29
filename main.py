print("Welcome to the Chemistry Translator")
userC = int(input("Input the number of carbon(C) atoms>>> "))
userH = int(input("Input the number of hydrogen(H) atoms>>> "))

#defining the category of the hydrocarbon
def hydrocarbonCategory(c, h):
    if c!=0 and h==(2*c)+2 :
        return "alkane"
    elif c!=0 and h==(2*c) :
        return "alkene"
    elif c!=0 and h==(2*c)-2 :
        return "alkyne"
    else:
        exit("Try again with number of C atoms <= 10 and with atmost one single and double bond between C and H!")

#defining the root word wrt the no of C atoms
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

category = hydrocarbonCategory(userC, userH)
rootword = hcrootWord(userC)

#get the primary suffix with the help of the category function
def hcPrimarySufifix(c):
    return category[3:]

primarySuffix = hcPrimarySufifix(userC)

print("Category:", category)
print("Name: ",rootword, primarySuffix, sep="")