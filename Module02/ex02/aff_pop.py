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
                return (float(number))
            except ValueError:
                return (0.0)


def main():
    '''
        Gets the info from Spain and another country from the csv given and
        displays it in a graph.
    '''
    thefile = load("population_total.csv")

    try:
        assert thefile is not None, "AssertionError: There was a problem \
with the file given"
    except AssertionError as msg:
        print(msg)
        return

    countryone = "Spain"
    countrytwo = "South Korea"

    try:
        target_data_one = thefile[thefile['country'] == countryone].iloc[0]
        target_data_two = thefile[thefile['country'] == countrytwo].iloc[0]

        xpoints = array(range(1800, 2051))
        ypointsone = array(list(map(turn2number, target_data_one[1:252])))
        ypointstwo = array(list(map(turn2number, target_data_two[1:252])))

        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.title("Population Projections")

        plt.gca().set_xticks(range(1800, 2041)[0::40])
        plt.gca().set_yticks([20_000_000, 40_000_000, 60_000_000])
        plt.gca().set_yticklabels(["20M", "40M", "60M"])
        plt.plot(xpoints, ypointsone, color="steelblue", label=countryone)
        plt.plot(xpoints, ypointstwo, color="green", label=countrytwo)
        plt.legend(loc='lower right')
        plt.show()
    except (KeyError, ValueError, IndexError) as msg:
        print(msg)
        return


if __name__ == '__main__':
    main()
