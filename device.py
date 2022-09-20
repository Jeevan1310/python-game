print(" - Welcome to Dixia -")
def acess():
    s=input("Enter the device name")
    if s=='samsung' :
        d=input("Welcome samsung , Enter Your passcode  ")
        if d=='1234':
            print("acces granted")
            print("we want to verify it ")
        else:
            print("acess denied")
    elif s=='apple':
        c=input("Welcome apple , Enter Your passcode  ")
        if c=='0001':
            print("acces granted")
        else:
            print("acess denied")
    elif s=='realme':
        c=input("Welcome Realeme , Enter Your passcode  ")
        if c=='###2':
            print("acces granted")
        else:
            print("acess denied")
    else:
        print("Sorry wrong device ")

#Main plot configuration

a=['Owner','Guest','user2.0']

user=input("Enter Your user name ")

if user in a :
    print("Succes")
else:
    print("Unsuccesful")