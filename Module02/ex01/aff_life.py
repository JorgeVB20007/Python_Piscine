from load_csv import load
import matplotlib.pyplot as plt
from numpy import array


def main():
    '''
        Gets the info from Spain from the csv given and displays it in a graph.
    '''
    thefile = load("life_expectancy_years.csv")

    try:
        assert thefile is not None, "AssertionError: There was a problem \
with the file given"
    except AssertionError as msg:
        print(msg)
        return

    country = "Spain"

    try:
        target_data = thefile[thefile['country'] == country].iloc[0]

        xpoints = array(range(1790, 2091))
        ypoints = array(target_data[1:])

        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.title(country + "'s Life expectancy Projections")
        plt.gca().set_xticks(range(1800, 2081)[0::40])
        plt.plot(xpoints, ypoints, color="steelblue")
        plt.show()
    except (KeyError, ValueError) as msg:
        print(msg)
        return


if __name__ == '__main__':
    main()
