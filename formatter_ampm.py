def ampmformat(name):
    file = open(name,'r')
    arrfile = [] 
    for i in file: 
        i=i.replace('a','')
        i=i.replace('PM','')
        arrfile.append(i)

    file1=open(name,'w')
    for i in arrfile: 
        file1.write(i);

    file.close()
    file1.close()

