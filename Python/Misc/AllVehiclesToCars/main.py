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
                                if line2val[11] == x and line2val[12] == y and line2val[13] == z and (line2val[0] == "Truck" or line2val[0] == "Motorbike" or line2val[0] == "Trailer" or line2val[0] == "Bus"):
                                    matchlist.append(linecount2)
                                    print("Match found: " + file_name + " Label:" + str(linecount2) + " Aug:" + str(linecountAug) + " LineVal: "+ line2val[0])

                    # Do Something with x and y
                except IndexError:
                    print
                    "A line in the file doesn't have enough entries."


        with open(output_path_label, 'r') as file:
            linesOverride = file.readlines()

        for i in matchlist:
            tempfile=linesOverride[i - 1].split(" ")
            linesOverride[i - 1] = "Car " + tempfile[1] + " " + tempfile[2] + " " + tempfile[3] + " " +  tempfile[4] + " " + tempfile[5] + " " + tempfile[6] + " " + tempfile[7] + " " + tempfile[8] + " " + tempfile[9] + " " + tempfile[10] + " " + tempfile[11] + " " + tempfile[12] + " " + tempfile[13] + " " + tempfile[14]

        createcopyfile=Outpath+file_name
        with open(createcopyfile, 'w') as file:
                file.writelines(linesOverride)


def UpdateLabels(LabelPath,Outpath):

    for filesonpath in glob.glob(LabelPath +"*.txt"):
        file_name = os.path.basename(filesonpath)
        label_path=LabelPath + file_name
        matchlist = []
        with open(label_path) as f:
            linecount2 = 0
            for line in f:
                linecount2=linecount2+1
                lineval=line.strip().split(' ')

                if lineval[0] == "Truck" or lineval[0] == "Motorbike" or lineval[0] == "Trailer" or lineval[0] == "Bus":
                      matchlist.append(linecount2)
                    # Do Something with x and y


        with open(label_path, 'r') as file:
            linesOverride = file.readlines()

        for i in matchlist:
            tempfile=linesOverride[i - 1].split(" ")
            linesOverride[i - 1] = "Car " + tempfile[1] + " " + tempfile[2] + " " + tempfile[3] + " " +  tempfile[4] + " " + tempfile[5] + " " + tempfile[6] + " " + tempfile[7] + " " + tempfile[8] + " " + tempfile[9] + " " + tempfile[10] + " " + tempfile[11] + " " + tempfile[12] + " " + tempfile[13] + " " + tempfile[14]

        createcopyfile=Outpath+file_name
        with open(createcopyfile, 'w') as file:
                file.writelines(linesOverride)



def TypesOfLabels():
    mylabels={}

    for filesonpath in glob.glob("C:\\Users\\Leandro\\Downloads\\Test\\*.txt"):
        file_name = os.path.basename(filesonpath)
        output_path = "C:\\Users\\Leandro\\Downloads\\Test\\" + file_name
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

                except IndexError:
                    print
                    "A line in the file doesn't have enough entries."

        #if(len(matchlist) != 0):
            #print("Match list for file " + file_name + ": ")
            #print(matchlist)

    for key, value in mylabels.items():
        print(key, ' : ', value)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #AllFiles("E:\\PresilOutput\\object_only_car\\label_aug_2\\","E:\\PresilOutput\\object_only_car\\label_2\\","C:\\Users\\Leandro\\Downloads\\Test\\")
    UpdateLabels("E:\\PresilOutput\\object_only_car\\label_2\\","C:\\Users\\Leandro\\Downloads\\Test\\")
    TypesOfLabels()
