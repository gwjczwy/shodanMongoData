# -*- coding: utf-8 -*-
# down data
import json
import pymongo
import sys

ip=sys.argv[1]
out=open("./"+ip,'a')

def getDBSize(ip,out):
    client = pymongo.MongoClient(ip,serverSelectionTimeoutMS=5000, socketTimeoutMS=5000)
    filList=['neowatt']
    for i in client.list_database_names():
        if i in filList:
            continue
        db=client[i]
        status = db.command("dbstats")
        datasize = int(status['dataSize'] / 1024 /1024)
        print(ip+'\t'+i+'\t'+str(datasize)+'MB')
        for c in db.list_collection_names():
            col=db[c].find({})
            out.write(str(ip)+'\n')
            try:
                while True:
                    out.write('\t'+str(col.next())+'\n')
            except:
                pass
    client.close()

getDBSize(ip,out)
