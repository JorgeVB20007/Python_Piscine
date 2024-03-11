from load_image import ft_load, zoom
import plotly.express as px
from numpy import array, ndarray


def rotate(img: ndarray) -> ndarray:
    '''
        Transposes the image, simulating a rotation.
    '''

    newimg = [[img[y][x] for y in range(len(img))] for x in range(len(img[0]))]

    return (array(newimg))


def main():
    '''
        Loads the image, zooms it, makes it greyscale and transposes the
        image, simulating a rotation.
    '''
    try:
        img = ft_load("animal.jpeg")
    except AssertionError as msg:
        print(msg)
        return
    img = zoom(img)
    img = rotate(img)
    fig = px.imshow(img, binary_string=True)
    fig.show()


if __name__ == '__main__':
    main()
