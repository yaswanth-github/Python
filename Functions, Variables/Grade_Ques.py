def main():
    marks = int(input("Enter Your Marks :: "))
    
    print("Your Marks are :: ",marks)
    G1(marks)
    G2(marks)


def G1(marks):
    if marks >=90 and marks <=100 :
        print("Your Grade is O")

    elif marks >=80 and marks <90 :
        print("Your Grade is A")

    elif marks >=70 and marks <80 :
        print("Your Grade is B")

    elif marks >=60 and marks <70 :
        print("Your Grade is C")

    elif marks >=50 and marks <60 :
        print("Your Grade is D")

    elif marks >=40 and marks <50 :
        print("Your Grade is E")

    else:
        print("Your Grade is F")



def G2(marks):
    if 90 <= marks <= 100 :
        print("Your Grade is O")

    elif 80 <= marks < 90 :
        print("Your Grade is A")

    elif 70 <= marks < 80 :
        print("Your Grade is B")

    elif 60 <= marks < 70 :
        print("Your Grade is C")

    elif 50 <= marks < 60 :
        print("Your Grade is D")

    elif 40 <= marks < 50 :
        print("Your Grade is E")

    else:
        print("Your Grade is F")

main()