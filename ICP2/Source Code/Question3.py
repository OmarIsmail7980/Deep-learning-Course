#open the file
infile = open('file1.txt', 'r')

#replace endline with space
line = infile.readline().replace("\n","")


dic = {}

while line!="":
    #read words in line
    for xstr in line.split(" "):
        if xstr in dic.keys():
            dic[xstr] = dic[xstr]+1
        else:
            dic[xstr]=1
    line = infile.readline().replace("\n","") 
    

       
outfile = open('file.txt', 'w')

for i in dic.keys():
    outfile.write(i+str(dic[i])+"\n")
    
    
    
    
