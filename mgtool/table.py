# -*- coding: utf-8 -*-
# down table
import json
import pymongo
import sys

tablename=sys.argv[1]
database=sys.argv[2]
ip=sys.argv[3]
out=open("./"+ip+'_'+database+'_'+tablename,'a')

def getDBSize(ip,database,tablename,out):
    client = pymongo.MongoClient(ip,serverSelectionTimeoutMS=5000, socketTimeoutMS=5000)
    db=client[database]
    status = db.command("dbstats")
    datasize = int(status['dataSize'] / 1024 /1024)
    if datasize>=10:
        print(ip+'\t'+database+'\t'+str(datasize)+'MB')
        col=db[tablename].find({})
        out.write(str(ip)+'\n')
        try:
            while True:
                out.write('\t'+str(col.next())+'\n')
        except:
            pass
    client.close()

getDBSize(ip,database,tablename,out)
