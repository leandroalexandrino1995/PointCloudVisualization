# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import glob
# Press the green button in the gutter to run the script.
import shutil

if __name__ == '__main__':
    counter = 0
    with open('F:\\bintoply\\000000.ply') as old, open('F:\\bintoply\\000120.ply', 'w') as new:
        next(old)
        next(old)
        next(old)
        next(old)
        next(old)
        next(old)
        next(old)
        next(old)
        for line in old:
            lineval=line.split(" ")
            if float(lineval[0]) <= float(75):
                new.write(line)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
