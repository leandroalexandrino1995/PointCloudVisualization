import glob
import os

if __name__ == '__main__':
    countnocar = 0
    count=0
    countVan=0
    countTruck=0
    countTram = 0
    countCyclist = 0
    countPed=0
    countPedSit=0
    countMisc=0
    count0occlusion=0
    count1occlusion = 0
    count2occlusion = 0
    count3occlusion = 0
    counteasy=0
    countmoderate=0
    counthard=0
    countnodif=0


    NFramesCar={}
    NFramesVan={}
    NFramesTruck={}

    NumberFiles=0

    file1 = open('C:\\Users\\Leandro\\Desktop\\Meeting\\Labels\\all7481.txt', 'r')
    Lines = file1.readlines()

    count = 0

    for line in Lines:
        filenumber=int(line)
        filename=line.rsplit()[0]
        file = "D:\\kittitest\\object\\training\\label_2\\" + filename + ".txt"
        print("FILE: " + file)
        NumberFiles=NumberFiles+1

        with open(file) as f:
            carflag = 0
            NCarPerFrame=0
            NVanPerFrame = 0
            NTruckPerFrame = 0

            for line in f:
                lineval = line.strip().split(' ')

                PixelCount=abs(float(lineval[7]) - float(lineval[5]))

                if (lineval[2] == '0' and float(lineval[1]) <= 0.15 and PixelCount >= 40.0 and lineval[0] == 'Car'):
                    counteasy = counteasy+1

                elif ((lineval[2] == '0' or lineval[2] == '1') and float(lineval[1]) <= 0.3 and PixelCount >= 25 and lineval[0] == 'Car'):
                    countmoderate = countmoderate+1

                elif ((lineval[2] == '0' or lineval[2] == '1' or lineval[2] == '2') and float(lineval[1]) <= 0.5 and PixelCount >= 25 and lineval[0] == 'Car'):
                    counthard = counthard+1
                else:
                    if( lineval[0] == 'Car'):
                        countnodif=countnodif+1

                if (lineval[2] == '0' and lineval[0] == 'Car'):
                    count0occlusion = count0occlusion+1

                if (lineval[2] == '1' and lineval[0] == 'Car'):
                    count1occlusion = count1occlusion+1

                if (lineval[2] == '2' and lineval[0] == 'Car'):
                    count2occlusion = count2occlusion+1

                if (lineval[2] == '3' and lineval[0] == 'Car'):
                    count3occlusion = count3occlusion+1

                if (lineval[0] == 'Car'):
                    NCarPerFrame=NCarPerFrame+1
                    carflag = 1
                    count = count + 1
                if (lineval[0] == 'Van'):
                    NVanPerFrame=NVanPerFrame+1
                    countVan = countVan + 1

                if (lineval[0] == 'Truck'):
                    NTruckPerFrame=NTruckPerFrame+1
                    countTruck = countTruck + 1

                if (lineval[0] == 'Tram'):
                    countTram = countTram + 1

                if (lineval[0] == 'Cyclist'):
                    countCyclist = countCyclist + 1

                if (lineval[0] == 'Pedestrian'):
                    countPed = countPed + 1

                if (lineval[0] == 'Person_sitting'):
                    countPedSit = countPedSit + 1

                if (lineval[0] == 'Misc'):
                    countMisc = countMisc + 1

            if (carflag == 0):
                print("No car on label " + filename)
                countnocar = countnocar + 1

            if NFramesCar.get(NCarPerFrame) != None:
                counter = NFramesCar.get(NCarPerFrame)
                counter = counter + 1
                NFramesCar[NCarPerFrame] = counter
            else:
                NFramesCar[NCarPerFrame] = 1



            if NFramesVan.get(NVanPerFrame) != None:
                counter = NFramesVan.get(NVanPerFrame)
                counter = counter + 1
                NFramesVan[NVanPerFrame] = counter
            else:
                NFramesVan[NVanPerFrame] = 1

            if NFramesTruck.get(NTruckPerFrame) != None:
                counter = NFramesTruck.get(NTruckPerFrame)
                counter = counter + 1
                NFramesTruck[NTruckPerFrame] = counter
            else:
                NFramesTruck[NTruckPerFrame] = 1


    print("Counter no cars: " + str(countnocar))
    print("Counter Car: " + str(count))
    print("Counter Van: " + str(countVan))
    print("Counter Truck: " + str(countTruck))
    print("Counter Tram: " + str(countTram))
    print("Counter Cyclist: " + str(countCyclist))
    print("Counter Pedestrian: " + str(countPed))
    print("Counter Person_sitting: " + str(countPedSit))
    print("Counter Misc: " + str(countMisc))




    print("Car on frames list: ")
    for key in sorted(NFramesCar.keys()):
        print(key, " : ", NFramesCar[key])
