import json
search=open('./search.json','r')
out=open('./web.txt','w')

for i in search.readlines():
 j=json.loads(i)
 # filter ipv6 address
 if ':' not in j['ip_str']:
  out.write(j['ip_str']+':'+str(j['port'])+'\n')

search.close()
out.close()