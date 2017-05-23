
file1 = open("text250-1sat.txt","r")
file2 = open("text250-1satreal.txt",'w+')
isPm = False;
for i in file1: 
    if (i[0] == '1' and i[1] == '2' ):
        isPm = True; 
    if (isPm == True ):
        i = i.rstrip();
        i= ''.join([i,' PM\n']);
    file2.write(i);
