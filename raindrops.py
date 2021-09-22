def check_raindrops(*args):
    result = ""
    if len(args) > 0:
        userinput = args[0]
    else:
        userinput = input("Enter an integer: ")
    try:
        x = int(userinput)
        if x % 3 == 0:
            result += "Pling"
        if x % 5 == 0:
            result += "Plang"
        if x % 7 == 0:
            result += "Plong"
        if len(result) > 0:
            return result
        else:
            return x
    except Exception as e:
        # print(e)
        return False


def main():
    print(check_raindrops())


if __name__ == "__main__":
    main()

