# _*_ coding:utf-8 _*_
'''
记得换路径, path=“”
记得换时间!!! f1()函数, 第二个循环, for i .... 这里的数字, 是时间尺度. 
1 Intro
    For m-gate article symmetry figure
    calculate every angle's degree
        A = h3-[h1]-h5
        B = h1-[h3]-h5
        C = h3-[h5]-h1
        a = length of h3-h5
        b = length of h1-h5
        c = length of h1-h3
        a = h3-h5
        b = h1-h5
        c = h1-h3

2 Function list
    1.ndx() #Generate GROMACS4.5 make_ndx command
    2.dist() #Generate GROMACS4.5 g_dist command
    3.rread() #Switch to Rstudio and abstract all distance cols from dist.xvg files
    4.f1() #Calculate the final deviation degree
    5.all_degree_deviation() #Switch to Rstudio and complie all degree deveation results to one file
    6.data_rearrange() #Matrix for plot heatmap


3 Samples
    sample1:
        make_ndx -f pr.tpr -o ~/~/paper5_m_gate/symmtery/symmetry_all4A_v25.ndx <<U
        3 & ri 25
        name 10 25
        3 & ri 127
        name 11 127
        3 & ri 224
        name 12 224
        q
        U

    sample2:
        g_dist -f pr_100ps.xtc -s pr.tpr -n ~/paper5_m_gate/symmtery/symmetry.ndx -xvg none -o ~/paper5_m_gate/symmtery/k22-l127_dist.xvg <<U
        10
        11
        U

    sample3
        path = '/Users/boyuan/Desktop/sci-research/AAC/paper5_gate/symmetry/all4A'
        25_a_dist <- read.table("25_a_dist.xvg")
        e29_k32$V1<- e29_k32$V1
        e29_k32$V3<- k32_n276$V2


4 Plot r script
library(ggplot2)
library(RColorBrewer)
library(scales)
setwd("/Users/boyuan/Desktop/sci-research/AAC/paper5_gate/symmetry/all4A/")

mydata1 <- read.table('7.data_for_plot.txt')
# Order y axis in my sequence.
mydata1$V4 <- factor(mydata1$V2, levels = c("V25-V130-S227","A26-Y131-Y228","P27-P132-P229","I28-L133-F230","E29-D134-D231",
                                            "R30-F135-T232","V31-A136-V233","K32-R137-R234","L33-T138-R235","L34-R139-R236",
                                            "L35-L140-M237","Q36-A141-M238","V37-A142-M239"))
classified_data <- cut(mydata1$V3,breaks=seq(-1,20,1))
mydata1$V5 <- classified_data
gradientC=c('#7b0041',"#F5F5F5",'#1E540F')
col <- colorRampPalette(gradientC)(21)
png('all4A.png', res=500,height = 6, width = 20,units = "cm")
l <- c("-1",)
w <- ggplot(mydata1,aes(x=V1,y=V4,fill=V5))+geom_raster()+
  xlab("Time (ns)")+ylab("")+
  theme_bw()+
  theme(panel.grid = element_blank(),
        title =element_text(family="Helvetica",face="bold",color="black",size=12),
        axis.title.x=element_text(family="Helvetica",face="bold",color="black",size=12),
        axis.text.x=element_text(family="Helvetica",color="black",face = "bold",size=11),
        axis.text.y=element_text(family="Helvetica",color="black",face = "bold",size=11),
        axis.title.y=element_text(family="Helvetica",face="bold",color="black",size=12),
        legend.text=element_text(family="Helvetica",color="black",size=10),
        legend.title=element_text(face="bold",color="black",size=12),
  )
w + #scale_fill_brewer(palette = "RdYlBu")
#scale_fill_brewer(palette = "PiYG")
  #scale_fill_manual(low = "orange",mid = "white", midpoint = 7,high = "blue")
#scale_fill_manual(values = c('darkmagenta','white','darkcyan'))
scale_fill_manual(values=col)+
  guides(fill = guide_legend(reverse = TRUE,title = "φ"))
dev.off()


library(ggplot2)
library(RColorBrewer)
library(scales)
setwd("/Users/boyuan/Desktop/sci-research/AAC/paper5_gate/symmetry/wt/")
mydata1 <- read.table('7.data_for_plot.txt')

# Order y axis in my sequence.
sequence <- rev(c("V25-V130-S227","A26-Y131-Y228","P27-P132-P229","I28-L133-F230","E29-D134-D231",
  "R30-F135-T232","V31-A136-V233","K32-R137-R234","L33-T138-R235","L34-R139-R236",
  "L35-L140-M237","Q36-A141-M238","V37-A142-M239"))
mydata1$V4 <- factor(mydata1$V2, levels = sequence)
a <- seq(0,20,2.5)
a[length(a)]<- Inf
classified_data <- cut(mydata1$V3,breaks=a,include.lowest = TRUE)
mydata1$V5 <- classified_data
mydata1$V1 <- mydata1$V1*10

gradientC=c('#7b0041',"#F5F5F5",'#1E540F')
col <- colorRampPalette(gradientC)(8)
png('wt2.png', res=500,height = 10, width = 20,units = "cm")
w <- ggplot(mydata1,aes(x=V1,y=V4,fill=V5))+geom_raster()+
  xlab("Time (ns)")+ylab("")+
  theme_bw()+
  theme(panel.grid = element_blank(),
        title =element_text(family="Helvetica",face="bold",color="black",size=12),
        axis.title.x=element_text(family="Helvetica",face="bold",color="black",size=12),
        axis.text.x=element_text(family="Helvetica",color="black",face = "bold",size=11),
        axis.text.y=element_text(family="Helvetica",color="black",face = "bold",size=10),
        axis.title.y=element_text(family="Helvetica",face="bold",color="black",size=12),
        legend.text=element_text(family="Helvetica",color="black",size=10),
        legend.title=element_text(face="bold",color="black",size=12),
        legend.key.size = unit(0.45,"cm"))
w+
  scale_fill_brewer(palette = "PRGn")+ggtitle('WT')+
  guides(fill = guide_legend(reverse = TRUE,title = "φ"))

dev.off()




'''

# import module
import os
# import xlrd
# import xlall4A
import math
import numpy as np

# functions module
def ndx():
    path = "/Users/boyuan/Desktop/sci-research/AAC/paper5_gate/symmetry/all4A/"
    makendx = open(path+"1.symmetry_ndx_making_shell.sh", 'w')
    for i in range(25, 38):
        makendx.write('make_ndx -f pr.tpr -o ~/paper5_m_gate/symmtery/all4A/symmetry_all4A_'+str(i)+'.ndx <<U'+"\n")
        makendx.write("3&ri"+str(i)+"\n")
        makendx.write("name 10"+' '+str(i)+"\n")
        makendx.write("3&ri"+str(i+105)+"\n")
        makendx.write("name 11"+' '+str(i+105)+"\n")
        makendx.write("3&ri"+str(i+202)+"\n")
        makendx.write("name 12" +' '+str(i + 202)+"\n")
        makendx.write("q"+"\n"+"U"+"\n"+"\n")
    print("1. finish ndx")


def dist():
    path = "/Users/boyuan/Desktop/sci-research/AAC/paper5_gate/symmetry/all4A/"
    dist = open(path + "2.symmetry_dist_calculation_shell.sh", 'w')
    for i in range(25, 38):
        dist.write('g_dist -f pr_100ps.xtc -s pr.tpr -n ~/paper5_m_gate/symmtery/all4A/symmetry_all4A_'+str(i)+'.ndx -xvg none -o ~/paper5_m_gate/symmtery/all4A/'+str(i)+'_a_dist.xvg <<U' + "\n")
        dist.write("11" + "\n" + "12"+"\n"+"U"+"\n")
        dist.write('g_dist -f pr_100ps.xtc -s pr.tpr -n ~/paper5_m_gate/symmtery/all4A/symmetry_all4A_'+str(i)+'.ndx -xvg none -o ~/paper5_m_gate/symmtery/all4A/'+str(i)+'_b_dist.xvg <<U' + "\n")
        dist.write("10" + "\n" + "12"+"\n"+"U"+"\n")
        dist.write('g_dist -f pr_100ps.xtc -s pr.tpr -n ~/paper5_m_gate/symmtery/all4A/symmetry_all4A_'+str(i)+'.ndx -xvg none -o ~/paper5_m_gate/symmtery/all4A/'+str(i)+'_c_dist.xvg <<U' + "\n")
        dist.write("10" + "\n" + "11"+"\n"+"U"+"\n"+"\n")
    print("2. finish dist")


def rread():
    path = "/Users/boyuan/Desktop/sci-research/Master/AAC/paper5_gate/MDPI/symmetry/all4A/"
    r = open(path + "3.symmetry_r_all4A.r", 'w')
    r.write("setwd(\"/Users/boyuan/Desktop/sci-research/AAC/paper5_gate/symmetry/all4A\")"+"\n")
    for i in range(25, 38):
        r.write("a_dist_"+str(i)+" <- read.table(\""+str(i) + '_a_dist.xvg")'+"\n")
        r.write("b_dist_"+str(i)+" <- read.table(\""+str(i) + '_b_dist.xvg")'+"\n")
        r.write("c_dist_"+str(i)+" <- read.table(\""+str(i) + '_c_dist.xvg")'+"\n")
        # r.write("\n")
        r.write('a_dist_'+str(i)+'$V1<- a_dist_'+str(i)+'$V1'+"\n")
        r.write('a_dist_'+str(i)+'$V3<- b_dist_'+str(i)+'$V2'+"\n")
        r.write('a_dist_'+str(i)+'$V4<- c_dist_'+str(i)+'$V2'+"\n")
        r.write("a_dist_"+str(i)+"<-round(a_dist_"+str(i)+",3)"+ "\n")
        r.write("write.table(a_dist_"+str(i)+"[1:4], file = \'4.raw_data"+str(i)+".txt\',col.names = FALSE,row.names = FALSE)" + "\n"+ "\n")
        r.write("print(\"switch to PyCharm\")"+"\n")
    # for j in range(26, 38):
    #     r.write('a_dist_25$V'+ ' ' +'<- '+"a_dist_"+str(j)+'$V2'+"\n")
    #     r.write('a_dist_25$V'+ ' ' +'<- '+"b_dist_"+str(j)+'$V2'+"\n")
    #     r.write('a_dist_25$V'+ ' ' +'<- '+"c_dist_"+str(j)+'$V2'+"\n")
    print("3. finish rread; switch to Rstudio")

def f1():
    # transform distance data to matirx via numpy
    path = '/Users/boyuan/Desktop/sci-research/Master/AAC/paper5_gate/MDPI/symmetry/all4A/'
    for j in range(25,38):
        raw_data = np.loadtxt(path+'4.raw_data'+str(j)+'.txt')
        degree = open(path + '5.degree_all4A'+str(j)+'.txt', 'w')
        for i in range(0,1501):
            # read distance from matrix
            a = raw_data[i,1]
            b = raw_data[i,2]
            c = raw_data[i,3]

            # calculate three sides' length
            a_cos = (b**2 + c**2 - a**2) / (2*b*c)
            a_cos = round(a_cos,2)
            # print(a_length)
            b_cos= (a**2 + c**2 - b**2) / (2*a*c)
            b_cos = round(b_cos, 2)

            c_cos = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
            c_cos = round(c_cos, 2)

                # import triangle function, such as cos(), sin(), acos() ...
            a_arccos = np.arccos(a_cos)
            b_arccos = np.arccos(b_cos)
            c_arccos= np.arccos(c_cos)

            A = math.degrees(a_arccos)
            A = round(A, 2)
            B = math.degrees(b_arccos)
            B = round(B, 2)
            C = math.degrees(c_arccos)
            C = round(C, 2)

            # calculating total deviation. follow kunji 2021's function
            a_deviation = abs(A - 60)
            b_deviation = abs(B - 60)
            c_deviation = abs(C - 60)
            deviation = (a_deviation + b_deviation + c_deviation)/3
            deviation = round(deviation, 2)
            degree.write(str(raw_data[i,0])+' ')
            degree.write(str(deviation)+"\n")
        degree.close()
    print("4. DONE f1")


def all_degree_deviation():
    path = '/Users/boyuan/Desktop/sci-research/Master/AAC/paper5_gate/MDPI/symmetry/all4A/'
    dev = open(path+"6.generating_all_degree_deviation.r","w")
    dev.write("setwd('//Users/boyuan/Desktop/sci-research/Master/AAC/paper5_gate/MDPI/symmetry/all4A')"+"\n")
    for i in range(25,38):
        dev.write("degree_all4A"+str(i)+ " <- read.table(\"5.degree_all4A"+ str(i) +".txt\")" + "\n")
    dev.write('degree_all4A25$V1 <- degree_all4A25$V1' + "\n")
    for j in range(26,38):
        dev.write('degree_all4A25$V'+str(j-23)+'<- degree_all4A'+str(j)+'$V2'+"\n")
    dev.write("write.table(degree_all4A25, file = \'7.wait_for_matrix_rebuild.txt\',col.names = FALSE,row.names = FALSE)" + "\n"+ "\n")
    dev.write("print(\"switch to PyCharm\")")
    dev.close()
    print("5. finish all_degree_deviation, switch to R")


def data_rearrange():
    path = '/Users/boyuan/Desktop/sci-research/Master/AAC/paper5_gate/MDPI/symmetry/all4A/'
    # transform distance data to matirx via numpy
    mydata = np.loadtxt(path+'7.wait_for_matrix_rebuild.txt')
    plot = open(path+'7.data_for_plot.txt','w')
    h1=['V25','A26','P27','I28','E29','R30','V31','K32','L33','L34','L35','Q36','V37']
    h2=['V130','Y131','P132','L133','D134','F135','A136','R137','T138','R139','L140','A141','A142']
    h3=['S227','Y228','P229','F230','D231','T232','V233','R234','A235','R236','M237','M238','M239']
    name = [h1[i]+'-'+h2[i]+'-'+h3[i] for i in range(0,len(h1))]
    # print(name[3:5])
    for i in range(0, 1501):
        for j in range(0,13):
            plot.write(str(mydata[i,0]/1000))
            plot.write(' ')
            # plot.write(str(j+1))
            plot.write(' ')
            plot.write(name[j])
            plot.write(' ')
            plot.write(str(mydata[i, j+1]))
            plot.write('\n')
    plot.close()
    print("6. done data rearrange, use R to plot. Plot code is saved at the explanation section, subsection 4")


if __name__ == '__main__':
    # pass
    # ndx()
    # dist()
    # rread()
    # f1()
    # all_degree_deviation()
    data_rearrange()