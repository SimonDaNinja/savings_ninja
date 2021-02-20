#! /usr/bin/python3

import os
import matplotlib.pyplot as plt
import numpy as np

def getRootDirectory():
    return os.path.dirname(os.path.abspath(__file__))

def getAccountDirectory():
    return "/".join([getRootDirectory(), "accounts"])

def getAccountPath(account):
    return "/".join([getAccountDirectory(), account])

def getMonthValueArraysForAccount(account):
    accountPath = getAccountPath(account)
    lines = open(accountPath, 'r').read().split('\n')
    while '' in lines:
        lines.remove('')
    firstMonth = int(lines.pop(0))
    values = np.array([float(i) for i in lines])
    months = np.array([i for i in range(firstMonth, firstMonth + len(values))])
    return values, months

if __name__ == "__main__":

    accounts = os.listdir(getAccountDirectory())

    for account in accounts:
        values, months = getMonthValueArraysForAccount(account)
        plt.plot(months, values, label = account)

    plt.legend()
    plt.show()
