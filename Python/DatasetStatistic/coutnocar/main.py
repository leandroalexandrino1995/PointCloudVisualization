import glob
import os

if __name__ == '__main__':
    countnocar = 0
    count=0
    countreplacnocar=0
    LabelSet=set()
    lstReplace=[]
    lstNewItem=[]
    for filesonpath in glob.glob("D:\kittitest\object\training\\label_2\\*.txt"):
        file_name = os.path.basename(filesonpath)
        if (file_name <= str("050000.txt")):
            file = "F:\\Split\\training\\label_2\\" + file_name

            with open(file) as f:
                carflag = 0
                for line in f:
                    lineval = line.strip().split(' ')
                    LabelSet.add(lineval[0])
                    if (lineval[0] == 'Unknown'):
                        carflag = 1
                        count = count + 1
                        print("file_name: " + file_name)
                if (carflag == 0):
                    #print("No car on label " + file_name)
                    countnocar = countnocar + 1
                    lstReplace.append(file_name)


    print("Counter no cars: " + str(countnocar))
    print("Counter cars: " + str(count))
    print("Labels: ")
    print(LabelSet)