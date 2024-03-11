from skimage import io
from numpy import ndarray


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
    return img
