from numpy import ndarray
import plotly.express as px


def ft_invert(array) -> ndarray:
    '''
        Inverts each pixel's color
    '''

    newarray = []

    for x in array:
        newarray.append([])
        for y in x:
            newarray[-1].append(y.copy())
            newarray[-1][-1][0] = 255 - y[0]
            newarray[-1][-1][1] = 255 - y[1]
            newarray[-1][-1][2] = 255 - y[2]

    fig = px.imshow(newarray)
    fig.show()
    return newarray


def ft_red(array) -> ndarray:
    '''
        Keeps the red values of the image and sets the rest of colors to 0.
    '''

    newarray = []

    for x in array:
        newarray.append([])
        for y in x:
            newarray[-1].append(y.copy())
            newarray[-1][-1][1] = 0
            newarray[-1][-1][2] = 0

    fig = px.imshow(newarray)
    fig.show()
    return newarray


def ft_green(array) -> ndarray:
    '''
        Keeps the green values of the image and sets the rest of colors to 0.
    '''

    newarray = []

    for x in array:
        newarray.append([])
        for y in x:
            newarray[-1].append(y.copy())
            newarray[-1][-1][0] = 0
            newarray[-1][-1][2] = 0

    fig = px.imshow(newarray)
    fig.show()
    return newarray


def ft_blue(array) -> ndarray:
    '''
        Keeps the blue values of the image and sets the rest of colors to 0.
    '''

    newarray = []

    for x in array:
        newarray.append([])
        for y in x:
            newarray[-1].append(y.copy())
            newarray[-1][-1][0] = 0
            newarray[-1][-1][1] = 0

    fig = px.imshow(newarray)
    fig.show()
    return newarray


def ft_grey(array) -> ndarray:
    '''
        Turns the image into greyscale
    '''
    newarray = []

    for x in array:
        newarray.append([])
        for y in x:
            newarray[-1].append(y.copy())
            newarray[-1][-1][0] = y[1]
            newarray[-1][-1][2] = y[1]

    fig = px.imshow(newarray)
    fig.show()
    return newarray


def next_idx(thelist: list) -> list:
    '''
        List goes [0, 1, 2] to [1, 2, 0] and [2, 0, 1] and [0, 1, 2] and
        [1, 2, 0] and [2, 0, 1] and [0, 1, 2] and [1, 2, 0] and [2, 0, 1]
        and [0, 1, 2] and [1, 2, 0] and [2, 0, 1] and [0, 1, 2] and [1, 2, 0]
        and [2, 0, 1] and [0, 1, 2] and [1, 2, 0] and [2, 0, 1] and [0, 1, 2]
        and [1, 2, 0] and [2, 0, 1] and [0, 1, 2] and [1, 2, 0].
    '''
    thelist.append(thelist[0])
    thelist.pop(0)
    return (thelist)


def ft_fake_grey(array) -> ndarray:
    '''
        Turns the image into greyscale
    '''
    newarray = []

    idxs = [0, 1, 2]
    for x in array:
        idxs = next_idx(idxs)
        newarray.append([])
        for y in x:
            avg = y[idxs[0]]
            newarray[-1].append(y.copy())
            newarray[-1][-1][0] = avg
            newarray[-1][-1][1] = avg
            newarray[-1][-1][2] = avg
            idxs = next_idx(idxs)

    fig = px.imshow(newarray)
    fig.show()
    return newarray
