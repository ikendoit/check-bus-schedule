# hour = int(input("enter what hour work starts in 24 hour format ")); 
# minute = int(input("enter what minute work starts ")); 
# day = str(input("enter what day it is ('week','sat','sun') "))
hour = 13
minute = 0
day = 'sun'
busnum = 0;
arr246 = []
arrother = []; 

def gethour(line):
    if len(line)>=8 :
        return int(line[5])*10+int(line[6])
    else :
        return int(line[0])*10+int(line[1])
#
def getminute(line): 
    if len(line) >= 8 : 
        return int(line[8])*10 + int(line[9])
    else: 
        return int(line[3])*10 + int(line[4])
# 
def getminute(line): 
    if len(line) >= 7:
        return int(line[line[4:].index(':')+1]*10 + line[line[4:].index(':')+2])
    else :
        return int(line[line.index(':')+1]*10 + line[line.index(':')+2])
#
def gotowork():
    busnum = 246
    busname = 'text'+str(busnum)+'-'+day+'.txt'
    file246 = open(busname,'r') 
    for line in file246.readlines(): 
        if gethour(line) >= (hour -2) and gethour(line) < (hour ): 
            arr246.append(line)

    busnum = 250
    busname = 'text'+str(busnum)+'-'+day+'.txt'
    file = open(busname,'r')
    for line in file.readlines():
        if gethour(line) >= hour -2 and gethour(line) < hour: 
            arrother.append(str(busnum)+": "+line)

    busnum = 255
    busname = 'text'+str(busnum)+'-'+day+'.txt'
    file = open(busname,'r')
    for line in file.readlines():
        if gethour(line) >= hour -2 and gethour(line) < hour: 
            arrother.append(str(busnum)+": "+line)
    file.close()
    file246.close()
#
def printschedule():
    print("246 :")
    for i in arr246:
        if (gethour(i) < (hour -1)):
            print("advised",)
        print(i)
    print("and then :")

    for i in arrother: 
        if (gethour(i) >= (hour -1)):
            print("advised",)
        print(i)

gotowork()
printschedule()
#go through the file
# check hour, take hour work minus 2 (if minute is 30, take hour minus 0.5, else 1)
# go through file, check if hour bus is within 2 hour between start going hour 
# print 
# do same with other buses.
