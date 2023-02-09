import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import logging
lis=[]

# creating a recursive function to get links and appending them to a csv file

def lin(url):
    
    response=requests.get(url)
    
    try:
        soup=BeautifulSoup(response.content,'html.parser')
        
        for i in soup.find_all('a',href=True):                             # finds all the web elements with tag a
            
            b=i['href']                                                    # b is the link in the web element
            
            if b not in lis and re.search(rf"^\b(?=\w){url}\b(?!\w)",b):   # checks if the link already existed in the list and the link starting with the base url
                
                lis.append(b)                                              # if the link not in list it will be appended
                
                df=pd.DataFrame([b])                                       # that link is turned into dataframe
                
                df.to_csv('links.csv',mode='a',index=False,header=False)   # append that link to csv file
                
                lin(b)                                                     # again calling lin function
    
    except Exception as Argument:

        f = open("log.txt", "a")     # creating/opening a file
        
        f.write(str(Argument))       # writing in the file
      
        f.close()                    # closing the file
        
lin('https://telanganatoday.com')
