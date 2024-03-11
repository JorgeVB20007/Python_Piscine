def ft_statistics(*args: any, **kwargs: any) -> None:
    '''Well, it does statistics.'''
    goodargs = []
    listlen = 0
    try:
        assert (len(args) > 0), "ERROR"
        assert args is not None and kwargs is not None, "ERROR"
        for item in args:
            goodargs.append(float(item))
            listlen += 1
    except (AssertionError, ValueError) as msg:
        print(msg)
        return

    listsum = 0
    sortedlist = sorted(goodargs)
    for num in goodargs:
        listsum += num
    for key, value in kwargs.items():
        match value:
            case "mean":
                do_mean(listsum, listlen)
            case "median":
                do_median(sortedlist, listlen)
            case "quartile":
                do_quartile(sortedlist, listlen)
            case "std":
                do_std(goodargs, listsum, listlen)
            case "var":
                do_var(goodargs, listsum, listlen)


def do_mean(listsum, listlen) -> None:
    '''It does mean. duh'''
    print("mean:", listsum / listlen)


def do_median(sortedlist, listlen) -> None:
    '''It does median. duh'''
    if listlen % 2:
        result = sortedlist[int(listlen / 2)]
    else:
        result = (sortedlist[int(listlen / 2) - 1] +
                  sortedlist[int(listlen / 2)]) / 2
    print("median:", result)


def do_quartile(sortedlist, listlen) -> None:
    '''It does quartile. duh'''
    if listlen % 4:
        result1 = sortedlist[int(listlen / 4)]
        result2 = sortedlist[int(listlen * 3 / 4)]
    else:
        result1 = (sortedlist[int(listlen / 4) - 1] +
                   sortedlist[int(listlen / 4)]) / 2
        result2 = (sortedlist[int(listlen * 3 / 4) - 1] +
                   sortedlist[int(listlen * 3 / 4)]) / 2

    print("quartile:", [result1, result2])


def do_std(goodargs, listsum, listlen) -> None:
    '''It does standard deviation.'''
    avg = listsum / listlen
    sumsqrt = 0
    for tosum in goodargs:
        sumsqrt += (tosum - avg) ** 2
    print("str:", (sumsqrt / listlen) ** 0.5)


def do_var(goodargs, listsum, listlen) -> None:
    '''It does variance.'''
    avg = listsum / listlen
    sumsqrt = 0
    for tosum in goodargs:
        sumsqrt += (tosum - avg) ** 2
    print("var:", sumsqrt / listlen)
