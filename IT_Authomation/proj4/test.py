import os
p = 'supplier-data/descriptions/'
files = os.listdir(p)
#print(files)
res =''
for file in files:
    with open (p+file) as f:
        data = f.read().split('\n')
    #print(data)
    res +="name: " + data[0] + "<br/>" + "weight: " + data[1] + "<br/><br/>"
    
print(res)
    
    
    
            
