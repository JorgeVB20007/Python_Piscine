from load_image import ft_load
import plotly.express as px
from numpy import array


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


def zoom(path: str):
    '''
        Slices the given image vertically and horizontally to "zoom" it.
    '''
    try:
        img = ft_load(path)
    except AssertionError as msg:
        print("AssertionError:", msg)
        return

    total_width = img.shape[1]
    total_height = img.shape[0]

    horiz_slice = slice(int(0.445 * total_width), int(0.835 * total_width), 1)
    vert_slice = slice(int(0.13 * total_height), int(0.65 * total_height), 1)

    img = img[vert_slice]

    newimg = array([do_avg(line[horiz_slice]) for line in img])

    print(newimg)

    print("New shape after slicing:", newimg.shape)
    print(array([newimg]))
    fig = px.imshow(newimg, binary_string=True)
    fig.show()


def main():
    zoom("animal.jpeg")


if __name__ == '__main__':
    main()
