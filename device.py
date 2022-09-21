from my_fa import fa
print(" - Welcome to Dixia -")
def acess():
    user_input=input("Enter the device name : ")
    if user_input=='samsung' :
        d=input("Welcome samsung , Enter Your passcode  ")
        if d=='1234':
            print("acces granted")
            print("we want to verify it ")
        else:
            print("acess denied")
    elif user_input=='apple':
        c=input("Welcome apple , Enter Your passcode  ")
        if c=='0001':
            print("acces granted")
        else:
            print("acess denied")
    elif user_input == 'realme':
        c=input("Welcome Realme , Enter Your passcode  ")
        if c=='###2':
            print("acces granted")
        else:
            print("acess denied")
    else:
        print("Sorry wrong device ")

#Main plot configuration

a=['Owner','Guest','user2.0']
b=['Admin','User','maxie']


user=input("Enter Your user name ")

if user in a :
    print("Succes")
    acess()
elif user in b:
    print("second type accesed")
    num=int(input("enter key : "))
    fa(num)
else:
    print("unsucessful")
