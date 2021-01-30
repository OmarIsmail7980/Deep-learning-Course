#open the file
infile = open('file.txt', 'r')

line = infile.readline()

count = 0

while line!="":
    #read words in line
    for xstr in line.split():
        count = count+1
        #print word with it's count
        print(xstr,count,'\n')
         
    #set the count for next line
    count = 0
    #read the following line
    line= infile.readline()
    
    
