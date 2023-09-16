

from csv import reader
# open file in read mode

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lstRows=[]
    with open('C:\\Users\\Leandro\\Desktop\\Presil\\DeepGTAV-PreSIL-master\\ObjectDet\\vehicle_labels.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj, delimiter=",")
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            lstRows.append(row[0])

    print((lstRows))
    with open('C:\\Users\\Leandro\\Desktop\\Presil\\DeepGTAV-PreSIL-master\\ObjectDet\\vehicle_labels_org.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj, delimiter=",")
        # Iterate over each row in the csv using reader object
        count = 0
        misscount=0
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            if(row[0] == lstRows[count]):
                print("Row: " + str(count) + " Match: " + row[0])
            else:
                print("Row: " + str(count) + " Missing: " + row[0])
                misscount=misscount+1

            count=count+1
    print("Failed label counter: " + str(misscount))