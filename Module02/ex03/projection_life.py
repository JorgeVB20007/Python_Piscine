from load_csv import load
import matplotlib.pyplot as plt
from numpy import array


def turn2number(number: str) -> float:
    '''
        Turns a number formatted with k, M and B to an actual number.
    '''
    try:
        float(number)
        return (float(number))
    except ValueError:
        if (number[-1] == 'k'):
            return (float(number[0:-1]) * 1_000)
        elif (number[-1] == 'M'):
            return (float(number[0:-1]) * 1_000_000)
        elif (number[-1] == 'B'):
            return (float(number[0:-1]) * 1_000_000_000)
        else:
            try:
                return (float(number[0]))
            except ValueError:
                return (0.0)


def main():
    '''
        Gets the info from Spain and another country from the csv given and
        displays it in a graph.
    '''
    thefile = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    theotherfile = load("life_expectancy_years.csv")

    try:
        assert thefile is not None and theotherfile is not None, \
            "AssertionError: There was a problem with a file given"

    except AssertionError as msg:
        print(msg)
        return

    try:
        target_data_one = thefile['1900']
        target_data_two = theotherfile['1900']

        xpoints = array(list(map(turn2number, target_data_one[1:])))
        ypointsone = array(list(map(turn2number, target_data_two[1:])))

        print(len(ypointsone))
        print("\n\n")
        print(len(xpoints))

        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.title("1900")
        plt.xscale("log")
        plt.xlim(300, 11000)

        plt.gca().set_xticks([300, 1000, 10000])
        plt.gca().set_yticks(range(20, 56)[0::5])
        plt.gca().set_xticklabels(["300", "1k", "10k"])
        plt.scatter(xpoints, ypointsone, color="steelblue")
        plt.show()
    except (KeyError, ValueError) as msg:
        print(msg)
        return


if __name__ == '__main__':
    main()
