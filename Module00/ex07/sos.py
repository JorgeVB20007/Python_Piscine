from sys import argv


def generate_dictionary():
    '''
        Generates the Morse dictionary here for a cleaner program.
    '''
    result = {
        " ": "/ ",
        "a": ".- ",
        "b": "-... ",
        "c": "-.-. ",
        "d": "-.. ",
        "e": ". ",
        "f": "..-. ",
        "g": "--. ",
        "h": ".... ",
        "i": ".. ",
        "j": ".--- ",
        "k": "-.- ",
        "l": ".-.. ",
        "m": "-- ",
        "n": "-. ",
        "o": "--- ",
        "p": ".--. ",
        "q": "--.- ",
        "r": ".-. ",
        "s": "... ",
        "t": "- ",
        "u": "..- ",
        "v": "...- ",
        "w": ".-- ",
        "x": "-..- ",
        "y": "-.-- ",
        "z": "--.. ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
        "0": "----- "
    }
    return (result)


def main():
    try:
        assert len(argv) == 2, "AssertionError: the arguments are bad"
    except AssertionError as msg:
        print(msg)
        exit(1)

    morse = generate_dictionary()
    result = ""
    message = (argv[1]).lower()
    try:
        for c in message:
            result += morse[c]
    except KeyError:
        try:
            assert False, "AssertionError: the arguments are bad"
        except AssertionError as msg:
            print(msg)
            exit(1)

    print(result)


if __name__ == '__main__':
    main()
