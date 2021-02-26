import math

invalidInput = "Please Enter a valid Number"

def validate(input):
    if (input <= 0):
       return False

def isCoprime(x,y):
    gcd = math.gcd(x, y)  
    if(gcd==1):
       return True
    else:
        return False

x = int(input("Enter First Number: "))

if (validate(x)) == False:
    print(invalidInput)
else:
    y = int(input("Enter Second Number: "))  
    if (validate(x)) == False:
        print(invalidInput)
    else:   
        if (isCoprime(x,y)==True):
            print("%d and %d are coprime"%(x,y))
        else:
            print("%d and %d are not coprime, they have GCD %d"%(x,y,math.gcd(x,y)))    


   



