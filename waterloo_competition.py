from bs4 import BeautifulSoup
import urllib.parse
import requests
import json
import time

def getDomains(phrase):
    phrase = phrase.replace(' ', '+')
    r = requests.get('https://duckduckgo.com/html/?q='+phrase+'&t=h', headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all('a', attrs={'class':'result__a'}, href=True)
    domains=[]
    for link in results:
        url = link['href']
        o = urllib.parse.urlparse(url)
        d = urllib.parse.parse_qs(o.query)
        try:
            print(d['uddg'][0])
        except:
            continue
        domains.append(d['uddg'][0])
    return domains

def getProxies():
    r = requests.get('https://free-proxy-list.net/', headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.text, 'html.parser')
    results = []
    header=True
    counter=0
    for result in soup.find_all('tr'):
        if counter==30:
            break
        if header:
            header=False
            continue
        data = result.find_all('td') 
        if len(data) == 0 or len(data)==1:
            continue
        proxy={'https':data[0].contents[0]+':'+data[1].contents[0]}
        results.append(proxy)
        counter+=1
    return results


def load():
    file = open("D:/data/train/train.json",'r')
    data = json.loads(file.read())
    return data

def main():
    data = load()
    domains={}
    trainData={}
    backupCounter=0
    numOfBackup=1
    for d in data:
        time.sleep(8)
        print(d['claim'])
        domainList = getDomains(d['claim'])
        trainData[d['claim']] = domainList
        for domain in domainList:
            if domain in domains:
                domains[domain] +=1
                continue
            domains[domain] = 1
        backupCounter+=1
        if(backupCounter > 100):
            numOfBackup+=1
            file=open("./backup"+ str(numOfBackup)+".json", 'w')
            json.dump(domains, file)
            file.close()
            file=open("./training"+ str(numOfBackup)+".json", 'w')
            json.dump(trainData, file)
            file.close()


if __name__ == '__main__':
    main()
