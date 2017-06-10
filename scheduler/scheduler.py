from __future__ import print_function
hour = int(raw_input("enter what hour work starts in 24 hour format ")); 
minute = int(raw_input("enter what minute work starts ")); 
day = str(raw_input("enter what day it is ('week','sat','sun') "));
busnum = 0;
arr246 = []
arrother = []; 

def getHour(line):
    if len(line)>=8 :
        return int(line[5])*10+int(line[6])
    else :
        return int(line[0])*10+int(line[1])
#
def getMinute(line): 
    if len(line) >= 8 : 
        return int(line[8])*10 + int(line[9])
    else: 
        return int(line[3])*10 + int(line[4])
# 
# def getMinute(line): 
#     if len(line) >= 7:
#         return int(line[line[4:].index(':')+1]*10 + line[line[4:].index(':')+2])
#     else :
#         return int(line[line.index(':')+1]*10 + line[line.index(':')+2])
#
def gotowork():
    busnum = 246
    busname = 'text'+str(busnum)+'-'+day+'.txt'
    file246 = open(busname,'r') 
    for line in file246.readlines(): 
        if getHour(line) >= (hour -2) and getHour(line) < (hour ): 
            arr246.append(line)

    busnum = 250
    busname = 'text'+str(busnum)+'-'+day+'.txt'
    file = open(busname,'r')
    for line in file.readlines():
        if getHour(line) >= hour -2 and getHour(line) <= hour: 
            arrother.append(str(busnum)+": "+line)

    busnum = 255
    busname = 'text'+str(busnum)+'-'+day+'.txt'
    file = open(busname,'r')
    for line in file.readlines():
        if getHour(line) >= hour -2 and getHour(line) <= hour: 
            arrother.append(str(busnum)+": "+line)
    file.close()
    file246.close()
#
def printschedule():
    print("246 :")
    for i in arr246:
        if (getHour(i) <= (hour-1 ) and minute == 0 and getMinute(i) <= 5) or ( minute ==30 and  getMinute(i) <=30 and getHour(i) <hour  ):
            print("advised ",end ='')
        print(i,end ='');

    print("****AND THEN****")

    for i in arrother:       
        if ((getHour(i) >= (hour-1 )) and ((minute>=30 and getMinute(i) <=10) or (minute ==0 and getMinute(i) <=40 ) )):
            print("advised ",end='')
        print(i,end ='' )

gotowork()
printschedule()
#go through the file
# check hour, take hour work minus 2 (if minute is 30, take hour minus 0.5, else 1)
# go through file, check if hour bus is within 2 hour between start going hour 
# print 
# do same with other buses.
