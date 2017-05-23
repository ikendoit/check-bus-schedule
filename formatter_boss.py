import formatter_24format
import formatter_deldot
import formatter_ampm 

arrnum = [246,250,255]
arrprop = ['week','sun','sat']

for num in arrnum : 
    for prop in arrprop: 
        name ="text"+str(num)+'-'+prop+'.txt'
        # formatter_24format.reformat(name)
        # formatter_deldot.deldot(name)
        formatter_ampm.ampmformat(name);