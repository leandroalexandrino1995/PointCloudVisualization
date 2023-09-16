import glob
import os
import numpy as np

def AllFiles():
    CarModel={}
    LabelSet=set()
    AugPath="F:\\TestingAll\\label_aug_2\\"
    LabelPath = "F:\\TestingAll\\label_2\\"

    testlist=[]
    setLabels=set()
    augLabelSet=set()
    filecount=0
    CarLabelCount=0
    CounterUnknown=0

    for filesonpath in glob.glob(LabelPath + "*.txt"):
        file_name = os.path.basename(filesonpath)
        filesplit = file_name.split(".")
        filenumber = filesplit[0]
        output_path = AugPath + filenumber + ".txt"
        output_path_label=LabelPath + filenumber + ".txt"
        print("File: " + filenumber + ".txt")
        with open(output_path) as f:
            filecount=filecount+1
            for line in f:
                lineval=line.strip().split(' ')
                try:
                    LabelSet.add(lineval[0])
                    if lineval[0] == "UNK":
                        CounterUnknown=CounterUnknown+1
                        testlist.append(filenumber)
                        augLabelSet.add(lineval[21])
                        x=lineval[11]
                        y=lineval[12]
                        z=lineval[13]
                        with open(output_path_label) as fnew:
                            linecount2=0
                            for line2 in fnew:
                                linecount2= linecount2+1
                                line2val=line2.strip().split(' ')
                                if line2val[11] == x and line2val[12] == y and line2val[13] == z and (lineval[21]=='UNK'):
                                    CarLabelCount=CarLabelCount+1
                                    setLabels.add(str(filenumber))
                                    if CarModel.get(lineval[21]) != None:
                                        counter = CarModel.get(lineval[21])
                                        counter = counter + 1
                                        CarModel[lineval[21]] = counter
                                    else:
                                        CarModel[lineval[21]] = 1

                    # Do Something with x and y
                except IndexError:
                    print
                    "A line in the file doesn't have enough entries."

    print("Car list: ")

    sortedDic= sorted(CarModel.items(), key=lambda x: x[1], reverse=True)

    numberCars=0
    for key, value in sortedDic:
        print(key, ' : ', value)
        numberCars=numberCars+value

    print("Number of files: " + str(filecount))
    print("Number of cars: " + str(numberCars))
    print("Number of cars label: " + str(CarLabelCount))

    print("Frames set: ")
    orderLabel=sorted(LabelSet)
    print(orderLabel)
    print("On frames: ")
    print(setLabels)
    print("UKN on frame: ")
    for i in range(len(testlist)):
        print(testlist[i])
    print("Aug label UNK:")
    print(augLabelSet)
    print("TESTE: ")
    print(CounterUnknown)
# Press the green button in the gutter to run the script.


def NonZeroIntensity():
    binpath="F:\\PresilOutput\\object\\velodyne\\"

    fileSet=set()
    entitySet = set()

    for filesonpath in glob.glob(binpath + "*.bin"):
        file_name = os.path.basename(filesonpath)
        filesplit = file_name.split(".")
        filenumber = filesplit[0]
        if(int(filenumber) < 1598):
            output_path = binpath + filenumber + ".bin"
            print("File: " + filenumber)
            with open(output_path,'r') as f:
                points = np.fromfile(output_path, dtype=np.float32).reshape(-1, 4)
                points = points[:, :4]  # exclude luminance

                point_tuple_list = []
                for i in range(len(points)):
                    point_tuple_list.append((points[i][0], points[i][1], points[i][2],points[i][3]))
                    if(points[i][3] > 0.0):
                        fileSet.add(str(filenumber))
                    if(points[i][3] >= 2.0):
                        entitySet.add(str(points[i][3]))

    print("Files: ")
    print(fileSet)
    s=sorted(entitySet)
    print(s)

def LabelValColumn():
    LabelSet = set()
    AugPath = "F:\\PresilOutput\\object\\label_aug_2\\"
    LabelPath = "F:\\PresilOutput\\object\\label_2\\"

    testlist = []
    filecount = 0

    for filesonpath in glob.glob(LabelPath + "*.txt"):
        file_name = os.path.basename(filesonpath)
        filesplit = file_name.split(".")
        filenumber = filesplit[0]
        output_path = AugPath + filenumber + ".txt"
        output_path_label = LabelPath + filenumber + ".txt"
        #print("File: " + filenumber + ".txt")
        with open(output_path) as f:
            filecount = filecount + 1
            for line in f:
                lineval = line.strip().split(' ')
                try:
                    LabelSet.add(lineval[0])
                    x = lineval[11]
                    y = lineval[12]
                    z = lineval[13]
                    with open(output_path_label) as fnew:
                        linecount2 = 0
                        for line2 in fnew:
                            linecount2 = linecount2 + 1
                            line2val = line2.strip().split(' ')
                            if line2val[11] == x and line2val[12] == y and line2val[13] == z and (
                                lineval[29] != '0'):
                                testlist.append(filenumber)
                                min_x = int(float(lineval[4]))
                                max_x = int(float(lineval[6]))
                                min_y = int(float(lineval[5]))
                                max_y = int(float(lineval[7]))
                                print("Frame: " + filenumber + ".")
                                print("Trailer attached: " + lineval[29])
                                print("Trailer entity: " + lineval[30])
                                print(str(min_x) + "," + str(max_x) + "," + str(min_y) + "," + str(max_y))
                                print("\n")



                    # Do Something with x and y
                except IndexError:
                    print
                    "A line in the file doesn't have enough entries."

    listsort=sorted(testlist)
    print("LISTA: ")
    print(listsort)
if __name__ == '__main__':
    #NonZeroIntensity()
    #LabelValColumn()
    AllFiles()