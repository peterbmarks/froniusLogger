"""
Simple code to draw a graph of a day of power.
Requires matplotlib

On Fedora Linux: sudo dnf install python3-matplotlib

"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv
import time
import datetime

today = time.strftime("%Y_%m_%d")

INFILENAME = today + '.csv'


def main():
    data_reader = csv.reader(open(INFILENAME,'r'), delimiter='\t')
    y = []
    x = []
    for row in data_reader:
        if len(row) > 1:
            timeval = row[0]

            dt = datetime.datetime.strptime(timeval, "%H:%M:%S")
            print("timeval = %s -> %s" % (timeval, dt))
            x.append(mdates.date2num(dt))
            watts = float(row[1])
            y.append(watts)

    fig, ax = plt.subplots()
    ax.plot(x,y)
    ax.xaxis_date()
    my_fmt = mdates.DateFormatter('%H:%M')
    ax.xaxis.set_major_formatter(my_fmt)
    plt.ylabel("Watts")
    plt.xlabel("Time")
    plt.show()
    plt.savefig('%s_graph' % today)


if __name__ == "__main__":
    main()
