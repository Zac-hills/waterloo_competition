import json
from urllib.parse import urlparse



def createDataMatrix(filename):
    mainDomain={}
    with open(filename, 'r') as file:
        data=json.load(file)
        for d in data:
            url=urlparse(d)
            result = '{uri.scheme}://{uri.netloc}/'.format(uri=url)
            if not result in mainDomain:
                mainDomain[result] = len(mainDomain)
    return mainDomain


def createTrainingData():
    file = open("./datamatrix.json", 'r')
    matrix = json.load(file)
    file.close()
    file = open("./train/train.json", 'r')
    oldData = json.load(file)
    file.close()
    file = open("./trainingdata/training192.json",'r')
    newData = json.load(file)

def main():
    matrix=createDataMatrix('./trainingdata/backup1925.json')
    with open('datamatrix.json','w') as file:
        json.dump(matrix, file)

    return



if __name__ == "__main__":
    main()