import glob
import os
import random
import filecmp
import shutil


if __name__ == '__main__':

    totalNumberFrames=29491
    FrameCounter=15000
    Counter=0

    logfilename = "E:\\Dataset\\Shuffle_log.txt"

    listIgnore=[0,1440, 2880, 4254, 5289, 7450, 7816, 9933, 10227, 10770, 11566, 13313, 15474, 17570, 19731, 21797,
                23082, 24861, 25767, 26260, 26414, 26996, 28052, 772,]

    emptyCount = 0
    setEmpty=set()
    for i in range(0,totalNumberFrames):
        filename='%06d' % (i)
        file = "E:\\PresilOutput\\Object\\label_2\\" + filename + ".txt"
        carflag = 0
        with open(file) as f:
             for line in f:
                 lineval = line.strip().split(' ')
                 if (lineval[0] == 'Car'):
                     carflag = 1
        if(carflag==0):
             setEmpty.add(i)
             emptyCount=emptyCount + 1
             print("File without car: " + file)

    print("Number frames with no cars: " + str(emptyCount))
    print(setEmpty)

    RandomFrameSet=set()

    setCounter = 0
    while setCounter < FrameCounter:
        n = random.randint(0, totalNumberFrames - 1)
        if n not in setEmpty and n not in listIgnore and n not in RandomFrameSet:
            RandomFrameSet.add(n)
            setCounter = setCounter + 1

    shuffled_list = list(RandomFrameSet)
    print("shuffled: ")
    print(shuffled_list)
    print("Number: " + str(len(shuffled_list)))

    for i in range(0,FrameCounter):

        NewLabelfile = ""
        NewImageFile = ""
        NewCalibFile = ""
        NewLabelAugFile = ""
        NewVelIdealFile = ""
        NewVelEntityFile = ""
        NewVelVelFile = ""
        NewVelVelAbsoluteFile = ""
        NewVelZeroFile = ""

        CurLabelfile = ""
        CurImageFile = ""
        CurCalibFile = ""
        CurLabelAugFile = ""
        CurVelIdealFile = ""
        CurVelEntityFile = ""
        CurVelVelFile = ""
        CurVelVelAbsoluteFile = ""
        CurVelZeroFile = ""

        try:
            os.remove(logfilename)
        except OSError:
            f = open(logfilename, "w+")
            f.close()

        NewLabelfile = "E:\\Dataset\\label_2\\" + '%06d.txt' % (i)
        NewImageFile = "E:\\Dataset\\image_2\\" + '%06d.png' % (i)
        NewCalibFile = "E:\\Dataset\\calib\\" + '%06d.txt' % (i)
        NewLabelAugFile = "E:\\Dataset\\label_aug_2\\" + '%06d.txt' % (i)
        NewVelIdealFile = "E:\\Dataset\\velodyne_ideal\\" + '%06d.bin' % (i)
        NewVelEntityFile = "E:\\Dataset\\velodyne_entity\\" + '%06d.bin' % (i)
        NewVelVelFile = "E:\\Dataset\\velodyne_velocity\\" + '%06d.bin' % (i)
        NewVelZeroFile = "E:\\Dataset\\velodyne_zero\\" + '%06d.bin' % (i)
        NewVelVelAbsoluteFile = "E:\\Dataset\\velodyne_velocity_abs\\" + '%06d.bin' % (i)


        CurLabelfile = "E:\\PresilOutput\\Object\\label_2\\" + '%06d.txt' % (shuffled_list[i])
        CurImageFile = "E:\\PresilOutput\\Object\\image_2\\" + '%06d.png' % (shuffled_list[i])
        CurCalibFile = "E:\\PresilOutput\\Object\\calib\\" + '%06d.txt' % (shuffled_list[i])
        CurLabelAugFile = "E:\\PresilOutput\\Object\\label_aug_2\\" + '%06d.txt' % (shuffled_list[i])
        CurVelIdealFile = "E:\\PresilOutput\\Object\\velodyne_ideal\\" + '%06d.bin' % (shuffled_list[i])
        CurVelEntityFile = "E:\\PresilOutput\\Object\\velodyne_entity\\" + '%06d.bin' % (shuffled_list[i])
        CurVelVelFile = "E:\\PresilOutput\\Object\\velodyne_velocity\\" + '%06d.bin' % (shuffled_list[i])
        CurVelZeroFile = "E:\\PresilOutput\\Object\\velodyne_zero\\" + '%06d.bin' % (shuffled_list[i])
        CurVelVelAbsoluteFile = "E:\\PresilOutput\\Object\\velodyne_velocity_ideal\\" + '%06d.bin' % (shuffled_list[i])


        with open(logfilename, "a") as ShuffleLog:
             ShuffleLog.write("\n\n\n--------- Frame " + str(i) + " -----------")
             ShuffleLog.write("\nPrevious label: " + CurLabelfile + ". New: " + NewLabelfile)
             ShuffleLog.write("\nPrevious img: " + CurImageFile + ". New: " + NewImageFile)
             ShuffleLog.write("\nPrevious calib: " + CurCalibFile + ". New: " + NewCalibFile)
             ShuffleLog.write("\nPrevious labelaug: " + CurLabelAugFile + ". New: " + NewLabelAugFile)
             ShuffleLog.write("\nPrevious Ideal velodyne: " + CurVelIdealFile + ". New: " + NewVelIdealFile)
             ShuffleLog.write("\nPrevious Entity velodyne: " + CurVelEntityFile + ". New: " + NewVelEntityFile)
             ShuffleLog.write("\nPrevious velocity velodyne: " + CurVelVelFile + ". New: " + NewVelVelFile)
             ShuffleLog.write("\nPrevious abs velocity velodyne: " + CurVelVelAbsoluteFile + ". New: " + NewVelVelAbsoluteFile)
             ShuffleLog.write("\nPrevious zero velodyne: " + CurVelZeroFile + ". New: " + NewVelZeroFile)
        ShuffleLog.close()

        shutil.copy2(CurLabelfile, NewLabelfile)
        shutil.copy2(CurImageFile, NewImageFile)
        shutil.copy2(CurCalibFile, NewCalibFile)
        shutil.copy2(CurLabelAugFile, NewLabelAugFile)
        shutil.copy2(CurVelIdealFile, NewVelIdealFile)
        shutil.copy2(CurVelEntityFile, NewVelEntityFile)
        shutil.copy2(CurVelVelFile, NewVelVelFile)
        shutil.copy2(CurVelZeroFile, NewVelZeroFile)
        shutil.copy2(CurVelVelAbsoluteFile, NewVelVelAbsoluteFile)

        LabelBool=filecmp.cmp(CurLabelfile, NewLabelfile)
        ImageBool=filecmp.cmp(CurImageFile, NewImageFile)
        CalibBool=filecmp.cmp(CurCalibFile, NewCalibFile)
        AugBool=filecmp.cmp(CurLabelAugFile, NewLabelAugFile)
        VelIdealBool=filecmp.cmp(CurVelIdealFile, NewVelIdealFile)
        VelEntityBool=filecmp.cmp(CurVelEntityFile, NewVelEntityFile)
        VelVelbool=filecmp.cmp(CurVelVelFile, NewVelVelFile)
        VelZeroBool = filecmp.cmp(CurVelZeroFile, NewVelZeroFile)
        VelAbsBool=filecmp.cmp(CurVelVelAbsoluteFile, NewVelVelAbsoluteFile)
        if(LabelBool and ImageBool and CalibBool and AugBool and VelIdealBool and VelEntityBool and VelVelbool and VelZeroBool and VelAbsBool):
            print("\n" + str(i) + "/" + str(FrameCounter - 1) + " successful.")
        else:
            print("\n" + str(i) + "/" + str(FrameCounter - 1) + " failed.")


    print("DONE!")