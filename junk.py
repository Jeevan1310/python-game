print("Welcome")
def simple():
    n=input("Enter the number")
    print(n)

def max():
    print("Function max is invoked")

def acess():
    s=input("Enter the device name")
    if s=='samsung' :
        d=input("Welcome samsung , Enter Your passcode")
        if d=='1234':
            print("acces granted")
        else:
            print("acess denied")
    elif s=='apple':
        c=input("Welcome apple , Enter Your passcode")
        if c=='0001':
            print("acces granted")
        else:
            print("acess denied")


simple()
max()