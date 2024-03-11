from sys import argv, stdin


def readinput() -> str:

    '''
        This function reads until a double newline or a ^D is found
        and then returns all the content read.
        (Newlines are substituted by whitespaces)
    '''

    fulltext = ""
    print("What is the text to count?")
    try:
        while True:
            thechar = stdin.read(1)
            if not thechar:
                break
            if (thechar == "\n"):
                thechar = " "
            fulltext += thechar
    except EOFError:
        print()
    return fulltext


def main():

    '''
        The program will return the amount of characters given. More
        specifically, the amount of UPPERCASE and lowercase characters,
        punctuation marks, whitespaces and digits.
        If no argument is given, a prompt will appear to introduce it.
    '''

    try:
        assert len(argv) < 3, "AssertionError: More than one argument\
was provided."
    except AssertionError as msg:
        print(msg)
        return 1
    fullstring = ""

    if len(argv) == 2:
        fullstring = argv[1]
    else:
        fullstring = readinput()

    allchars = 0
    upperchars = 0
    lowerchars = 0
    punctmarks = 0
    spaces = 0
    digits = 0

    for c in fullstring:
        allchars += 1
        if (c.isupper()):
            upperchars += 1
        elif (c.islower()):
            lowerchars += 1
        elif (c.isdigit()):
            digits += 1
        elif (c.isspace()):
            spaces += 1
        elif (c.isprintable()):
            punctmarks += 1

    print("The text contains {0} characters:".format(allchars))
    print("{0} upper letters".format(upperchars))
    print("{0} lower letters".format(lowerchars))
    print("{0} punctuation marks".format(punctmarks))
    print("{0} spaces".format(spaces))
    print("{0} digits".format(digits))


if __name__ == '__main__':
    main()
