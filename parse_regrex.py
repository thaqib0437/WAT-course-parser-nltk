import re
import json 

class dataParser(object):
    def __init__(self,fname,data_dir,max_num):
        self.fname = fname + '.json'
        self.data_dir = data_dir
        self.max_num = max_num
        with open(self.data_dir + self.fname, 'r') as f:
            datastore = json.load(f)
        self.datastore = datastore

    def getStr(self,index):
        prereqRe = re.compile('([\w|\s|\d|,|&|\%|\(|\)|\/]*[;|.]){1}')
        out = prereqRe.findall(self.datastore[index]['prerequisites'])[0] if (prereqRe.match(self.datastore[index]['prerequisites'])) else 'None'
        return out