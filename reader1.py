import docx2txt
# create raw data base
# my_text = docx2txt.process("250-horseshoe-sat.docx");
# isPm = False;
# file = open("text250-1sat.txt","w+");
# file.write(my_text);


# file = open("text250-1sat.txt","r");

# count = 0 ;
# mystop = [];
# for line in file: 
#     if (ord(line[0]) ==45) or (ord(line[0]) >=48 and ord(line[0]) <=57  ):
#         count+=1;
#         if ((count -6 ) % 8) == 0:
#             mystop.append(line);

#seperate Am and Pm

file1 = open("text255-sat.txt","r")
mystop = []; 
isPm = False;
for line in file1 : 
    mystop.append(line);

file1 =open("text255-sat.txt",'w')
for i in mystop: 
    if (i[0] == '1' and i[1] == '2' ):
        isPm = True; 
    if (isPm == True ):
        i = i.rstrip();
        i= ''.join([i,' PM\n']);
    file1.write(i);

file1.close();
