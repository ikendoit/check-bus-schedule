file = open("text246-sun.txt",'r');

arr = file.read();

arr = arr.split(" ");
file1 = open("text246-sun.txt",'w');
for i in arr: 
    file1.write(i + '\n');
