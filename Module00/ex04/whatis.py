from sys import argv


if len(argv) > 1:
    try:
        assert len(argv) <= 2, "AssertionError: more than one argument is \
provided"

        try:
            int(argv[1])
        except ValueError:
            assert False, "AssertionError: argument is not an integer"

        if len(argv) == 2:
            if int(argv[1]) % 2:
                print("I'm Odd.")
            else:
                print("I'm Even.")

    except AssertionError as msg:
        print(msg)
