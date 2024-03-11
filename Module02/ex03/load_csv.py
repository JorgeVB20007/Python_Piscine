from pandas import DataFrame, read_csv, errors


def load(path: str) -> DataFrame:
    '''
        Loads a csv file and prints its dimensions.
    '''
    try:
        read = read_csv(path)
    except (FileNotFoundError, errors.EmptyDataError, PermissionError,
            IsADirectoryError, ValueError, TypeError) as msg:
        print("Error:", msg)
        return None
    print("Loading dataset of dimensions", read.shape)
    return read
