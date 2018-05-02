#Hashem Alnader January 2018

import requests
from bs4 import BeautifulSoup
import math
import time
start_time = time.clock()

with open('PatentNumbers.txt', 'r') as fin:
    with open('PatentsCollected.txt', 'w') as fout:
        patentsFromFile = fin.readlines()
        fout.write('') #Title
        for i in range(0, len(patentsFromFile)):
            stringIn = patentsFromFile[i].strip()
            if stringIn is '':
                pass
            else:
                patent = stringIn
                title = ''
                date = ''
                claim = ''
                abstract = ''
                if patent is '':
                    pass
                else:
                    url = 'https://patents.google.com/patent/' + patent
                    print('Finding ' + url + '...')
                    try:
                        googlePatent = requests.get(url)
                        googlePatentPage = BeautifulSoup(googlePatent.content, 'lxml')
                        title = googlePatentPage.find("span", {"itemprop": "title"}).get_text(strip=True)
                        date = googlePatentPage.find("span", {"itemprop": "priorityDate"}).get_text(strip=True)
                        claim = googlePatentPage.find_all("div", {"class": "claim-text"})
                        for i in range(0, len(claim)):
                            claim[i] = claim[i].get_text(strip=True)
                        abstract = googlePatentPage.find("div", {"class": "abstract"}).get_text(strip=True)
                    except:
                        print('Patent ' + patent + ' not found')
                        pass
                    try:
                        #Prints patent number, title, date, abtract, then all claim text (seperated by tabs)
                        fout.write('\n__' + patent + '_' + title + '_' + date + '_' + abstract + '_' + '\t'.join(claim) + '\n')
                    except:
                        pass
print(math.floor(time.clock() - start_time)/60, ' min')
print('Done')

                   
