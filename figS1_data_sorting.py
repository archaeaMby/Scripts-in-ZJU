# _*_ coding:utf-8 _*_
'''
For m-gate article figure 2
Sorting mindist.xvg file data process
Dividing two groups.
1st is hbond group = 1
2nd is non-interaction group = 0

E29_K32<-round(E29_K32,3)
idx<-c("E29:K32","K32:D231","Q36:D231","D231:R234","D231:R235",
       "R234:S179","R235:D134","R234:D134","T138:R235","D134:R79",
       "D134:R137","R137:E29","E29:R279")
names(E29_K32) <- c("Time",c(idx))
new_data <- melt(E29_K32,id="Time")
colnames(new_data) <- c("Time","residue","distance")

f1 <- unique(c(0,0.33,2))
new_data$distance <- cut(new_data$distance, breaks=f1,labels=c(0,1))
f1=unique(new_data$distance)

'''
import os
import numpy as np


def  sorting_data():
    path = '/Users/boyuan/Desktop/sci-research/AAC/paper5_gate/distance/r79a/'
    files = os.listdir(path) # read all files' name in the path.
    # print(files[3][-3:])
    residue_pair=["E29:K32","K32:D231","Q36:D231","D231:R234","D231:R235","R234:S179","R235:D134","R234:D134","T138:R235","D134:R79","D134:R137","R137:E29","E29:R279"]
    xvg_file = [i for i in files if i[-3:] == 'xvg']
    r_For_Read_Data = open(path+'1.read_data.r','w')
    # print(xvg_file)
    # print(xvg_file[2][12:-4])
    r_For_Read_Data.write('library(reshape2)'+"\n")
    r_For_Read_Data.write("setwd(\'" + path + "\')"+"\n")
    for i in xvg_file:
        r_For_Read_Data.write(str.upper(i[13:-4])+"<-read.table(\'"+i+"\')"+"\n")
    r_For_Read_Data.write("\n")
    for i in range(0,len(xvg_file)-1):
        r_For_Read_Data.write('E29_K32$V'+str(i+3)+'<-'+str.upper(xvg_file[i+1][13:-4])+'$V2'+"\n")

    r_For_Read_Data.write("E29_K32<-round(E29_K32,3)"+"\n")
    r_For_Read_Data.write("idx<-c("+str(residue_pair)+')'+"\n")
    r_For_Read_Data.write("names(E29_K32) <- c(\"Time\",c(idx))"+"\n")
    r_For_Read_Data.write("new_data <- melt(E29_K32,id=\"Time\")"+"\n")
    r_For_Read_Data.write("colnames(new_data) <- c(\"Time\",\"residue\",\"distance\")"+"\n")
    r_For_Read_Data.write("f1 <- unique(c(0,0.33,2))"+"\n")
    r_For_Read_Data.write("new_data$distance <- cut(new_data$distance, breaks=f1,labels=c(0,1))"+"\n"+"f1=unique(new_data$distance)"+"\n")
    r_For_Read_Data.write("write.table(new_data, file = \'r79a_data.txt\',col.names = FALSE,row.names = FALSE)"+"\n")
    print("Finished. Find file named 1.read_data.r")
    
if __name__ == '__main__':
    sorting_data()
