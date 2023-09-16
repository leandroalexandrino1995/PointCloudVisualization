

from csv import reader
# open file in read mode

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file1 = open('C:\\Users\\Leandro\\Desktop\\Meeting\\Labels\\setD.txt', 'r')
    file2 = open('C:\\Users\\Leandro\\Desktop\\Meeting\\Labels\\setB.txt', 'r')
    file1_list=list()
    file2_list = list()

    for line1 in file1:
        file1_list.append(line1)

    for line2 in file2:
        file2_list.append(line2)



    print(set(file1_list).intersection(file2_list))