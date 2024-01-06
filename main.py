import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates, patches
import matplotlib as mpl

import glob
import re

font = {'family': 'normal',
        'weight': 'bold',
        'size': 8}
plt.rc('font', **font)

def parseFile():
    arrivals = []
    lags = []
    yes = 0

    file1 = open('250ms.log', 'r')
    Lines = file1.readlines()
    for line in Lines:
        arrivalstring = re.search('arrival: (\d+)', line)
        if arrivalstring != None:
            arrival = re.findall('\d+', arrivalstring.group())[0]
            print(arrival)
            if (yes==0):
             arrivals.append(float(arrival))
        lagstring = re.search('total lag (\d+)', line)
        if lagstring != None:
            lag = re.findall('\d+', lagstring.group())[0]
            print(lag)
            if (yes == 0):
                lags.append(float(lag))
            #yes = (yes + 1) % 2

    fig, ax = plt.subplots()
    plt.xticks(rotation=45, ha='right')

    ax.set_xlabel("Time (sec)", **font)
    ax.set_ylabel("latency (ms)", **font)
    ax.plot(arrivals)
    ax.plot(lags)


    plt.show()

    print(arrivals)
    print(lags)

def parseFileLag():
    arrivals = []
    lags = []
    yes = 0

    file1 = open('expc.log', 'r')
    Lines = file1.readlines()
    for line in Lines:
        # arrivalstring = re.search('arrival: (\d+)', line)
        # if arrivalstring != None:
        #     arrival = re.findall('\d+', arrivalstring.group())[0]
        #     print(arrival)
        #     if (yes==0):
        #      arrivals.append(float(arrival))
        lagstring = re.search('total lag (\d+)', line)
        if lagstring != None:
            lag = re.findall('\d+', lagstring.group())[0]
            print(lag)
            if (yes == 0):
                lags.append(float(lag))
            #yes = (yes + 1) % 2

    fig, ax = plt.subplots()
    plt.xticks(rotation=45, ha='right')

    ax.set_xlabel("Time (sec)", **font)
    ax.set_ylabel("lag", **font)
    ax.plot(arrivals)
    ax.plot(lags)

    plt.show()

    print(arrivals)
    print(lags)













if __name__ == '__main__':

    #parseFile()

    parseFileLag()


