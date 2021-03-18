import os
import csv

os.chdir('E:/Hackrush/Processed_Individual_Datasets/Train')


frequency1 = open("frequency1.csv",'a')
csv_writer1 = csv.writer(frequency1)
frequency2 = open("frequency2.csv",'a')
csv_writer2 = csv.writer(frequency2)
frequency3 = open("frequency3.csv",'a')
csv_writer3 = csv.writer(frequency3)
frequency4 = open("frequency4.csv",'a')
csv_writer4 = csv.writer(frequency4)
frequency5 = open("frequency5.csv",'a')
csv_writer5 = csv.writer(frequency5)

               
for fileNum in range (1,10440):
    with open("Processed_IN_Data_"+str(fileNum)+".csv",'r') as input_csv:
        input_csv_reader = csv.reader(input_csv)
        digitsFile = open("IN_Digit_Dataset_train.csv",'r')
        digList = digitsFile.readlines()
        digString = digList[fileNum].split(',')[1]
        x = 1
        for line in input_csv_reader:
            # line.insert(0,',')
            line.insert(0,digString+',')
            print(x)
            if x==1:
                csv_writer1.writerow(line)
                x=2  
            elif x==2:
                csv_writer2.writerow(line)
                x=3  
            elif x==3:
                csv_writer3.writerow(line)
                x=4  
            elif x==4:
                csv_writer4.writerow(line)
                x=5
            elif x==5:
                csv_writer5.writerow(line)
                x = 1
        
