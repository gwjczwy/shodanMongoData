# ׼������
pip3 install pymongo
pip3 install shodan

shodan init SHODAN_API_KEY #û���˺ŵĿ��Ե�githubй¶�ļ�ȥ��,�����ؼ��� SHODAN_API_KEY
shodan info  #�鿴�Ƿ����㹻�Ĳ�ѯ����,����0����

# ʳ�÷���
### �Զ���shodan��ȡ����MongoDB��Ϣ���������ӣ�������ݿ��С����10M�����ݿ��ַ�����ݿ���
./mongodb.sh

#�ѿ�ű�
### ���������ݿ�
mgtool/data.py
    data.py 127.0.0.1

### ��ָ�����ݿ�
mgtool/db.py
    db.py 127.0.0.1 users

### ��ָ����
mgtool/table.py
    table.py 127.0.0.1 users addres

### ָ�����ݿⲻ�� ��Ҫ�޸Ľű�
mgtool/data_filter.py
    data_filter.py 127.0.0.1