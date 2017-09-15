"""
Logs key data from a Fronius inverter to a CSV file for later analysis.
peter.marks@pobox.com
"""

import requests
import json
import datetime
import time

# Set this to the IP address of your inverter
host = "192.168.0.112"
sample_seconds = 60  # how many seconds between samples, set to zero to run once and exit


def main():
    print("started")
    while True:
        try:
            watts = watts_generated()
            now = time.strftime("%H:%M:%S")
            line = "%s\t%s\n" % (now, watts)
            # print(line)
            write_to_logfile(line)
        except requests.exceptions.ConnectTimeout:
            print("Connect timeout")
        if sample_seconds > 0:
            time.sleep(sample_seconds)
        else:
            return


def write_to_logfile(line):
    today = time.strftime("%Y_%m_%d")
    file_name = today + ".csv"
    out_file = open(file_name, "a")
    out_file.write(line)
    out_file.close()


def watts_generated():
    url = "http://" + host + "/solar_api/v1/GetInverterRealtimeData.cgi?Scope=System"
    r = requests.get(url, timeout=2)
    json_data = r.json()
    result = json_data["Body"]["Data"]["PAC"]["Values"]["1"]
    return result


if __name__ == "__main__":
    main()
