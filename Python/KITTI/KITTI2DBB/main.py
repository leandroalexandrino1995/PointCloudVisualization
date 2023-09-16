
import glob
import os
import cv2

def AllImagesWithTreshold():
    minTresh = 1
    maxTresh = 2

    labelinit = "F:\\PresilOutput\\Object\\label_2\\"
    imginit = "F:\\PresilOutput\\Object\\image_2\\"


    for filesonpath in glob.glob("F:\\PresilOutput\\Object\\label_2\\*.txt"):
        file_name = os.path.basename(filesonpath)
        filesplit = file_name.split(".")
        filenumber = filesplit[0]
        print("Label: " + str(filenumber))
        labelpath = labelinit + filenumber + ".txt"
        imgpath = imginit + filenumber + ".png"
        img = cv2.imread(imgpath)
        print("File: " + file_name)

        result = img.copy()

        with open(labelpath) as f:
            checkflag = 0
            for line in f:
                lineval = line.strip().split(' ')
                if (float(lineval[2])>minTresh and float(lineval[2])<=maxTresh) and (lineval[0]=='Car'):
                    checkflag = 1
                    min_x = int(float(lineval[4]))
                    max_x = int(float(lineval[6]))
                    min_y = int(float(lineval[5]))
                    max_y = int(float(lineval[7]))
                    cv2.rectangle(result, (min_x, min_y), (max_x, max_y), (0, 255, 0), 1)  # add rectangle to image
                    cv2.putText(result, lineval[2], (min_x, min_y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
        if (checkflag):
            winname = 'image %d' % (int(filenumber))
            cv2.namedWindow(winname)  # Create a named window
            cv2.moveWindow(winname, 10, 10)  # Move it to (40,30)
            cv2.imshow(winname, img)
            cv2.imshow(winname, result)
            while 1:
                if cv2.waitKey(0) != ord('q'):
                    break
                else:
                    exit()
            cv2.destroyAllWindows()

def DrawBB():

    imginit = "F:\\Split\\training\\image_2\\"

    filenumber = "003611"

    coorList=[1099,547,1151,566]

    imgpath = imginit + filenumber + ".png"
    img = cv2.imread(imgpath)

    result = img.copy()

    min_x = int(float(coorList[0]))
    max_x = int(float(coorList[1]))
    min_y = int(float(coorList[2]))
    max_y = int(float(coorList[3]))
    cv2.rectangle(result, (min_x, min_y), (max_x, max_y), (0, 255, 0), 1)  # add rectangle to image
    cv2.putText(result, "0", (min_x, min_y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)


    cv2.imshow('image %d' % (int(filenumber)), result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def main():
    AllImagesWithTreshold()
    #DrawBB()

if __name__ == "__main__":
    main()
