def callLimit(limit: int):
    '''callLimit function'''
    count = limit

    def callLimiter(function):
        '''callLimiter function'''
        def limit_function(*args: any, **kwds: any):
            '''limit_function function'''
            nonlocal function
            nonlocal count

            try:
                assert count > 0, "Error: {0} call too many times".format(
                    function)
                count -= 1
                function()
            except AssertionError as msg:
                print(msg)

        return limit_function

    return callLimiter
