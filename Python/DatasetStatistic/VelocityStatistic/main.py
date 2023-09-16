import glob
import os
from matplotlib import pyplot as plt

def CarVelocity():

    CarVelocity={}
    CarVelArray=[]

    AugPath="E:\\Dataset\\label_aug_2\\"
    LabelPath = "E:\\Dataset\\label_2\\"
    file1 = open('C:\\Users\\Leandro\\Desktop\\Meeting\\Labels\\setD.txt', 'r')
    typeObj='Misc'
    title_splot="Velocity occurrences on " + typeObj + " class on the dataset"
    #title_splot = "Velocity occurrences on 'Car' class on Set D"


    filecount=0
    CarLabelCount=0
    Counter0Vel=0
    CounterNonZeroVel=0
    Counter1bin=0
    Counter2bin=0
    Counter3bin = 0
    Counter4bin = 0
    Counter5bin = 0
    Counter6bin = 0
    Counter7bin = 0
    Counter8bin = 0
    Counter9bin = 0
    Counter10bin = 0
    Counter11bin = 0
    Counter12bin = 0
    Counter13bin = 0
    Counter14bin = 0
    Counter15bin = 0
    Counter16bin = 0
    Counter17bin = 0
    Counter18bin = 0
    Counter19bin = 0
    Counter20bin = 0
    Counter21bin = 0
    Counter22bin = 0
    Counter23bin = 0
    Counter24bin = 0
    Counter25bin = 0
    Counter26bin = 0
    Counter27bin = 0
    Counter28bin = 0
    Counter29bin = 0
    Counter30bin = 0
    Counter31bin = 0

    SumVelocity=0
    CounterVelocity=0


    max=0

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
                    if lineval[0] == typeObj:
                        x=lineval[11]
                        y=lineval[12]
                        z=lineval[13]
                        with open(output_path_label) as fnew:
                            linecount2=0
                            for line2 in fnew:
                                linecount2= linecount2+1
                                line2val=line2.strip().split(' ')
                                if line2val[11] == x and line2val[12] == y and line2val[13] == z and line2val[0]==typeObj:
                                    CarLabelCount=CarLabelCount+1

                                    velocitykmh=float(lineval[18])*3.6 #m/s to km/h
                                    if(velocitykmh > 0):
                                        SumVelocity=SumVelocity+velocitykmh
                                        CounterVelocity=CounterVelocity+1
                                    if(velocitykmh>max):
                                        max=velocitykmh
                                    CarVelArray.append(velocitykmh)

                                    if (velocitykmh == 0):
                                        Counter0Vel = Counter0Vel + 1
                                    else:
                                        CounterNonZeroVel=CounterNonZeroVel+1

                                    if(velocitykmh >= 0 and velocitykmh <= 5):
                                        Counter1bin=Counter1bin + 1
                                    elif (velocitykmh > 5 and velocitykmh <= 10):
                                        Counter2bin = Counter2bin + 1
                                    elif (velocitykmh > 10 and velocitykmh <= 15):
                                        Counter3bin = Counter3bin + 1
                                    elif (velocitykmh > 15 and velocitykmh <= 20):
                                        Counter4bin = Counter4bin + 1
                                    elif (velocitykmh > 20 and velocitykmh <= 25):
                                        Counter5bin = Counter5bin + 1
                                    elif  (velocitykmh > 25 and velocitykmh <= 30):
                                        Counter6bin = Counter6bin + 1
                                    elif  (velocitykmh > 30 and velocitykmh <= 35):
                                        Counter7bin = Counter7bin + 1
                                    elif  (velocitykmh > 35 and velocitykmh <= 40):
                                        Counter8bin = Counter8bin + 1
                                    elif  (velocitykmh > 40 and velocitykmh <= 45):
                                        Counter9bin = Counter9bin + 1
                                    elif  (velocitykmh > 45 and velocitykmh <= 50):
                                        Counter10bin = Counter10bin + 1
                                    elif (velocitykmh > 50 and velocitykmh <= 55):
                                        Counter11bin = Counter11bin + 1
                                    elif (velocitykmh > 55 and velocitykmh <= 60):
                                        Counter12bin = Counter12bin + 1
                                    elif (velocitykmh > 60 and velocitykmh <= 65):
                                        Counter13bin = Counter13bin + 1
                                    elif (velocitykmh > 65 and velocitykmh <= 70):
                                        Counter14bin = Counter14bin + 1
                                    elif (velocitykmh > 70 and velocitykmh <= 75):
                                        Counter15bin = Counter15bin + 1
                                    elif (velocitykmh > 75 and velocitykmh <= 80):
                                        Counter16bin = Counter16bin + 1
                                    elif (velocitykmh > 80 and velocitykmh <= 85):
                                        Counter17bin = Counter17bin + 1
                                    elif (velocitykmh > 85 and velocitykmh <= 90):
                                        Counter18bin = Counter18bin + 1
                                    elif (velocitykmh > 90 and velocitykmh <= 95):
                                        Counter19bin = Counter19bin + 1
                                    elif (velocitykmh > 95 and velocitykmh <= 100):
                                        Counter20bin = Counter20bin + 1
                                    elif (velocitykmh > 100 and velocitykmh <= 105):
                                        Counter21bin = Counter21bin + 1
                                    elif (velocitykmh > 105 and velocitykmh <= 110):
                                        Counter22bin = Counter22bin + 1
                                    elif (velocitykmh > 110 and velocitykmh <= 115):
                                        Counter23bin = Counter23bin + 1
                                    elif (velocitykmh > 115 and velocitykmh <= 120):
                                        Counter24bin = Counter24bin + 1
                                    elif (velocitykmh > 120 and velocitykmh <= 125):
                                        Counter25bin = Counter25bin + 1
                                    elif (velocitykmh > 125 and velocitykmh <= 130):
                                        Counter26bin = Counter26bin + 1
                                    elif (velocitykmh > 130 and velocitykmh <= 135):
                                        Counter27bin = Counter27bin + 1
                                    elif (velocitykmh > 135 and velocitykmh <= 140):
                                        Counter28bin = Counter28bin + 1
                                    elif (velocitykmh > 140 and velocitykmh <= 145):
                                        Counter29bin = Counter29bin + 1
                                    elif (velocitykmh > 145 and velocitykmh <= 150):
                                        Counter30bin = Counter30bin + 1
                                    elif (velocitykmh > 150 and velocitykmh <= 155):
                                        Counter31bin = Counter31bin + 1
                                    else:
                                        print("MAXIMUM:::::::::"+str(velocitykmh))




                                    if CarVelocity.get(velocitykmh) != None:
                                        counter = CarVelocity.get(velocitykmh)
                                        counter = counter + 1
                                        CarVelocity[velocitykmh] = counter
                                    else:
                                        CarVelocity[velocitykmh] = 1

                    # Do Something with x and y
                except IndexError:
                    print
                    "A line in the file doesn't have enough entries."

    sortedDic= sorted(CarVelocity.items(), key=lambda x: x[1], reverse=True)
    #for key, value in sortedDic:
    #    print(key, ' : ', value)
    print("MAXIMO: " + str(max))
    # Creating histogram

    print("[0,5]: " + str(Counter1bin))
    print("]5,10]: " + str(Counter2bin))
    print("]10,15]: " + str(Counter3bin))
    print("]15,20]: " + str(Counter4bin))
    print("]20,25]: " + str(Counter5bin))
    print("]25,30]: " + str(Counter6bin))
    print("]30,35]: " + str(Counter7bin))
    print("]35,40]: " + str(Counter8bin))
    print("]40,45]: " + str(Counter9bin))
    print("]45,50]: " + str(Counter10bin))
    print("]50,55]: " + str(Counter11bin))
    print("]55,60]: " + str(Counter12bin))
    print("]60,65]: " + str(Counter13bin))
    print("]65,70]: " + str(Counter14bin))
    print("]70,75]: " + str(Counter15bin))
    print("]75,80]: " + str(Counter16bin))
    print("]80,85]: " + str(Counter17bin))
    print("]85,90]: " + str(Counter18bin))
    print("]90,95]: " + str(Counter19bin))
    print("]95,100]: " + str(Counter20bin))
    print("]100,105]: " + str(Counter21bin))
    print("]105,110]: " + str(Counter22bin))
    print("]110,115]: " + str(Counter23bin))
    print("]115,120]: " + str(Counter24bin))
    print("]120,125]: " + str(Counter25bin))
    print("]125,130]: " + str(Counter26bin))
    print("]130,135]: " + str(Counter27bin))
    print("]135,140]: " + str(Counter28bin))
    print("]140,145]: " + str(Counter29bin))
    print("]145,150]: " + str(Counter30bin))
    print("]150,155]: " + str(Counter31bin))

    print("Average speed: " + str(SumVelocity/CounterVelocity))


    print("Counter 0 velocity: " + str(Counter0Vel))
    print("Counter non-0 velocity: " + str(CounterNonZeroVel))


    fig, ax = plt.subplots(figsize=(15, 7))
    bins=[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160]
    ax.hist(CarVelArray, bins=bins,alpha=0.5, histtype='bar', ec='black')
    for c in ax.containers:
        ax.bar_label(c)
    plt.xticks(bins)
    plt.title(title_splot)
    plt.xlabel('Velocity (km/h)')
    plt.ylabel('Occurrences')
    # Show plot
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    CarVelocity()
