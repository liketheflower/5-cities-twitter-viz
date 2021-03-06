'''
    The code is used as a practise code of python
    cretated on Tue May 14, 2017
    @author: jimmy shen
'''
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d
import collections
import re

def file_parse(file_name, head_length=0):
    
    line_data=[]
    with open(file_name) as f:
        for line in f:
            line_data.append(line.split())
    #print "before",head_length,line_data[0]
    #del line_data[0:head_length]
    # print line_data[0]
    #line_data_array=np.array(line_data)
#line_data_array = line_data_array.astype(float)
    return line_data



def plot_2d(data,i,color_list, label_name):
    x=data[:,12].astype(float)
    y = np.cos(2*np.pi*x)
    y=-0.5+i+0.5*y
    #i=1    -0.5+1+0.5(-1.+1)=0.5~1.5
    #i=2    -0.5+2+0.5(-1.+1)= 1.5~2.5

    print y[0:10]
    print data[0:10,12]
    plt.scatter(x, y,alpha=0.3,label= label_name, color=color_list[i-1], s=0.01)


#2011-09-04_12:57:54

def is_leap_year(year):
    """ if year is a leap year return True
        else return False """
    if year % 100 == 0:
        return year % 400 == 0
    return year % 4 == 0

def doy(Y,M,D):
    """ given year, month, day return day of year
        Astronomical Algorithms, Jean Meeus, 2d ed, 1998, chap 7 """
    if is_leap_year(Y):
        K = 1
    else:
        K = 2
    N = int((275 * M) / 9.0) - K * int((M + 9) / 12.0) + D - 30
    return N


#2011-09-04_12:57:54
def get_time(str_number):
    new_time = []
    str_number=str_number.split("_")
    new_time.extend(str_number[0].split("-"))
    new_time.extend(str_number[1].split(":"))
    year,month,day,hour,minute,second=int(new_time[0]),int(new_time[1]),int(new_time[2]),int(new_time[3]),int(new_time[4]),int(new_time[5])
    number_of_days=0
#visual tweets in five cities during 2011-2014.
    if year<2011 or year >2014:
        print "error, the visual tweets  in five cities is during 2011-2014"
    elif year == 2011:
        time=doy(year,month,day)-1+(hour*60*60+minute*60+second)/(24*60*60.0)
    else:
        for i in range(2011,year):
            number_of_days+=doy(i,12,31)
        time=number_of_days+doy(year,month,day)-1+(hour*60*60+minute*60+second)/(24*60*60.0)
        number_of_days=0
    return time


def change_the_time_into_some_number (data, index=7):
    data[0].append("time")
    for i in range(1,len(data)):
         data[i].append(get_time(data[i][index]))

def check_valid(data):
    for i in range(len(data)-1):
        if len(data[i]) != len(data[i+1]):
            print "error"


def  visualize_city_one_by_one(data_array,city_name):
    #'b', 'g', 'k', 'm'
    color_list=['#69D2E7', '#C3FF68', '#FE4365','#CCFF00','#025D8C']
    for i in range(len(city_name)):
        plot_2d(data_array[data_array[:,0]==city_name[i]],i+1,color_list,city_name[i])
    plt.xlabel('Days since 2011 January 1')
    plt.title("Posts from five cities")
    plt.legend(loc='lower left',scatterpoints=10,fontsize=8)
    plt.savefig('/Users/xshen/Documents/python_r/result_new.pdf')
    plt.show()



if __name__=="__main__":

    file_name = "/Users/xshen/Documents/python_r/tw5cities_after_data_clean.txt"
    data = file_parse(file_name, 0)
    print data[:3]
    
    #remove the first row of the original data
    
    check_valid(data)
    change_the_time_into_some_number (data)
    del data[0]
    print data[:3]
    data_array=np.array(data)
    city_name =list(set(data_array[:,0].tolist()))
    print city_name
    print "data_array[0:10,12]",data_array[0:10,12]
    visualize_city_one_by_one(data_array,city_name)

