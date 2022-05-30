while True:
    try:
        X=int(input("What's X :: "))

    except ValueError:
        print("X is not an integer, Give Only Integer")
    else:
        break
print("X is",X)