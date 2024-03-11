
def ft_filter(funct: any, iterable: any) -> object:
    '''
        ft_filter(function or None, iterable) --> filter object

        Return an iterator yielding those items of iterable for which
        function(item) is true. If function is None, return the items
        that are true.
    '''
    if funct is None:
        results = (item for item in iterable if item is not False)
    else:
        results = (item for item in iterable if funct(item))
    return (results)
