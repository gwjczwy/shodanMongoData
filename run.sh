# 用来自动下载shodan中关于开放mongodb数据库的数据,并筛选出其中比较大的数据库
shodan download search "mongodb"
gzip -d search.json.gz
python3 run.py