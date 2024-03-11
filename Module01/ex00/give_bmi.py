from numpy import column_stack


def give_bmi(height: list[int | float], weight: list[int | float])\
 -> list[int | float]:
    '''
        Returns the BMI of a series of people with the function
        BMI = weight / (height ^2).
    '''
    try:
        assert height is not None and weight is not None, \
            "AssertionError: Wrong type"
    except AssertionError as msg:
        print(msg)
        return None

    all_bmis = []
    try:
        table = column_stack((height, weight))
    except ValueError as msg:
        print("ValueError:", msg)
        return None

    try:
        for item in table:
            if (item[0] == 0):
                all_bmis.append(float("NaN"))
            else:
                all_bmis.append(item[1] / (item[0] ** 2))
    except TypeError as msg:
        print("TypeError:", msg)

    return all_bmis


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
        Creates a list with the results of the comparison between a list of
        BMIs and the limit.
    '''
    all_limits = []

    try:
        assert bmi is not None and limit is not None, \
            "AssertionError: Wrong type"
    except AssertionError as msg:
        print(msg)
        return None

    for item in bmi:
        if item > limit:
            all_limits.append(True)
        else:
            all_limits.append(False)

    return all_limits
