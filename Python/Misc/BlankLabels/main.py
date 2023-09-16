# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import glob
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    counter = 0
    for filesonpath in glob.glob("E:\\PresilOutput\\object\\label_2\\*"):
        file_name = os.path.basename(filesonpath)
        filesize = os.path.getsize(filesonpath)
        if filesize == 0:
            print("The file " + filesonpath + " is empty.")
            counter = counter + 1


    print("Counter: " + str(counter))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
