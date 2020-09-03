# -*- coding: utf-8 -*-
# down database
import json
import pymongo
import sys

ip=sys.argv[1]
database=sys.argv[2]
out=open("./"+ip+'_'+database,'a')

def getDBSize(ip,database,out):
    client = pymongo.MongoClient(ip,serverSelectionTimeoutMS=5000, socketTimeoutMS=5000)
    db=client[database]
    status = db.command("dbstats")
    datasize = int(status['dataSize'] / 1024 /1024)
    if datasize>=10:
        print(ip+'\t'+database+'\t'+str(datasize)+'MB')
        for c in db.list_collection_names():
            col=db[c].find({})
            out.write(str(ip)+'\n')
            try:
                while True:
                    out.write('\t'+str(col.next())+'\n')
            except:
                pass
    client.close()

getDBSize(ip,database,out)
