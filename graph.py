"""
Simple code to draw a graph of a day of power.
Requires matplotlib

On Fedora Linux: sudo dnf install python3-matplotlib

"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv
import time

today = time.strftime("%Y_%m_%d")

INFILENAME = today + '.csv'


def main():
    datareader = csv.reader(open(INFILENAME,'r'), delimiter='\t')
    y = []
    x = []
    xlabels = []
    counter = 0
    for row in datareader:
        if len(row) > 1:
            timeval = row[0]
            print("timeval = %s" % timeval)
            xlabels.append(timeval)
            x.append(counter)
            counter += 1
            watts = float(row[1])
            y.append(watts)

    plt.plot(y)
    plt.xticks(x, xlabels, rotation=30)
    plt.ylabel('Watt')
    plt.show()
    plt.savefig('%s_graph' % today)


if __name__ == "__main__":
    main()
