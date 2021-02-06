from urllib import request
from bs4 import BeautifulSoup


#saves title and links on a file       
def results(site):
    url = site
    html = request.urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(html, "html.parser") 
    title = soup.find('title')
    a_tag = soup.find_all('a')
    
    print("\nThe title of the page:", title.string)
    
    result = open("file.txt",'w')
    result.write(title.string+"\n")
    
    #write a-tags with hrefs on the file
    for link in a_tag:
        result.writelines(str(link.get("href"))+'\n')
       
    
    
      
results("https://en.wikipedia.org/wiki/Deep_learning")

