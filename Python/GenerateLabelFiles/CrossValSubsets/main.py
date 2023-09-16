import random
import shutil



def GenerateSplit():
    totalNumberFrames = 15000
    Number_folds = 4
    frames_per_subset = int(15000 / Number_folds)

    setA = set()
    setB = set()
    setC = set()
    setD = set()

    setCounter = 0

    # Create subset A
    while setCounter < frames_per_subset:
        n = random.randint(0, totalNumberFrames-1)
        if n not in setA:
            setA.add(n)
            setCounter = setCounter + 1


    setCounter = 0
    # Create subset B
    while setCounter < frames_per_subset:
        n = random.randint(0, totalNumberFrames-1)
        if n not in setB and n not in setA:
            setB.add(n)
            setCounter = setCounter + 1

    setCounter = 0
    # Create subset C
    while setCounter < frames_per_subset:
        n = random.randint(0, totalNumberFrames-1)
        if n not in setC and n not in setA and n not in setB:
            setC.add(n)
            setCounter = setCounter + 1

    setCounter = 0
    # Create subset D
    while setCounter < frames_per_subset:
        n = random.randint(0, totalNumberFrames-1)
        if n not in setD and n not in setA and n not in setB and n not in setC:
            setD.add(n)
            setCounter = setCounter + 1

    setA = sorted(setA)
    setB = sorted(setB)
    setC = sorted(setC)
    setD = sorted(setD)

    print(setA)
    print(setB)
    print(setC)
    print(setD)

    setBCD=set()
    setBCD.update(setB)
    setBCD.update(setC)
    setBCD.update(setD)

    setACD=set()
    setACD.update(setA)
    setACD.update(setC)
    setACD.update(setD)

    setABD=set()
    setABD.update(setA)
    setABD.update(setB)
    setABD.update(setD)

    setABC = set()
    setABC.update(setA)
    setABC.update(setB)
    setABC.update(setC)


    # --------------------- TRAIN B,C,D TEST A ---------------------
    with open("C:\\Users\\Leandro\\Desktop\\Meeting\\Labels\\TestA\\train.txt", "w+") as f:
        for OtherFrame in setBCD:
            f.write('%06d\n' % (OtherFrame))

    with open("C:\\Users\\Leandro\\Desktop\\Meeting\\Labels\\TestA\\val.txt", "w+") as f:
        for Aelement in setA:
            f.write('%06d\n' % (Aelement))


    # --------------------- TRAIN A,C,D TEST B ---------------------
    with open("C:\\Users\\Leandro\\Desktop\\Meeting\\Labels\\TestB\\train.txt", "w+") as f:
        for OtherFrame in setACD:
            f.write('%06d\n' % (OtherFrame))

    with open("C:\\Users\\Leandro\\Desktop\\Meeting\\Labels\\TestB\\val.txt", "w+") as f:
        for Belement in setB:
            f.write('%06d\n' % (Belement))


    # --------------------- TRAIN A,B,D TEST C ---------------------
    with open("C:\\Users\\Leandro\\Desktop\\Meeting\\Labels\\TestC\\train.txt", "w+") as f:
        for OtherFrame in setABD:
            f.write('%06d\n' % (OtherFrame))

    with open("C:\\Users\\Leandro\\Desktop\\Meeting\\Labels\\TestC\\val.txt", "w+") as f:
        for Celement in setC:
            f.write('%06d\n' % (Celement))

    # --------------------- TRAIN A,B,C TEST D ---------------------
    with open("C:\\Users\\Leandro\\Desktop\\Meeting\\Labels\\TestD\\train.txt", "w+") as f:
        for OtherFrame in setABC:
            f.write('%06d\n' % (OtherFrame))

    with open("C:\\Users\\Leandro\\Desktop\\Meeting\\Labels\\TestD\\val.txt", "w+") as f:
        for Delement in setD:
            f.write('%06d\n' % (Delement))

    with open("C:\\Users\\Leandro\\Desktop\\Meeting\\Labels\\setA.txt", "w+") as f:
        for Aelement in setA:
            f.write('%06d\n' % (Aelement))

    with open("C:\\Users\\Leandro\\Desktop\\Meeting\\Labels\\setB.txt", "w+") as f:
        for Belement in setB:
            f.write('%06d\n' % (Belement))

    with open("C:\\Users\\Leandro\\Desktop\\Meeting\\Labels\\setC.txt", "w+") as f:
        for Celement in setC:
            f.write('%06d\n' % (Celement))

    with open("C:\\Users\\Leandro\\Desktop\\Meeting\\Labels\\setD.txt", "w+") as f:
        for Delement in setD:
            f.write('%06d\n' % (Delement))


def GenerateSplit12to3():
    totalNumberFrames = 15000
    training_frames=11250
    testing_frames=3750


    setCounter = 0

    set3000=set()
    set12000=set()

    print("\n\n\n SPLIT")
    # Create subset A
    while setCounter < training_frames:
        n = random.randint(0, totalNumberFrames-1)
        if n not in set12000:
            set12000.add(n)
            setCounter = setCounter + 1


    setCounter = 0
    # Create subset B
    while setCounter < testing_frames:
        n = random.randint(0, totalNumberFrames-1)
        if n not in set3000 and n not in set12000:
            set3000.add(n)
            setCounter = setCounter + 1



    setA = sorted(set12000)
    setB = sorted(set3000)
    # fileTest="test.txt"
    # fileTrain = "train.txt"
    # fileValidation = "val.txt"

    print(setA)
    print(setB)

    # --------------------- 12K training, 3k testing ---------------------
    with open("C:\\Users\\Leandro\\Desktop\\train.txt", "w+") as f:
        for Aelement in setA:
            f.write('%06d\n' % (Aelement))

    with open("C:\\Users\\Leandro\\Desktop\\val.txt", "w+") as f:
        for Belement in setB:
            f.write('%06d\n' % (Belement))




def VerificationLabels():
    with open('C:\\Users\\Leandro\\Desktop\\NextMeeting\\GTACrossLabels\\TrainATestB\\train.txt', 'r') as read1:
        f1 = read1.read().split()

    with open('C:\\Users\\Leandro\\Desktop\\NextMeeting\\GTACrossLabels\\TrainATestB\\val.txt', 'r') as read2:
        f2 = read2.read().split()

    for line in f2:
        if line in f1:
            print("EQUAL!")


def GenerateSplit15():
    totalNumberFrames = 15000

    setCounter = 0
    set15000=set()

    # Create subset A
    while setCounter < totalNumberFrames:
        n = random.randint(0, totalNumberFrames-1)
        if n not in set15000:
            set15000.add(n)
            setCounter = setCounter + 1




    setA = sorted(set15000)
    # fileTest="test.txt"
    # fileTrain = "train.txt"
    # fileValidation = "val.txt"

    print(setA)

    # --------------------- 12K training, 3k testing ---------------------
    with open("C:\\Users\\Leandro\\Desktop\\teste.txt", "w+") as f:
        for Aelement in setA:
            f.write('%06d\n' % (Aelement))





def LabelsOutput():
    file1 = open('C:\\Users\\Leandro\\Desktop\\Tese\\scripts\\valsplit.txt', 'r')
    gt_path="D:\\kittitest\\object\\training\\label_2\\"
    out_path = "D:\\kittitest\\eval\\gt\\"
    Lines = file1.readlines()
    # Strips the newline character
    for line in Lines:
        file_name='%06d' % (int(line))
        label_file=gt_path + file_name + ".txt"
        output_label=out_path + file_name + ".txt"

        print("Moving " + label_file + " to: " + output_label)

        shutil.copyfile(label_file, output_label)




def main():
    #GenerateSplit()
    #GenerateSplit12to3()
    #GenerateSplit15()
    #VerificationLabels()
    #LabelsOutput()
    GenerateSplit15()


if __name__ == "__main__":
    main()
