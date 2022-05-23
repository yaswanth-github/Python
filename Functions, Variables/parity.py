# num = int(input("Enter Number :: "))

# if num % 2 == 0:
#     print("The Number",num,"is Even")
# else:
#     print("The Number",num,"is Odd")


def main():
    num = int(input("Enter Number :: "))
    if is_even(num):
        print("The Number",num,"is Even")
    else:
        print("The Number",num,"is Odd")


def is_even(x):
    # if x % 2 == 0:
    #     return True
    # else:
    #     return False
    return x % 2 == 0 # Gives True

main()