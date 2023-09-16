import glob
import os

def AllFiles(AugPath,LabelPath,Outpath):
    mylabels={}
    TruckList=[]
    TruckCount=0
    TruckModel={}

    for filesonpath in glob.glob(AugPath +"*.txt"):
        file_name = os.path.basename(filesonpath)
        output_path = AugPath + file_name
        output_path_label=LabelPath + file_name
        matchlist = []
        with open(output_path) as f:
            linecountAug = 0
            for line in f:
                linecountAug= linecountAug+1
                lineval=line.strip().split(' ')
                try:
                    if mylabels.get(lineval[0]) != None:
                        counter = mylabels.get(lineval[0])
                        counter = counter+1
                        mylabels[lineval[0]] = counter
                    else:
                        mylabels[lineval[0]] = 0

                    if lineval[0] == "Truck":
                        x=lineval[11]
                        y=lineval[12]
                        z=lineval[13]
                        with open(output_path_label) as fnew:
                            linecount2=0
                            for line2 in fnew:
                                linecount2= linecount2+1
                                line2val=line2.strip().split(' ')
                                if line2val[11] == x and line2val[12] == y and line2val[13] == z and lineval[21] == "cavcade":
                                    matchlist.append(linecount2)
                                    #print("Match found: " + file_name + " Label:" + str(linecount2) + " Aug:" + str(linecountAug))

                    # Do Something with x and y
                except IndexError:
                    print
                    "A line in the file doesn't have enough entries."

        #print("Match list for file " + file_name + ": ")
        #print(matchlist)

        with open(output_path_label, 'r') as file:
            linesOverride = file.readlines()

        for i in matchlist:
            tempfile=linesOverride[i - 1].split(" ")
            linesOverride[i - 1] = "Car " + tempfile[1] + " " + tempfile[2] + " " + tempfile[3] + " " +  tempfile[4] + " " + tempfile[5] + " " + tempfile[6] + " " + tempfile[7] + " " + tempfile[8] + " " + tempfile[9] + " " + tempfile[10] + " " + tempfile[11] + " " + tempfile[12] + " " + tempfile[13] + " " + tempfile[14]

        createcopyfile=Outpath+file_name
        with open(createcopyfile, 'w') as file:
                file.writelines(linesOverride)


def TruckModels(pathlabel):
    mylabels = {}
    TruckCount = 0
    TruckModel = {}

    filepath=pathlabel + "\\*.txt"

    for filesonpath in glob.glob(filepath):
        file_name = os.path.basename(filesonpath)
        output_path = pathlabel +"\\" + file_name
        matchlist = []
        with open(output_path) as f:
            linecountAug = 0
            for line in f:
                linecountAug = linecountAug + 1
                lineval = line.strip().split(' ')
                try:
                    if mylabels.get(lineval[0]) != None:
                        counter = mylabels.get(lineval[0])
                        counter = counter + 1
                        mylabels[lineval[0]] = counter
                    else:
                        mylabels[lineval[0]] = 0

                    if lineval[0] == "Truck":
                        TruckCount=TruckCount+1
                        if TruckModel.get(lineval[21]) != None:
                            counter = TruckModel.get(lineval[21])
                            counter = counter + 1
                            TruckModel[lineval[21]] = counter
                        else:
                            TruckModel[lineval[21]] = 0
                    # Do Something with x and y
                except IndexError:
                    print
                    "A line in the file doesn't have enough entries."
    print("Truck list: ")
    for key, value in TruckModel.items():
        print(key, ' : ', value)


def CountTrucks(pathlabel):
    TruckCount = 0

    filepath=pathlabel + "\\*.txt"

    for filesonpath in glob.glob(filepath):
        file_name = os.path.basename(filesonpath)
        output_path = pathlabel +"\\" + file_name
        matchlist = []
        with open(output_path) as f:
            linecountAug = 0
            for line in f:
                lineval = line.strip().split(' ')
                try:
                    if lineval[0] == "Truck":
                        TruckCount=TruckCount+1
                    # Do Something with x and y
                except IndexError:
                    print
                    "A line in the file doesn't have enough entries."
    print("Truck count: " + str(TruckCount))


def ModelOnLabel(modelname):
    mylabels={}
    TruckCount=0

    for filesonpath in glob.glob("C:\\Users\\Leandro\\Downloads\\other\\label_aug_2\\*.txt"):
        file_name = os.path.basename(filesonpath)
        output_path = "C:\\Users\\Leandro\\Downloads\\other\\label_aug_2\\" + file_name
        output_path_label="C:\\Users\\Leandro\\Downloads\\other\\label_2\\" + file_name
        matchlist = []
        with open(output_path) as f:
            linecountAug = 0
            for line in f:
                linecountAug= linecountAug+1
                lineval=line.strip().split(' ')
                try:
                    if mylabels.get(lineval[0]) != None:
                        counter = mylabels.get(lineval[0])
                        counter = counter+1
                        mylabels[lineval[0]] = counter
                    else:
                        mylabels[lineval[0]] = 0

                    if lineval[0] == "Truck":
                        x=lineval[11]
                        y=lineval[12]
                        z=lineval[13]
                        with open(output_path_label) as fnew:
                            linecount2=0
                            for line2 in fnew:
                                linecount2= linecount2+1
                                line2val=line2.strip().split(' ')
                                if line2val[11] == x and line2val[12] == y and line2val[13] == z and lineval[21] == modelname:
                                    matchlist.append(linecount2)
                                    TruckCount=TruckCount+1
                                    #print("Match found: " + file_name + " Label:" + str(linecount2) + " Aug:" + str(linecountAug))

                    # Do Something with x and y
                except IndexError:
                    print
                    "A line in the file doesn't have enough entries."

        #if(len(matchlist) != 0):
            #print("Match list for file " + file_name + ": ")
            #print(matchlist)

    print("\nCOUNT: "+ str(TruckCount))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #CountTrucks("C:\\Users\\Leandro\\Downloads\\other\\label_2")
    AllFiles("C:\\Users\\Leandro\\Downloads\\label_aug_2\\","C:\\Users\\Leandro\\Downloads\\label_2\\","C:\\Users\\Leandro\\Downloads\\Test\\")
    #TruckModels("C:\\Users\\Leandro\\Downloads\\other\\label_aug_2")
    #CountTrucks("C:\\Users\\Leandro\\Downloads\\Test")
    #ModelOnLabel("benson")
