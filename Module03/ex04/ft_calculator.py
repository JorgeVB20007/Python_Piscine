class calculator:
    '''It's a calculator which is in a class.'''
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        '''Prints the dot product of two vectors'''
        try:
            piz = zip(V1, V2)
            thesum = 0
            for one, two in piz:
                thesum += one * two
            print(thesum)

        except Exception as msg:
            print(msg)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        '''Sums two vectors and prints the resulting vector'''
        result = []
        try:
            piz = zip(V1, V2)
            for one, two in piz:
                result.append(one + two)
            print(result)

        except Exception as msg:
            print(msg)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        '''Substracts two vectors and prints the resulting vector'''
        result = []
        try:
            piz = zip(V1, V2)
            for one, two in piz:
                result.append(one - two)
            print(result)

        except Exception as msg:
            print(msg)
