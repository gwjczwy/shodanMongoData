# -*- coding: utf-8 -*-# 整理eearch.json中的文件到eearch.ip.txt中# 自动连接并将大于10MB的数据库中所有表的前5条数据保存到本地import json,pymongo,sysa=open("search.json",'r')try:    out=open(sys.argv[1],'a')except:    print('-h\t\tpython3 xx.py /root/download/out.txt')li=[]for l in a.readlines(): data=json.loads(l) li.append(data['ip_str'])a.close()def getDBSize(ip,out):    client = pymongo.MongoClient(ip,serverSelectionTimeoutMS=5000, socketTimeoutMS=5000)    for i in client.list_database_names():        db=client[i]        status = db.command("dbstats")        datasize = int(status['dataSize'] / 1024 /1024)        if datasize>=10:            print(ip+'\t'+i+'\t'+str(datasize)+'MB')            for c in db.list_collection_names():                co=db[c]                col=db['backup'].find({})                out.write(str(ip)+'\n')                for x in range(5):                    out.write('\t'+str(col.next())+'\n')    client.close()for ip in li:    try:        getDBSize(ip,out)    except:        passtry:    out.close()except:    pass