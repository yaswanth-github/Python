def main():
    a=input("Enter Num1 :: ")
    b=input("Enter Num2 :: ")
    print("For Number Calculation")
    cal(a,b)
    print("For Concatenation")
    con(a,b)


#For Number Calculation
def cal(a,b):
    c= int(a)+int(b)
    print("Gives",c)


#For Concatenation
def con(a,b):
    c= a+b
    print("Gives",c)

main()

