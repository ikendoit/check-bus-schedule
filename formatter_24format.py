name = 'text255-week.txt'

def translate(num):
    trans = [13,14,15,16,17,18,19,20,21,22,23,24]
    return trans[num-1]

def getnum(line):
    if line[1]!=':':
        num = line[0]+line[1]
        num = int(num);
        line =  str(translate(num))+line[2:]
        
    else :
        num = int(line[0])
        line = str(translate(num))+line[1:]
    return line;

def reformat(name):
    file = open(name,'r')
    pm = False
    arrfile =[] 
    for line in file.readlines(): 

        if len(line) == 5:
            line =''.join(['0',line]);
        if (line[0] =='0' and line[1] == '1')  : 
            pm = True;
        if pm:
            arrfile.append(getnum(line))
        else :
            arrfile.append(line);

    file1 = open(name,'w')
    for i in arrfile: 
        file1.write(i)
    file1.close()
    file.close()






