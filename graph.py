"""
Simple code to draw a graph of a day of power.
Requires matplotlib

On Fedora Linux: sudo dnf install python3-matplotlib

Usage: python3 graph.py [csv file name]
If you don't give the file name it will use today's

"""

import csv
import time
import datetime
import sys
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def main():
    date_base = time.strftime("%Y_%m_%d")
    if len(sys.argv) > 1:
        date_base = os.path.splitext(sys.argv[1])[0]
    in_file_name = date_base + ".csv"
    data_reader = csv.reader(open(in_file_name,'r'), delimiter='\t')
    y = []
    x = []
    max_watts = 0.0
    for row in data_reader:
        if len(row) > 1:
            timeval = row[0]

            dt = datetime.datetime.strptime(timeval, "%H:%M:%S")
            x.append(mdates.date2num(dt))
            watts = float(row[1])
            y.append(watts)
            if watts > max_watts:
                max_watts = watts

    fig, ax = plt.subplots()
    ax.plot(x,y)
    ax.xaxis_date()
    my_fmt = mdates.DateFormatter('%H:%M')
    ax.xaxis.set_major_formatter(my_fmt)

    title_date = time.strftime("%d-%b-%Y")
    plt.title("Solar generation on %s" % title_date)
    plt.ylabel("Watts")
    plt.xlabel("Time")

    text_x = datetime.datetime.strptime("06:00", "%H:%M")
    text_y = max_watts
    plt.text(text_x, text_y, "Max: %dW" % max_watts)
    plt.show()
    print("writing: %s" % date_base)
    plt.savefig('%s_graph' % date_base)


if __name__ == "__main__":
    main()
