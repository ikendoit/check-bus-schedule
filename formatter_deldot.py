def deldot(name):
    arrline = []
    file = open(name,'r')
    for line in file.readlines():
        arrline.append(line);

    file = open(name,'w')
    for line in arrline: 
        line = line.replace('.',':')
        file.write(line)

    file.close()
