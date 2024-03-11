from ft_filter import ft_filter
from sys import argv


def main():
    '''
        The program outputs a list of strings longer than the number given.
    '''
    try:
        assert len(argv) == 3, "AssertionError: the arguments are bad"
        assert argv[2].isdigit(), "AssertionError: the arguments are bad"

        initlist = argv[1].split(" ")
        number = int(argv[2])
        finalist = ft_filter(lambda string: len(string) > number, initlist)

        result = []
        for item in finalist:
            result.append(item)
        print(result)
        return 0

    except AssertionError as msg:
        print(msg)
        return 1


if __name__ == '__main__':
    main()
