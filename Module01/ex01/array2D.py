def slice_me(family: list, start: int, end: int) -> list:
    '''
        Gets a 2D list and slices it from `start` to `end`.
    '''
    try:
        assert type(family) is list, "AssertionError: not a list."
    except AssertionError as msg:
        print(msg)
        return None

    if len(family) > 0:
        lineref = len(family[0])
        try:
            for item in family:
                assert len(item) == lineref, "AssertionError: the lists \
lengths are not consistent."
        except AssertionError as msg:
            print(msg)
            return None
    print("My shape is : (" + str(len(family)) + ", " +
          str(len(family[0])) + ")")
    sliced = slice(start, end, 1)
    print("My new shape is : (" + str(len(family[sliced])) + ", " +
          str(len(family[sliced][0])) + ")")
    return (family[sliced])
