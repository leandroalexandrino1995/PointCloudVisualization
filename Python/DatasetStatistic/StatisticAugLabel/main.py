import glob
import os

def AllFiles():
    CarModel={}

    AugPath="F:\\Split\\training\\label_aug_2\\"
    LabelPath = "F:\\Split\\training\\label_2\\"

    filecount=0
    CarLabelCount=0

    file1 = open('C:\\Users\\Leandro\\Desktop\\Tese\\scripts\\valsplit.txt', 'r')
    Lines = file1.readlines()
    # Strips the newline character
    for line in Lines:
        filenumber = int(line)
        filename = line.rsplit()[0]
        output_path = AugPath + filename + ".txt"
        output_path_label=LabelPath + filename + ".txt"
        print("File: " + filename + ".txt")
        with open(output_path) as f:
            filecount=filecount+1
            for line in f:
                lineval=line.strip().split(' ')
                try:
                    if lineval[0] == "Car":
                        x=lineval[11]
                        y=lineval[12]
                        z=lineval[13]
                        with open(output_path_label) as fnew:
                            linecount2=0
                            for line2 in fnew:
                                linecount2= linecount2+1
                                line2val=line2.strip().split(' ')
                                if line2val[11] == x and line2val[12] == y and line2val[13] == z and line2val[0]=='Car':
                                    CarLabelCount=CarLabelCount+1
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
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    AllFiles()
