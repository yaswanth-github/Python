def main():
    print_square(3)

def print_square(size):
    #For Each Row in square
    for i in range(size):
        print("#" * size)
        
        #For Each Brick in Row
        # for j in range(size):
        #     #For Brick
        #     print("#",end="")
        # print("")

main()