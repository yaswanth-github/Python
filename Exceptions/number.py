def main():
    X=get_int("What is X :: ")
    print("X is",X)


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
           pass
main()