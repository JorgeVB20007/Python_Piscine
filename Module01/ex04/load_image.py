from skimage import io
from numpy import array, ndarray


def do_avg(rgb: list) -> list:
    '''
        Gets a list of RGB values (list of lists) and replaces each list \
        with an int based on the average of the values in it.
    '''
    final = []
    for item in rgb:
        tot = 0
        num = 0
        for sum in item:
            tot += sum
            num += 1
        final.append(int(round(tot / num)))
    return (final)


def ft_load(path: str) -> ndarray:
    '''
        Gets an image from the given path and prints its shape, file
        format and a reduced list of pixels.
    '''

    filetype = path.split(".")

    assert filetype[-1].lower() in ["jpg", "jpeg"], "Unknown file type."

    try:
        img = io.imread(path)
    except (FileNotFoundError, OSError) as msg:
        assert False, msg

    print("The file format is:", filetype[-1].upper())
    print("The shape of the image is:", img.shape)
    print(img)
    return img


def zoom(img: ndarray) -> ndarray:
    '''
        Slices the given image vertically and horizontally to "zoom" it.
    '''

    total_width = img.shape[1]
    total_height = img.shape[0]

    horiz_slice = slice(int(0.445 * total_width), int(0.835 * total_width), 1)
    vert_slice = slice(int(0.13 * total_height), int(0.65 * total_height), 1)

    img = img[vert_slice]

    newimg = array([do_avg(line[horiz_slice]) for line in img])

    print("New shape after slicing:", newimg.shape)
    print(array([newimg]))

    return (newimg)
